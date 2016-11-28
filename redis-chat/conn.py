import redis

config = {
    'host': '192.168.31.163',
    'port': 6379,
    'db': 0,
}

client = redis.StrictRedis(**config)