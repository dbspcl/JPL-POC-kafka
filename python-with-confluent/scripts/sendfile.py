import sys
from confluent_kafka import Producer
import json
import random

topic = sys.argv[1]
jsonfile = sys.argv[2]
print("Send to topic: ", topic, " the JSON message from file: ", jsonfile)

conf = {'bootstrap.servers': 'broker:9092', 'client.id': topic, 'default.topic.config': {'acks': 'all'}, 'group.id': 'mygroup'}
producer = Producer(conf)

with open(jsonfile,'r') as file:
	for line in file:
		randkey = str(random.randint(1,10000000))
		producer.produce(topic,key=randkey,value=line)
		print ('Key: ', randkey, ', Msg: ', line)

producer.flush()