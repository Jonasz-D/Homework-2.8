import pika, json
from faker import Faker
from models import Contact
from mongoengine import connect


NUM_OF_CONTACTS = 40

def generate_fake_data(number_of_contacts):
    host = f'mongodb+srv://Jd:s7SyzV9Wkkj-Yex@cluster0.jybrqzs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    connect(host=host)
    fake_data = Faker('pl_PL')
    fake_contacts = []
    Contact.drop_collection()

    for _ in range(number_of_contacts):
        contact = Contact()
        contact.fullname = fake_data.name()
        contact.address_email = fake_data.email()
        contact.save()
        fake_contacts.append(contact)
    return fake_contacts


def send_data(data:list):
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange='task_mock', exchange_type='direct')
    channel.queue_declare(queue='task_queue', durable=True)
    channel.queue_bind(exchange='task_mock', queue='task_queue')

    for contact in data:
        message = {
            'contact_id': str(contact.id)
        }
        channel.basic_publish(exchange='task_mock', 
                              routing_key='task_queue', 
                              body=json.dumps(message).encode(),
                              properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
                              )
        print(f'Sent {message}')
    connection.close()


if __name__ == '__main__':
    data_of_contacts = generate_fake_data(NUM_OF_CONTACTS)
    send_data(data_of_contacts)
