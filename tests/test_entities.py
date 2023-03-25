import pytest

from data_structures import BirdImages


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

    @pytest.mark.tyl
    def test_down_function(self, bird):
        bird.current_position.x = 3
        bird.initial_position.y = 10
        bird.current_position.y = 5
        assert bird._down_function(0) == 0
        assert bird.current_position.x == 2

    @pytest.mark.tyl
    def test_up_function(self, bird):
        bird.current_position.x = 3
        bird.initial_position.y = 4
        bird.current_position.y = 5
        assert bird._up_function(0) == 0
        assert bird.current_position.x == 2

    @pytest.mark.tyl
    def test_linear_function(self, bird):
        assert bird._linear_function(0) == 0
        assert bird._linear_function(10) == 5

    @pytest.mark.tyl
    def test_root_function(self, bird):
        assert bird._root_function(0) == 0
        assert bird._root_function(4) == 30
        with pytest.raises(ValueError):
            bird._root_function(-1)

    @pytest.mark.tyl
    def test_in_power_function(self, bird):
        assert bird._in_power_function(0) == 0
        assert bird._in_power_function(100) == 20

    @pytest.mark.tyl
    def test_get_math_subfunction_easy_level(self, monkeypatch, bird):
        bird._level = 'easy'
        monkeypatch.setattr('entities.Bird._up_function', '_up_function')
        monkeypatch.setattr('entities.Bird._linear_function', '_linear_function')
        assert bird._get_math_subfunction() in ('_up_function', '_linear_function')

    @pytest.mark.tyl
    def test_get_math_subfunction_medium_level(self, monkeypatch, bird):
        monkeypatch.setattr('entities.Bird._up_function', '_up_function')
        monkeypatch.setattr('entities.Bird._linear_function', '_linear_function')
        monkeypatch.setattr('entities.Bird._root_function', '_root_function')
        assert bird._get_math_subfunction() in (
            '_up_function', '_linear_function', '_root_function'
        )

    @pytest.mark.tyl
    def test_get_math_subfunction_hard_level(self, monkeypatch, bird):
        bird._level = 'hard'
        monkeypatch.setattr('entities.Bird._up_function', '_up_function')
        monkeypatch.setattr('entities.Bird._linear_function', '_linear_function')
        monkeypatch.setattr('entities.Bird._root_function', '_root_function')
        monkeypatch.setattr('entities.Bird._in_power_function', '_in_power_function')
        assert bird._get_math_subfunction() in (
            '_up_function', '_linear_function', '_root_function', '_in_power_function'
        )

    @pytest.mark.tyl
    def test_get_bird_images(self, monkeypatch, bird):
        monkeypatch.setattr('pygame.image.load', lambda x: x)
        assert bird._get_bird_images() == BirdImages(
            top=['images/birds/medium/top_1.png', 'images/birds/medium/top_2.png', 'images/birds/medium/top_3.png'],
            top_right=['images/birds/medium/top_right_1.png', 'images/birds/medium/top_right_2.png', 'images/birds/medium/top_right_3.png'],
            right=['images/birds/medium/right_1.png', 'images/birds/medium/right_2.png', 'images/birds/medium/right_3.png'],
            bottom=['images/birds/medium/bottom_1.png', 'images/birds/medium/bottom_2.png', 'images/birds/medium/bottom_3.png']
        )

    @pytest.mark.tyl
    def test_get_random_position(self, bird):
        bird_position = bird._get_random_position()
        assert 200 <= bird_position.x <= 480
        assert 500 <= bird_position.y <= 555
