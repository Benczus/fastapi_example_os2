from typing import Dict
from pprint import pprint
import pymongo
from pymongo import MongoClient

client=MongoClient('localhost', 27017)
db = client.valami
coll=db.valami_collection

def db_insert(doc:Dict):
    coll.insert_one(doc)
    return

def db_read(critera:Dict):
    return coll.find_one(critera)


def db_count(field_name:str):
    return coll.count_documents({field_name: {"$exists": True}})

def db_find_last_entry(field_name:str):
    return coll.find({field_name: {"$exists": True}}).sort("_id", -1).limit(1)