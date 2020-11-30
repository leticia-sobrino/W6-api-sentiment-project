"""
En este archivo es donde realizamos la conexion con mongo
"""

import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DBURL = os.getenv("URL")

#VAMOS A CONECTAR CON LA BASE DE DATOS DE MONGO LOCAL

### este if es para que me salte este mensaje si no se me ha conectado bien a la base de datos
if not (DBURL):
    raise ValueError("Tienes que especificar una URL")

client = MongoClient(DBURL)
db = client.get_database()
collection = db["tweets"]

