from flask import Flask
from main import run_model

app = Flask(__name__)

@app.route("/")
def home():
    return run_model()

@app.route("/predict")
def predict():
    return run_model()
