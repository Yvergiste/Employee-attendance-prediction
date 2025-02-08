async function handleFileUpload() {
    const fileInput = document.getElementById("jsonFileInput");
    const resultsDiv = document.getElementById("predictionResults");

    if (fileInput.files.length === 0) {
        alert("Please upload a JSON file first.");
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = async function(event) {
        try {
            const jsonData = JSON.parse(event.target.result); // Read JSON data
            
            // Make POST request to Flask API
            const response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(jsonData)
            });

            const result = await response.json();
            
            // Display Prediction Result
            if (response.ok) {
                resultsDiv.innerHTML = `<p><strong>Prediction:</strong> ${result.status} (Value: ${result.prediction})</p>`;
            } else {
                resultsDiv.innerHTML = `<p style="color: red;">Error: ${result.error}</p>`;
            }
        } catch (error) {
            resultsDiv.innerHTML = `<p style="color: red;">Invalid JSON file.</p>`;
        }
    };

    reader.readAsText(file);
}
