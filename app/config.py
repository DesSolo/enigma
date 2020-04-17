import os

PROTOCOL = os.getenv('PROTOCOL', 'http')

LISTEN = {
    'host': '0.0.0.0',
    'port': os.getenv('PORT', 8000)
}

LOG_FORMAT = '%a %t "%r" %s %b "%{Referer}i" "%{User-Agent}i"'

DAYS_RANGE = ['1', '2', '3', '4']

REDIS = {
    'host': os.getenv('REDIS_HOST', '127.0.0.1'),
    'port': os.getenv('REDIS_PORT', 6379)
}

CACHE = 'caches.redis.CacheRedis'

DENY_USER_AGENTS = [
    r'curl',
    # r'Mozilla/\d[.]\d'
]

TOKEN_BYTES = os.getenv('TOKEN_BYTES', 20)
