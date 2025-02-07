async function predictAttendance() {
    const formData = new FormData(document.getElementById("predictionForm"));
    let data = {};

    formData.forEach((value, key) => {
        data[key] = isNaN(value) ? value : parseFloat(value);
    });

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText = "Prediction: " + result.status;
}
