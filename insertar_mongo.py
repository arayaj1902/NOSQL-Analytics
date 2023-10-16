import random
import pymongo
from datetime import datetime, timedelta

# Conectarse a la base de datos MongoDB
mongo_client = pymongo.MongoClient("mongodb+srv://luisfer:HHiLiGZhCk53ea6q@cluster0.b00maxa.mongodb.net/")  # Reemplaza la URL con la configuración de tu servidor MongoDB
database_name = "instagram_data"
collection_name = "post_metrics"
db = mongo_client[database_name]
collection = db[collection_name]

# ID de la cuenta de Instagram
account_id = "Imperial"

# Generar 4000 métricas de publicación simuladas e insertarlas en MongoDB
for i in range(4000):
    post_id = i + 1
    likes = random.randint(1, 100000)
    comments = random.randint(1, 5000)
    shares = random.randint(1, 20000)

    # Generar fecha aleatoria
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 1, 1)
    random_date = start_date + (end_date - start_date) * random.random()

    post_metrics = {
        "account_id": account_id,
        "post_id": post_id,
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "date": random_date
    }

    # Insertar las métricas de la publicación en la colección de MongoDB
    collection.insert_one(post_metrics)

print("Métricas de publicación han sido insertadas en MongoDB.")
