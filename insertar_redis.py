
import random
import redis
from datetime import datetime, timedelta

# Conectarse al servidor de Redis
redis_host = '127.0.0.1'  # Reemplaza con tu host de servidor de Redis
redis_port = 6379         # Reemplaza con tu puerto de servidor de Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

# ID de la cuenta de Instagram
account_id = 'imperial'

# Generar 4000 datos aleatorios sobre métricas para cada publicación
for i in range(4000):
    post_id = f'post_{i}'
    likes = random.randint(1, 1000)  
    comments = random.randint(1, 500)
    shares = random.randint(1, 200)

    # Generar fecha aleatoria
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 1, 1)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

    # Crear un diccionario con las métricas generadas, incluyendo la fecha aleatoria
    post_metrics = {
        'likes': likes,
        'comments': comments,
        'shares': shares,
        'date': random_date.isoformat()  # Convierte la fecha en formato ISO para guardar en Redis
    }

    # Guardar en Redis como un hash
    redis_client.hmset(f'{account_id}:{post_id}', post_metrics)

print("Métricas han sido exportadas a Redis.")


