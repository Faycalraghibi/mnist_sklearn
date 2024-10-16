# MNIST Digit Classifier

This project is a web application that uses a machine learning model to classify handwritten digits from the MNIST dataset. Users can upload an image of a handwritten digit, and the application will predict which digit it is.

## Features

- FastAPI backend for serving predictions
- Simple HTML/CSS/JavaScript frontend for user interaction
- Sklearn-based machine learning model for digit classification
- Image preprocessing to match MNIST dataset format

## Project Structure

- `main.py`: FastAPI server that handles image uploads and serves predictions
- `index.html`: Frontend HTML file
- `styl.css`: CSS styles for the frontend
- `script.js`: JavaScript for handling user interactions and API calls
- `mnist_model.pkl`: Pickled sklearn model for digit classification

## Setup and Installation

1. Clone this repository
2. Install the required Python packages:
   ```
   pip install fastapi uvicorn pillow numpy scikit-learn
   ```
3. Ensure you have the `mnist_model.pkl` file in the project root directory

## Running the Application

1. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```
2. Open a web browser and navigate to `http://localhost:8000`

## Usage

1. Click the "Choose File" button to upload an image of a handwritten digit
2. Click the "Predict" button
3. The predicted digit will be displayed on the page

## Technologies Used

- Backend: Python, FastAPI
- Frontend: HTML, CSS, JavaScript
- Machine Learning: scikit-learn
- Image Processing: Pillow (PIL)

## Future Improvements

- Add error handling for invalid image uploads
- Implement a drawing canvas for users to draw digits directly in the browser
- Expand the model to classify other types of images or handwritten characters

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

