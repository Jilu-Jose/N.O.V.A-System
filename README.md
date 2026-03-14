<div align="center">

<br/>

```
███╗   ██╗ ██████╗ ██╗   ██╗ █████╗
████╗  ██║██╔═══██╗██║   ██║██╔══██╗
██╔██╗ ██║██║   ██║██║   ██║███████║
██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
```

# Satellite Telemetry Fault Detection System

**Real-time anomaly detection for satellite systems powered by an ensemble of machine learning models**

<br/>

[![Live Demo](https://img.shields.io/badge/Live_Demo-n--o--v--a--system.onrender.com-0A66C2?style=for-the-badge&logo=googlechrome&logoColor=white)](https://n-o-v-a-system.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML_Engine-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble-FF6600?style=for-the-badge&logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)

<br/>

</div>

---

## ![readme](https://img.shields.io/badge/-Overview-1a1a2e?style=flat-square&logo=readme&logoColor=white) Overview

**NOVA** is a Flask-based fault detection system that analyzes satellite telemetry data in real time. It uses an **ensemble of 7 machine learning models** with majority voting to classify system states as `NORMAL` or `FAULT DETECTED`, returning a confidence score alongside each prediction.

Sensor data is collected via an **Arduino-based multi-sensor array** that captures real-world environmental and system health parameters — bridging physical IoT hardware with intelligent ML diagnostics.

---

## ![features](https://img.shields.io/badge/-Key_Features-1a1a2e?style=flat-square&logo=todoist&logoColor=white) Key Features

| | Feature | Description |
|---|---|---|
| ![](https://img.shields.io/badge/Ensemble_ML-0078D4?style=flat-square&logo=azureml&logoColor=white) | **Ensemble ML** | 7 pre-trained models working in concert for robust predictions |
| ![](https://img.shields.io/badge/Majority_Voting-6A0DAD?style=flat-square&logo=checkmarx&logoColor=white) | **Majority Voting** | Aggregates predictions into a single status with confidence % |
| ![](https://img.shields.io/badge/Arduino_Integration-00979D?style=flat-square&logo=arduino&logoColor=white) | **Arduino Integration** | Real sensor array feeds live telemetry into the pipeline |
| ![](https://img.shields.io/badge/REST_API-FF6C37?style=flat-square&logo=postman&logoColor=white) | **REST API** | Simple `/predict` endpoint accepts JSON telemetry payloads |
| ![](https://img.shields.io/badge/Web_Interface-4285F4?style=flat-square&logo=googlechrome&logoColor=white) | **Web Interface** | Dashboard, landing page, and login portal included |
| ![](https://img.shields.io/badge/Cloud_Deployed-46E3B7?style=flat-square&logo=render&logoColor=white) | **Cloud Deployed** | Live and accessible via Render cloud platform |

---

## ![ml](https://img.shields.io/badge/-Machine_Learning_Models-1a1a2e?style=flat-square&logo=scikitlearn&logoColor=white) Machine Learning Models

The system runs every incoming telemetry payload through **all 7 models simultaneously** and applies majority voting to arrive at a final prediction.

```
┌─────────────────────────────────────────────────────────────┐
│                    Telemetry Input (JSON)                    │
└─────────────────────┬───────────────────────────────────────┘
                      │
        ┌─────────────▼──────────────┐
        │     Feature Preprocessor   │
        └──┬──┬──┬──┬──┬──┬──┬──────┘
           │  │  │  │  │  │  │
     ┌─────▼──▼──▼──▼──▼──▼──▼──────┐
     │  Decision Tree  │    KNN      │
     │  Logistic Reg.  │    MLP      │
     │  Random Forest  │    SVC      │
     │           XGBoost             │
     └──────────────┬────────────────┘
                    │
          ┌─────────▼──────────┐
          │   Majority Voting  │
          └─────────┬──────────┘
                    │
     ┌──────────────▼───────────────┐
     │  NORMAL  ·or·  FAULT DETECTED │
     │      + Confidence Score %     │
     └───────────────────────────────┘
```

| Model | Type |
|---|---|
| ![](https://img.shields.io/badge/Decision_Tree-informational?style=flat-square&logo=graphql&logoColor=white) | Tree-based classifier |
| ![](https://img.shields.io/badge/K--Nearest_Neighbors-informational?style=flat-square&logo=googlecolab&logoColor=white) | Instance-based learning |
| ![](https://img.shields.io/badge/Logistic_Regression-informational?style=flat-square&logo=chartdotjs&logoColor=white) | Linear probabilistic model |
| ![](https://img.shields.io/badge/MLP_Neural_Network-informational?style=flat-square&logo=pytorch&logoColor=white) | Multi-layer perceptron |
| ![](https://img.shields.io/badge/Random_Forest-informational?style=flat-square&logo=leaflet&logoColor=white) | Bagged ensemble of trees |
| ![](https://img.shields.io/badge/Support_Vector_Classifier-informational?style=flat-square&logo=apacheairflow&logoColor=white) | Margin-based classifier |
| ![](https://img.shields.io/badge/XGBoost-informational?style=flat-square&logo=xgboost&logoColor=white) | Gradient boosted trees |

---

## ![hw](https://img.shields.io/badge/-Hardware_%26_Sensors-1a1a2e?style=flat-square&logo=arduino&logoColor=white) Hardware & Sensors

Telemetry data is captured via an **Arduino microcontroller** interfaced with the following sensor array:

| Sensor | Measurements |
|---|---|
| ![](https://img.shields.io/badge/DHT11_%2F_DHT22-00979D?style=flat-square&logo=arduino&logoColor=white) | `temperature_c`, `humidity_percent` |
| ![](https://img.shields.io/badge/BMP180_%2F_BME280-00979D?style=flat-square&logo=arduino&logoColor=white) | `pressure_pa`, `altitude_m` |
| ![](https://img.shields.io/badge/MQ--Series_Gas_Sensor-00979D?style=flat-square&logo=arduino&logoColor=white) | `gas_ppm` |
| ![](https://img.shields.io/badge/Geiger_Counter_Module-00979D?style=flat-square&logo=arduino&logoColor=white) | `radiation_usv_h` |
| ![](https://img.shields.io/badge/INA219_Voltage_%2F_Current-00979D?style=flat-square&logo=arduino&logoColor=white) | `battery_voltage_v`, `solar_current_ma` |
| ![](https://img.shields.io/badge/MPU6050_IMU-00979D?style=flat-square&logo=arduino&logoColor=white) | `gyro_stability_index`, `vibration_mms` |
| ![](https://img.shields.io/badge/HMC5883L_Magnetometer-00979D?style=flat-square&logo=arduino&logoColor=white) | `magnetic_field_uT` |

> The Arduino continuously samples all parameters, formats them into a structured payload, and transmits them to the Flask application for real-time inference.

---

## ![stack](https://img.shields.io/badge/-Tech_Stack-1a1a2e?style=flat-square&logo=stackshare&logoColor=white) Tech Stack

```
┌──────────────┐  ┌──────────────────────────────────────────┐
│  FRONTEND    │  │  HTML5 · CSS3 (custom animations) · JS   │
├──────────────┤  ├──────────────────────────────────────────┤
│  BACKEND     │  │  Python 3.x · Flask · Gunicorn           │
├──────────────┤  ├──────────────────────────────────────────┤
│  ML ENGINE   │  │  Scikit-Learn · XGBoost · NumPy · Joblib │
├──────────────┤  ├──────────────────────────────────────────┤
│  HARDWARE    │  │  Arduino UNO (C++) · Python Data Aug.    │
├──────────────┤  ├──────────────────────────────────────────┤
│  DEPLOYMENT  │  │  Render Cloud Platform                   │
└──────────────┘  └──────────────────────────────────────────┘
```

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=arduino&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white)

---

## ![start](https://img.shields.io/badge/-Getting_Started-1a1a2e?style=flat-square&logo=dependabot&logoColor=white) Getting Started

### Prerequisites

![Python](https://img.shields.io/badge/Python-3.x_required-3776AB?style=flat-square&logo=python&logoColor=white)
![pip](https://img.shields.io/badge/pip-package_manager-3775A9?style=flat-square&logo=pypi&logoColor=white)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/nova-telemetry.git
cd nova-telemetry
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Launch the application**
```bash
python app.py
```

The app will be available at **`http://127.0.0.1:5000`**

---

## ![api](https://img.shields.io/badge/-API_Reference-1a1a2e?style=flat-square&logo=postman&logoColor=white) API Reference

### `POST /predict`

Accepts a JSON payload of satellite telemetry readings and returns fault prediction results from all 7 models.

#### Input Telemetry Fields

| Field | Type | Description |
|---|---|---|
| `temperature_c` | `float` | Temperature (°C) |
| `humidity_percent` | `float` | Relative humidity (%) |
| `pressure_pa` | `float` | Atmospheric pressure (Pa) |
| `gas_ppm` | `float` | Gas concentration (ppm) |
| `radiation_usv_h` | `float` | Radiation level (µSv/h) |
| `battery_voltage_v` | `float` | Battery voltage (V) |
| `solar_current_ma` | `float` | Solar panel current (mA) |
| `cpu_temp_c` | `float` | CPU temperature (°C) |
| `vibration_mms` | `float` | Vibration (mm/s) |
| `satellite_mode` | `int` | Current operating mode |
| `region` | `int` | Operating region code |
| `battery_voltage_next` | `float` | Predicted next battery voltage (V) |
| `altitude_m` | `float` | Altitude (m) |
| `magnetic_field_uT` | `float` | Magnetic field strength (µT) |
| `solar_panel_temp_c` | `float` | Solar panel temperature (°C) |
| `gyro_stability_index` | `float` | Gyroscope stability index |

#### Example Request

```bash
curl -X POST https://n-o-v-a-system.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

#### Example Response

```json
{
  "success": true,
  "overall_status": "NORMAL",
  "confidence": 100.0,
  "fault_count": 0,
  "total_models": 7,
  "predictions": {
    "Decision Tree":       { "prediction": 0, "status": "NORMAL" },
    "KNN":                 { "prediction": 0, "status": "NORMAL" },
    "Logistic Regression": { "prediction": 0, "status": "NORMAL" },
    "MLP":                 { "prediction": 0, "status": "NORMAL" },
    "Random Forest":       { "prediction": 0, "status": "NORMAL" },
    "SVC":                 { "prediction": 0, "status": "NORMAL" },
    "XGBoost":             { "prediction": 0, "status": "NORMAL" }
  }
}
```

---

## ![routes](https://img.shields.io/badge/-Web_Routes-1a1a2e?style=flat-square&logo=googlechrome&logoColor=white) Web Routes

| Route | Method | Description |
|---|---|---|
| `/` | `GET` | Landing page |
| `/dashboard` | `GET` | Telemetry monitoring dashboard |
| `/login` | `GET` | User authentication |
| `/predict` | `POST` | ML prediction endpoint |

---

## ![structure](https://img.shields.io/badge/-Project_Structure-1a1a2e?style=flat-square&logo=files&logoColor=white) Project Structure

```
nova-telemetry/
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── models/                 # Pre-trained ML model files (.pkl / .joblib)
├── static/
│   ├── css/                # Custom stylesheets & animations
│   └── js/                 # Frontend scripts
└── templates/
    ├── index.html          # Landing page
    ├── dashboard.html      # Telemetry dashboard
    └── login.html          # Login portal
```

---

<div align="center">

Built for real-time satellite health monitoring

[![Status](https://img.shields.io/badge/status-live-brightgreen?style=flat-square&logo=googlechrome&logoColor=white)](https://n-o-v-a-system.onrender.com/)
[![Made with Python](https://img.shields.io/badge/Made_with-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Powered by Flask](https://img.shields.io/badge/Powered_by-Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)

</div>