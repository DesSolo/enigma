import datetime
from base64 import b64encode, b64decode
from redis import StrictRedis
from caches.base import AbstractCache
from core.settings import REDIS


class CacheRedis(AbstractCache):
    redis = StrictRedis(**REDIS)

    def set(self, key, value, expire_at):
        self.redis.set(key, b64encode(value.encode('utf-8')))
        self.redis.expireat(key, datetime.datetime.now() + datetime.timedelta(int(expire_at)))

    def get(self, key):
        message = self.redis.get(key)
        self.redis.delete(key)
        if not message:
            return None
        return b64decode(message).decode('utf-8')

