from kafka import KafkaConsumer
from json import loads
from src.model.base_model import CustProfile
from kafka_produce import Producer


class ConsumerKafka:
    consumer = KafkaConsumer('vib_topic', bootstrap_servers=['localhost:9092'],
                             group_id='vib-kafka',
                             value_deserializer=lambda x: loads(x.decode('utf-8')))

    consumer1 = KafkaConsumer('vib_record', group_id='vib-group',
                              bootstrap_servers=['localhost:9092'],
                              value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        for record_per_page in CustProfile.select().order_by(CustProfile.cust_id).paginate(message.value, 500):
            Producer.producer_send_msg_records(record_per_page.cust_name)
            print(message.value, message.partition, message.offset, message.topic, message.key)
            print(record_per_page.cust_name, record_per_page.cust_card)








