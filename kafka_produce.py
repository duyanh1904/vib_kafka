from kafka import KafkaProducer
from json import dumps
from src.model.pagination_model import paginate_page
from kafka.admin import KafkaAdminClient, NewTopic

# admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

# topic_list = []
# topic_list.append(NewTopic(name="vib_topic", num_partitions=5, replication_factor=1))
# admin_client.create_topics(new_topics=topic_list, validate_only=False)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

count = 0
for page in range(1, paginate_page.page_all):
    producer.send('vib_topic', page)
    count += 1
    if count == paginate_page.page_all:
        print('finish send_msg')

class Producer:
    @staticmethod
    def producer_send_msg_records(records):
        producer.send('vib_record', records)
