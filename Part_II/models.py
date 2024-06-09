from mongoengine import Document
from mongoengine.fields import StringField, EmailField, BooleanField

class Contact(Document):
    fullname = StringField()
    address_email = EmailField()
    sending_status = BooleanField(default=False)
