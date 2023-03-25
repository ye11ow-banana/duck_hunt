import pytest


class TestBird:

    @pytest.mark.yakubets
    def test_move_alive(self, monkeypatch, bird):
        _previous_y = bird._previous_y
        current_position_x = bird.current_position.x
        monkeypatch.setattr('entities.Bird._math_function', lambda this, x: x)
        bird.move()
        assert bird._previous_y == _previous_y
        assert bird.current_position.x == current_position_x + 1
        assert bird.current_position.y == current_position_x + 1

    @pytest.mark.yakubets
    def test_move_killed(self, monkeypatch, bird):
        _previous_y = bird._previous_y
        current_position_x = bird.current_position.x
        bird.is_killed = True
        monkeypatch.setattr('entities.Bird._down_function', '_down_function')
        monkeypatch.setattr('entities.Bird._math_function', lambda this, x: x)
        bird.move()
        assert bird._previous_y == _previous_y
        assert bird.current_position.x == current_position_x + 1
        assert bird.current_position.y == current_position_x + 1
        assert bird._math_subfunction == '_down_function'

    @pytest.mark.yakubets
    def test_get_current_image_bottom(self, bird):
        bottom_image = bird._images.bottom[0]
        bird.is_killed = True
        assert bird.get_current_image() == bottom_image

    @pytest.mark.yakubets
    def test_get_current_image_right(self, monkeypatch, bird):
        bird._previous_y = 2
        bird.current_position.y = 1.8
        monkeypatch.setattr(
            'entities.Bird._get_serial_image_by_direction', lambda this, direction: direction
        )
        assert bird.get_current_image() == 'right'
        assert bird.current_image == 'right'

    @pytest.mark.yakubets
    def test_get_current_image_top(self, monkeypatch, bird):
        bird._previous_y = 2
        bird.current_position.y = 1
        bird.initial_position.x = 3
        bird.current_position.x = 3
        monkeypatch.setattr(
            'entities.Bird._get_serial_image_by_direction', lambda this, direction: direction
        )
        assert bird.get_current_image() == 'top'
        assert bird.current_image == 'top'

    @pytest.mark.yakubets
    def test_get_current_image_top_right(self, monkeypatch, bird):
        bird._previous_y = 2
        bird.current_position.y = 1
        bird.initial_position.x = 3
        bird.current_position.x = 4
        monkeypatch.setattr(
            'entities.Bird._get_serial_image_by_direction', lambda this, direction: direction
        )
        assert bird.get_current_image() == 'top_right'
        assert bird.current_image == 'top_right'

    @pytest.mark.yakubets
    @pytest.mark.parametrize('direction', ('top', 'right', 'top_right'))
    def test_get_serial_image_by_direction_float_index(self, bird, direction):
        bird._serial_image_indexes = {}
        assert bird._get_serial_image_by_direction(
            direction) == getattr(bird._images, direction)[0]
        assert bird._serial_image_indexes == {direction: 0.25}

    @pytest.mark.yakubets
    @pytest.mark.parametrize('direction', ('top', 'right', 'top_right'))
    def test_get_serial_image_by_direction_int_index(self, bird, direction):
        bird._serial_image_indexes = {direction: 0.75}
        assert bird._get_serial_image_by_direction(
            direction) == getattr(bird._images, direction)[1]
        assert bird._serial_image_indexes == {direction: 1.}

    @pytest.mark.yakubets
    def test_math_function(self, monkeypatch, bird):
        bird.initial_position.y = 10
        bird.initial_position.x = 4
        monkeypatch.setattr('entities.Bird._math_subfunction', lambda this, x: x)
        assert bird._math_function(11) == 3
