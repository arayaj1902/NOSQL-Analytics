# Instalación de librerías
import random
import redis

# Conectarse al servidor
redis_host = '127.0.0.1'  # Remplazar con su host de servidor de Redis
redis_port = 6379         # Remplazar con su puerto de servidor de Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

# Instagram account ID
account_id = 'imperial'

# Generar 4000 datos aleatorios sobre posibles metricas para cada posteo
for i in range(4000):
    post_id = f'post_{i}'
    likes = random.randint(1, 1000)
    comments = random.randint(1, 500)
    shares = random.randint(1, 200)
    
    # Crear un diccionario con las metricas generadas
    post_metrics = {
        'likes': likes,
        'comments': comments,
        'shares': shares
    }
    
    # Guardaar como Redis hash
    redis_client.hmset(f'{account_id}:{post_id}', post_metrics)

print("Metrics have been exported to Redis.")
