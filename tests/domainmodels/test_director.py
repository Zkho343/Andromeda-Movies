import pytest

from movie.domainmodels.director import Director


def test_init():
    director_one = Director("James Cameron")
    assert repr(director_one) == "<Director James Cameron>"
    director_two = Director("")
    assert director_two.director_full_name is None


def test_equal():
    director_none_1 = Director("")
    director_none_2 = Director("")

    assert director_none_1 == director_none_2
    director_one = Director("director_two")
    director_two = Director("director_two")
    assert director_one == director_two

    director_three = Director("director_two")
    director_four = Director("director_two")
    assert director_three != director_four
    assert director_none_1 != director_four


def test_lt():
    director_one = Director("Director A")
    director_two = Director("Director B")
    assert director_one < director_two


def test_hash():
    director_one = Director("Director A")
    assert hash(director_one) == hash("Director A")
    director_none = Director("")
    assert hash(director_none) == hash(None)


def test_type_mismatch():
    director_full_name = Director("Director")
    other = "Director"
    with pytest.raises(TypeError):
        return director_full_name < other
