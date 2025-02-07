import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model and feature names
model = joblib.load("C:/Users/PATH TECH/OneDrive/Desktop/COURSES/Data science/Hands_on_ml/rf_model.joblib")
feature_names = joblib.load("C:/Users/PATH TECH/OneDrive/Desktop/COURSES/Data science/Hands_on_ml/feature_names.joblib")

@app.route("/")
def home():
    return "Worker Attendance Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Convert JSON into DataFrame
        df = pd.DataFrame([data])

        # Reorder columns to match training set and fill missing values
        df = df.reindex(columns=feature_names, fill_value=0)  # Fill missing features with 0

        # Make a prediction
        prediction = model.predict(df)[0]

        return jsonify({"prediction": int(prediction), "status": "Absent" if prediction == 1 else "Present"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
