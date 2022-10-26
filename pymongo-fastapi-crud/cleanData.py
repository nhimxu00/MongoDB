from distutils.command.config import config
from typing import Collection
from dotenv import dotenv_values
from pymongo import MongoClient
from cleanText import clean_text


config = dotenv_values(".env")

mongodb_client = MongoClient(config['ATLAS_URI'])

# raw data
database = mongodb_client[config['DB_NAME']]

newsList = database['news'].find()

clean_database = mongodb_client['cleaned_data']



for item in newsList:
    cleaned_text = clean_text(item['text'])
    
    clean_database['news'].insert_one({
        "text" : cleaned_text,
        'raw_id' : item['_id']
    })
    

db  =  'training'
Collection = 'news-training'

{
    "_id": "1111",
    "timeStart": "21:31",
    "timeEnd": "23:00",
    "train_ids": [
        "4448488488993939",
        "7437438493294392"
    ],
    "test_ids" : [
        "1372743724374733",
        "3743747375737535"
    ],
    "acc": "",
    "loss": "",
    "history": [
        
    ]
}
