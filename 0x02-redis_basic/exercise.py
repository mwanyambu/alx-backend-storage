#!/usr/bin/env python3
""" writting strings to redis """
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional
import sys


def count_calls(method: Callable) -> Callable:
        """ returns a callable """
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """ get name of method """
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper



def call_history(method: Callable) -> Callable:
    """ add input params in one list """
    key = method.__qualname__
    inp = "".join([key, ":inputs"])
    outp = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper """
        self._redis.rpush(inp, str(args))
        resp = method(self, *args, **kwargs)
        self._redis.rpush(outp, str(resp))
        return resp
    return wrapper

class Cache:
    def __init__(self):
        """instance of redis client stored here """
        self._redis = redis.Redis()
        self._redis.flushdb()
    @count_calls
    @call_history

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key using uuid """
        randkey = str(uuid.uuid4())
        self._redis.set(randkey, data)

        return randkey

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        """ convert data back to desired format """
        data = self._redis.get(key)
        if data is not None:
            if fn is not None:
                return fn(data)
            return data
        return None

    def get_str(self, bytes) -> str:
        """ automaticaly parameterize Cache.get with correct function """
        return self.decode('utf-8')

    def get_int(self, bytes) -> int:
        """ prioritize Cache with correct conversion function """
        return self.get(key, fn=int)
