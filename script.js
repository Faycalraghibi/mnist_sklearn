async function predictDigit() {
    const file = document.getElementById('ImgInput').files[0];
    if (!file) {
        alert('Please select an image file');
        return;
    }
    const fileImg = input.files[0]
    const formData = new FormData();
    formData.append('file', fileImg);

    try{
        const response = await fetch('http://localhost:8000/predict', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        document.getElementById('result').textContent = `Prediction: ${data.prediction}`;
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while predicting the digit');
    }
}