import pymongo
from novel.constant.database import DATABASE_NAME
from novel.constant.env_variable import MONGODB_URL_KEY
import certifi
import os
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                print(mongo_db_url)
                
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")


                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

                MongoDBClient.client = pymongo.MongoClient(mongo_db_url)

            self.client = MongoDBClient.client

            self.database = self.client[database_name]

            self.database_name = database_name

        except Exception as e:
            raise e

