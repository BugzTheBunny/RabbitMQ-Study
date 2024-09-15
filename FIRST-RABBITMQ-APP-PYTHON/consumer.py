import pika

def on_message_recieved(ch,method,properties,body):
    print(f"Got a message: {body}")

host = "localhost"

connection_parameters = pika.ConnectionParameters(host)
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

channel.basic_consume(queue="letterbox",auto_ack=True,on_message_callback=on_message_recieved)

print("Started consuming")

channel.start_consuming()