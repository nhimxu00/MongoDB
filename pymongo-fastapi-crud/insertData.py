from distutils.command.config import config
from dotenv import dotenv_values
from pymongo import MongoClient
config = dotenv_values(".env")

mongodb_client = MongoClient(config['ATLAS_URI'])

# raw data
database = mongodb_client[config['DB_NAME']]

# database['news'].insert_one({
#     "text" : "hello",
#     "label" : 1,
#     "link" : "http://"
# })

# Blob Store

# Cloud Storage. link.

new_data = [
    {
        "text" : "chào bạn ",
        "label" : 2,
        "link" :"http://"
    },
    {
        "text" : "Chào buổi sáng ",
        "label" : 2,
        "link" :"http://"
    }
]


database['news'].insert_many(new_data)
