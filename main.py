from flask import Flask
from kafka_produce import *
from src.model.pagination_model import paginate_page
from kafka_consumer import *

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)