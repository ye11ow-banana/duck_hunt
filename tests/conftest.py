import pytest

from entities import Bird


@pytest.fixture
def bird() -> Bird:
    return Bird(level='medium')
