from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['my_database']
collection = db['my_collection']

document = {
    'name': 'Test Document',
    'data': 'Some data',
    'createdAt': datetime.now()
}
collection.insert_one(document)

collection.create_index('createdAt', expireAfterSeconds=86400)  # 86400 секунд = 24 часа
