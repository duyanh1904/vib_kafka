from flask import Flask
from src.model.base_model import *
from kafka_produce import *
from kafka_consumer import *

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)