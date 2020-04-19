import pytest
from caches.base import AbstractCache
from core.settings import cache


@pytest.mark.parametrize('method', ['get', 'set'])
def test_abstract_cache_methods(method):
    assert hasattr(AbstractCache, method)


def test_inheritance():
    assert isinstance(cache, AbstractCache)
