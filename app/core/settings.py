import importlib
from re import compile
from config import *

DENY_USER_AGENTS = [compile(i) for i in DENY_USER_AGENTS]

_module_name = '.'.join(CACHE.split('.')[:-1])
_class_name = CACHE.split('.')[-1]
_module = importlib.import_module(_module_name)
cache = getattr(_module, _class_name)()
