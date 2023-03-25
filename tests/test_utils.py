import pytest

from consts import LEVELS
from utils import get_level


@pytest.mark.yakubets
class TestGetLevel:

    @pytest.mark.parametrize('level', LEVELS)
    def test_all_valid_levels(self, monkeypatch, level):
        monkeypatch.setattr('sys.argv', ['main', '--level', level])
        assert get_level() == level

    def test_invalid_level(self, monkeypatch):
        monkeypatch.setattr('sys.argv', ['main', '--level', 'not valid level'])
        with pytest.raises(SystemExit):
            get_level()
