import sys
from confluent_kafka import Consumer
import json
from elasticsearch import Elasticsearch
import random

es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])

topic = sys.argv[1]
print ("Consuming on topic", topic)
print

conf = {'bootstrap.servers': 'broker:9092', 'client.id': 'test', 'default.topic.config': {'acks': 'all'}, 'group.id': 'mygroup'}

consumer = Consumer(conf)
consumer.subscribe([topic])
while True:
	msg = consumer.poll(1.0)
	if msg is None:
		continue
	if msg.error():
		print("Consumer error: {}".format(msg.error()))
		continue
	print('Message key: {}'.format(msg.key().decode('utf-8')))
	print('Message value: {}'.format(msg.value().decode('utf-8')))
	es.index(index=topic, doc_type='jsonfile', id=random.randint(1,10000000), body=format(msg.value().decode('utf-8')))

consumer.close()