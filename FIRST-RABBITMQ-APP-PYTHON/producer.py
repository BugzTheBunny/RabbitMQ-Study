import pika

host = "localhost"

connection_parameters = pika.ConnectionParameters(host)
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

message = "Hello this is my first message"

channel.basic_publish(exchange="",routing_key="letterbox",body=message)

print(f"Sent a message : {message}")

connection.close()