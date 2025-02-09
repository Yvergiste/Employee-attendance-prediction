# Employee Attendance Prediction

## Overview
This project focuses on predicting employee attendance using machine learning models. The system takes in relevant employee data and predicts whether a worker will be present or absent based on historical patterns. The primary goal is to enhance workforce planning and management by providing data-driven insights.

## Data Source
The dataset used in this project was obtained from the **University of California, Irvine (UCI) Machine Learning Repository**, which is an open-source repository for machine learning datasets. The dataset contains various features related to employee work habits, schedules, and historical attendance records.

## Table of Contents
- Installation
- Project Structure
- Data Processing
- Model Development
- Deployment 
- Usage

## Installation
The installation process for this project involves setting up the necessary environment, dependencies, and frameworks to ensure smooth execution. Below are the general steps followed during the installation:

1. **Setting up a virtual environment**: A virtual environment was created to manage dependencies and avoid conflicts with system-wide packages.
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

2. **Installing dependencies**: The required libraries and frameworks were installed using the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

3. **Downloading necessary machine learning tools**: This includes installing essential packages such as `scikit-learn`, `pandas`, `flask`, and `joblib` for model training and deployment.

4. **Running the Flask API**: To deploy the model as an API, Flask was used, and the server was initiated using:
   ```bash
   python app.py
   ```

## Project Structure
```
employee-attendance-prediction/
├── data/                # Dataset (downloaded from UCI ML Repository)
├── notebooks/           # Jupyter notebooks for data exploration & model training
├── src/                 # Source files for data processing and model training
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
├── app.py               # Flask API for making predictions
├── Front_end.html        # Front-end interface for uploading JSON files
├── model_development.ipynb # Jupyter notebook for model development
├── requirements.txt     # Required dependencies
└── README.md            # Project documentation
```

## Data Processing
The dataset underwent the following preprocessing steps:
- Handling missing values by replacing or dropping them appropriately.
- Encoding categorical variables to numerical representations.
- Standardizing numerical features using **StandardScaler**.
- Splitting the dataset into training and testing sets.

## Model Development
Several machine learning models were tested, including:
- Random Forest (Final Model)
- Decision Tree
- Gradient Boosting

The best-performing model, **Random Forest**, was selected based on evaluation metrics such as accuracy, precision, recall, and F1-score. The trained model was saved as `rf_model.joblib`.

## Deployment
The trained model was deployed using a **Flask API**, which allows users to send employee data via a POST request and receive predictions.

### Flask API Endpoints:
- **`/`** - Home route to check if the API is running.
- **`/predict`** - Endpoint for making predictions (expects JSON input).

### Front-End Interface:
A simple **HTML + JavaScript** interface (`Front_end.html`) allows users to upload a JSON file containing employee data, which is sent to the Flask API for predictions.

## Usage
### 1. Making Predictions via API
After running the Flask API, send a request with employee data:
```bash
curl -X POST "http://127.0.0.1:5000/predict" \
     -H "Content-Type: application/json" \
     -d '{"feature1": value1, "feature2": value2, ...}'
```
Example Response:
```json
{
  "prediction": 1,
  "status": "Absent"
}
```

### 2. Using the Web Interface
- Open `[Front_end.html](file:///C:/Users/PATH%20TECH/OneDrive/Desktop/COURSES/Data%20science/Employees_attendance_prediction/Front_end.html)` in a browser.
- Upload a JSON file with employee data.
- Click "Enter" to get predictions displayed on the page.

## Conclusion
This project provides an efficient way to predict employee attendance using machine learning. The implementation includes:
- Data preprocessing techniques to ensure high-quality input.
- Model training and evaluation to find the best-performing algorithm.
- Deployment via a Flask API for seamless integration.
- A simple front-end for user interaction.



