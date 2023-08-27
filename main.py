"""
Atlas: https://cloud.mongodb.com/v2/64eaa9949731c104c803cba9#/overview

Replace <password> with the password for the philbed user. Ensure any option params are URL encoded:
https://www.mongodb.com/docs/atlas/troubleshoot-connection/#special-characters-in-connection-string-password
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os

load_dotenv()

atlas_link = os.getenv("ATLAS_LINK")

uri = atlas_link

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)