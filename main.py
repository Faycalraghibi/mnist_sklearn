import io 
import pickle
import numpy as np
import PIL.Image
import PIL.ImageOps
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

with open('mnist_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post('/predict')
async def predict_digit(file: UploadFile = File(...)):
    image = PIL.Image.open(io.BytesIO(await file.read())).convert('L')
    image = PIL.ImageOps.invert(image)  
    image = image.resize((28, 28), PIL.Image.ANTIALIAS)
    img_array = np.array(image).reshape(1, -1) / 255
    prediction = model.predict(img_array)
    return {'prediction': int(prediction[0])}

# Create 'static' directory if it doesn't exist
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('index.html')
