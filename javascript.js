<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Worker Attendance Prediction</title>
    <script defer src="script.js"></script>
</head>
<body>
    <h2>Worker Attendance Prediction</h2>
    
    <!-- New section for JSON file upload -->
    <h3>Predict employees' attendance</h3>
    <input type="file" id="jsonFileInput" accept="application/json">
    <button type="button" onclick="handleFileUpload()">Upload</button>
    
    <!-- Placeholder for prediction results -->
    <h3>Prediction Results:</h3>
    <div id="predictionResults"></div>
</body>
</html>
