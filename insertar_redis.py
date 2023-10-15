# Install necessary packages if you haven't already
import random
from datetime import datetime, timedelta
import json
import redis
from faker import Faker

# Connect to the Redis server
redis_host = '127.0.0.1'  # Replace with your Redis server's host
redis_port = 6379         # Replace with your Redis server's port
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

# Instagram account ID
account_id = 'imperial'

# Generate 4000 random post metrics and store them in a Redis hash
for i in range(4000):
    post_id = f'post_{i}'
    likes = random.randint(1, 1000)
    comments = random.randint(1, 500)
    shares = random.randint(1, 200)
    
    # Create a dictionary with the post metrics
    post_metrics = {
        'likes': likes,
        'comments': comments,
        'shares': shares
    }
    
    # Store the metrics in the Redis hash
    redis_client.hmset(f'{account_id}:{post_id}', post_metrics)

print("Metrics have been exported to Redis.")
