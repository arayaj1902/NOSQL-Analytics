import redis

# Conéctate al servidor de Redis
redis_host = '127.0.0.1'  # Reemplaza con el host de tu servidor de Redis
redis_port = 6379         # Reemplaza con el puerto de tu servidor de Redis
redis_cliente = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

# ID de la cuenta de Instagram
id_cuenta_instagram = 'Imperial'

# Crea una lista vacía para almacenar los datos extraídos
datos_extraidos = []

# Itera a través de todas las claves de las publicaciones y extrae los datos
for id_publicacion in range(4000):
    clave = f'{id_cuenta_instagram}:post_{id_publicacion}'
    metrics_publicacion = redis_cliente.hgetall(clave)
    
    if metrics_publicacion:
        datos_extraidos.append(metrics_publicacion)

# Ahora, 'datos_extraidos' contiene una lista de diccionarios, donde cada diccionario representa las métricas de una publicación.

# Ejemplo: Calcula el promedio de "likes" para todas las publicaciones
total_likes = 0
for metrics_publicacion in datos_extraidos:
    total_likes += int(metrics_publicacion[b'likes'])

promedio_likes = total_likes / len(datos_extraidos)
print(f'Promedio de Likes para todas las publicaciones: {promedio_likes:.2f}')


