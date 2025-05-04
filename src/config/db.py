from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("MONGO_DB")

if not mongo_uri:
    raise ValueError("URI do banco de dados (MONGO_DB) não definido no .env")

client = MongoClient(mongo_uri)

if not db_name:
    raise ValueError("Nome do banco de dados (MONGO_DB) não definido no .env")

db = client[db_name]

colecao = db['paises-covid']
