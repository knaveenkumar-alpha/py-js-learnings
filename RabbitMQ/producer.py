import pika

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='hello')

# Send a message to the queue
message = "Hello, RabbitMQ!"
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" [x] Sent '{message}'")

# Close the connection
connection.close()
