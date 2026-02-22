from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os
import joblib

app = Flask(__name__)

# Load all models
models = {}
model_files = {
    'Decision Tree': 'DecTree_SAT_NOVA.pkl',
    'KNN': 'KNN_SAT_NOVA.pkl',
    'Logistic Regression': 'LogReg_SAT_NOVA.pkl',
    'MLP Neural': 'mlp_SAT_NOVA.pkl',
    'Random Forest': 'RanForest_SAT_NOVA.pkl',
    'SVC': 'SVC_SAT_NOVA.pkl',
    'XGBoost': 'XGB_T_NOVA.pkl'
}

def load_models():
    for name, filename in model_files.items():
        try:
            with open(filename, 'rb') as f:
                models[name] = joblib.load(f)
            print(f"Loaded {name} successfully")
        except Exception as e:
            print(f"Error loading {name}: {e}")

load_models()

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extract features in correct order
        features = [
            float(data.get('temperature_c', 0)),
            float(data.get('humidity_percent', 0)),
            float(data.get('pressure_pa', 0)),
            float(data.get('gas_ppm', 0)),
            float(data.get('radiation_usv_h', 0)),
            float(data.get('battery_voltage_v', 0)),
            float(data.get('solar_current_ma', 0)),
            float(data.get('cpu_temp_c', 0)),
            float(data.get('vibration_mms', 0)),
            float(data.get('satellite_mode', 0)),
            float(data.get('region', 0)),
            float(data.get('battery_voltage_next', 0)),
            float(data.get('altitude_m', 0)),
            float(data.get('magnetic_field_uT', 0)),
            float(data.get('solar_panel_temp_c', 0)),
            float(data.get('gyro_stability_index', 0))
        ]
        
        input_data = np.array([features])
        
        # Get predictions from all models
        predictions = {}
        for name, model in models.items():
            try:
                pred = model.predict(input_data)[0]
                predictions[name] = {
                    'prediction': int(pred),
                    'status': 'FAULT DETECTED' if pred == 1 else 'NORMAL'
                }
            except Exception as e:
                predictions[name] = {
                    'prediction': -1,
                    'status': f'Error: {str(e)}'
                }
        
        # Majority voting
        fault_count = sum(1 for p in predictions.values() if p['prediction'] == 1)
        total_models = len([p for p in predictions.values() if p['prediction'] != -1])
        
        overall_status = 'FAULT DETECTED' if fault_count > total_models / 2 else 'NORMAL'
        confidence = (max(fault_count, total_models - fault_count) / total_models * 100) if total_models > 0 else 0
        
        return jsonify({
            'success': True,
            'overall_status': overall_status,
            'confidence': round(confidence, 2),
            'fault_count': fault_count,
            'total_models': total_models,
            'predictions': predictions
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)