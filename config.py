PROTOCOL = 'http'

LISTEN = {
    'port': 8888,
    'address': ""
}

DAYS_RANGE = ['1', '2', '3', '4']

REDIS = {
    'host': '192.168.122.16',
    'port': 6379
}

CACHE = 'caches.redis.CacheRedis'

DENY_USER_AGENTS = [
    r'curl',
    # r'Mozilla/\d[.]\d'
]

TOKEN_BYTES = 20
