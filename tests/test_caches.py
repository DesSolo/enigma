import pytest
from caches.base import AbstractCache


@pytest.mark.parametrize('method', ['get', 'set'])
def test_abstract_cache_methods(method):
    assert hasattr(AbstractCache, method)
