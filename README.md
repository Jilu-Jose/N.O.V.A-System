# Satellite Telemetry Fault Detection

This project is a Flask-based web application that predicts faults in satellite systems based on telemetry data. It utilizes an ensemble of machine learning models to provide robust predictions and a confidence score through majority voting.


Live: https://n-o-v-a-system.onrender.com/
## Features
- **Ensemble Machine Learning:** Uses multiple pre-trained models to make predictions:
  - Decision Tree
  - K-Nearest Neighbors (KNN)
  - Logistic Regression
  - Multi-Layer Perceptron (MLP) Neural Network
  - Random Forest
  - Support Vector Classifier (SVC)
  - XGBoost
- **Majority Voting System:** Aggregates individual model predictions to determine the overall system status (`FAULT DETECTED` or `NORMAL`) and calculates a confidence percentage.
- **REST API:** Exposes a `/predict` endpoint that accepts telemetry data in JSON format and returns prediction details.
- **Web Interface Pages:** Includes basic routes for landing (`/`), dashboard (`/dashboard`), and login (`/login`).

## Input Features
The `/predict` endpoint expects JSON data with the following telemetry fields:
- `temperature_c`: Temperature in Celsius
- `humidity_percent`: Humidity percentage
- `pressure_pa`: Pressure in Pascals
- `gas_ppm`: Gas concentration in ppm
- `radiation_usv_h`: Radiation level in µSv/h
- `battery_voltage_v`: Current battery voltage
- `solar_current_ma`: Solar panel current in mA
- `cpu_temp_c`: CPU temperature in Celsius
- `vibration_mms`: Vibration in mm/s
- `satellite_mode`: Current operating mode
- `region`: Operating region
- `battery_voltage_next`: Predicted next battery voltage
- `altitude_m`: Altitude in meters
- `magnetic_field_uT`: Magnetic field strength in µT
- `solar_panel_temp_c`: Solar panel temperature in Celsius
- `gyro_stability_index`: Gyroscope stability index

## Installation and Setup

1. **Navigate to the application directory**

2. **Install Required Packages:**
   Ensure you have Python installed, then install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   Start the Flask development server:
   ```bash
   python app.py
   ```
   The application will become available at `http://127.0.0.1:5000` (by default).

## API Usage

### `POST /predict`

**Request Body (JSON):**
```json
{
    "temperature_c": 25.5,
    "humidity_percent": 45.0,
    "pressure_pa": 101325,
    "gas_ppm": 400,
    "radiation_usv_h": 0.15,
    "battery_voltage_v": 12.5,
    "solar_current_ma": 500,
    "cpu_temp_c": 40.0,
    "vibration_mms": 0.1,
    "satellite_mode": 1,
    "region": 2,
    "battery_voltage_next": 12.4,
    "altitude_m": 400000,
    "magnetic_field_uT": 45.0,
    "solar_panel_temp_c": 55.0,
    "gyro_stability_index": 0.98
}
```

**Successful Response (JSON):**
```json
{
    "confidence": 100.0,
    "fault_count": 0,
    "overall_status": "NORMAL",
    "predictions": {
        "Decision Tree": {
            "prediction": 0,
            "status": "NORMAL"
        },
        ...
    },
    "success": true,
    "total_models": 7
}
```
