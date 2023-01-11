import os
import pymongo
import certifi
from finance_complaint.constants.constants import env_var
ca = certifi.where()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url, tlsCAFile=ca)
