import pytest

from movie.domainmodels.actor import Actor
from movie.domainmodels.genre import Genre


def test_init():
    genre1 = Genre("Horror")
    assert repr(genre1) == "<Genre Horror>"
    genre2 = Genre("")
    assert genre2.genre_name is None


def test_lt():
    actor1 = Actor("Actor one")
    actor2 = Actor("Actor two")
    assert actor1 < actor2


def test_equal():
    genre_empty_one = Genre("")
    genre_empty_two = Genre("")
    assert genre_empty_one == genre_empty_two
    genre1 = Genre("Horror")
    genre2 = Genre("Horror")
    assert genre1 == genre2
    genre3 = Genre("Horror")
    genre4 = Genre("Actor")
    assert genre3 != genre4
    assert genre_empty_one != genre4


def test_type_mismatch():
    genre = Genre("Genre")
    other = "Genre"
    with pytest.raises(TypeError):
        return genre < other






