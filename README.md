# POC-kafka

## Simple POC that sends a JSON file to a topic called 'test' or 'test-small' and then consumes it back
## Uses Python confluent libraries for Producer, Consumer

Build the datagen container

Build the python-with-confluent container

Run stack in Portainer using docker-compose file

View logs in Portainer for python-readtopic container

Select the python-sendfile container and Restart it

Each time you restart the sendfile container it will display the message in the readtopic container log
