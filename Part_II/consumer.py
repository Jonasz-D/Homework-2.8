import pika
import json
from mongoengine import connect
from models import Contact

def connect_with_db():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', 
                                port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    host = f'mongodb+srv://Jd:s7SyzV9Wkkj-Yex@cluster0.jybrqzs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    connect(host=host)
    return channel

def channel_consuming(channel, callback):
    channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


def send_email_stub(contact_id):
    print(f'Sending email to contact with id {contact_id}')

def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    contact_id = message['contact_id']
    contact = Contact.objects.get(id=contact_id)
    send_email_stub(contact_id)
    contact.sending_status = True
    contact.save()


if __name__ == '__main__':
    channel = connect_with_db()
    channel_consuming(channel, callback)

