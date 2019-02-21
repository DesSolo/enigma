PROTOCOL = 'http'

LISTEN = {
    'port': 8888,
    'address': ""
}

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
