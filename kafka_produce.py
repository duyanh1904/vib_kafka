from kafka import KafkaProducer
from json import dumps
from src.helper.pagination import Pagination

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


for page in range(1, Pagination.page + 1):
    producer.send('vib', page)

