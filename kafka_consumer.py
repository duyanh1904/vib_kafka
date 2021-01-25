from kafka import KafkaConsumer
from json import loads
from src.model.base_model import CustProfile


class ConsumerKafka:
    consumer = KafkaConsumer(
        'vib',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        for record_per_page in CustProfile.select().order_by(CustProfile.cust_id).paginate(message.value, 500):
            print(message.value)
            print(record_per_page.cust_name)


