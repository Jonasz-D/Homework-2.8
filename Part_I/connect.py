from mongoengine import connect
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

mongodb_password = config.get('DB', 'password')
# host = f'mongodb+srv://Jd:{mongodb_password}.jybrqzs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
host = f'mongodb+srv://Jd:s7SyzV9Wkkj-Yex@cluster0.jybrqzs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

connect(host=host)


