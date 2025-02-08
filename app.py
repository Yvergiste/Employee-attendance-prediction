import joblib
import pandas as pd
import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Optional: If integrating with a frontend

app = Flask(__name__)
CORS(app)  # Enable CORS if needed

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
        data = request.get_json()
        df = pd.DataFrame([data])

        # Ensure correct column order and fill missing features
        df = df.reindex(columns=feature_names, fill_value=0)

        # Apply Scaling (important!)
        df_scaled = scaler.transform(df)

        # Make a prediction
        prediction = model.predict(df_scaled)[0]

        return jsonify({"prediction": int(prediction), "status": "Absent" if prediction == 1 else "Present"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)  # Host on all network interfaces
