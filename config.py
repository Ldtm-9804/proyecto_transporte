import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
    MYSQL_DB = os.getenv("MYSQL_DB", "transporte_db")


# ¿Qué hace este archivo? Este módulo:
#Carga las variables desde tu archivo .env.
#Define la clase Config con los datos necesarios para conectar a MySQL.
#Se integra perfectamente con tu app.py mediante: app.config.from_object(Config