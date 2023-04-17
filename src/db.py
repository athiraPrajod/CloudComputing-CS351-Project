from flask import Flask
import pymongo
from app import app
CONNECTION_STRING = "mongodb+srv://athira_p:cc-proj@cc-project.jz0cu2o.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')