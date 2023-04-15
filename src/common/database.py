import pymongo


class Database(object):

    #URI = "mongodb://127.0.0.1:27017"
    URI = "mongodb+srv://athira_p:cc-proj@cc-project.jz0cu2o.mongodb.net/?retryWrites=true&w=majority"
    DATABASE = None
    COLLECTION = None
    

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        #Database.DATABASE = client['cc-project']
        Database.DATABASE = client.database_name
        Database.COLLECTION = client.collection_name

    @staticmethod
    def insert(collection, data):
        #Database.DATABASE[collection].insert(data)
        Database.COLLECTION.insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

