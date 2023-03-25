import pygame
import pytest

from consts import LEVELS
from utils import get_level, get_music


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


@pytest.mark.tyl
class TestGetMusic:
    pygame.init()

    @pytest.mark.parametrize('level', LEVELS)
    def test_all_valid_levels(self, level):
        assert isinstance(get_music(level), pygame.mixer.Sound)

    def test_invalid_level(self):
        with pytest.raises(FileNotFoundError):
            assert get_music('not valid level')
