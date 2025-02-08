import joblib
import pandas as pd
import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable CORS for cross-origin requests

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})  # Allow requests from any origin

# Define base directory to avoid hardcoded paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained model, scaler, and feature names
model = joblib.load(os.path.join(BASE_DIR, "rf_model.joblib"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.joblib"))  # Load scaler
feature_names = joblib.load(os.path.join(BASE_DIR, "feature_names.joblib"))

@app.route("/")
def home():
    return "Worker Attendance Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Ensure request is JSON
        if not request.is_json:
            return jsonify({"error": "Request must be JSON format"}), 400

        data = request.get_json()
        
        # If data is a list (multiple rows), convert properly
        if isinstance(data, list):
            df = pd.DataFrame(data)
        elif isinstance(data, dict):
            df = pd.DataFrame([data])
        else:
            return jsonify({"error": "Invalid input format. Expecting JSON dictionary or list."}), 400

        # Ensure correct column order and fill missing features
        df = df.reindex(columns=feature_names, fill_value=0)

        # Apply Scaling
        df_scaled = scaler.transform(df)

        # Make a prediction
        prediction = model.predict(df_scaled)

        # Convert predictions into readable format
        results = [{"prediction": int(pred), "status": "Absent" if pred == 1 else "Present"} for pred in prediction]

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)  # Secure production settings
