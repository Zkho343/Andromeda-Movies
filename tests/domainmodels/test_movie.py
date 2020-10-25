import pytest

from movie.domainmodels.movie import Movie
from movie.domainmodels.director import Director


def test_init():
    movie_one = Movie("Passengers", 2016)
    assert repr(movie_one) == "<Movie Passengers, 2016>"
    movie_one = Movie("", 1899)
    assert movie_one.title is None
    assert repr(movie_one) == "<Movie None, None>"


def test_get_title():
    movie_one = Movie("Passengers", 2016)
    assert movie_one.title == "Passengers"


def test_set_title():
    movie_one = Movie("Passengers", 2016)
    movie_one.title = "Passengers"
    assert movie_one.title == "Passengers"


def test_get_director():
    movie1 = Movie("Passengers", 2016)
    assert movie1.director is None


def test_set_director():
    movie1 = Movie("Passengers", 2016)
    director = Director("Director")
    movie1.director = director
    assert movie1.director == director
    director_invalid = "Director"
    movie1.director = director_invalid
    assert movie1.director == director


def test_set_runtime_minutes():
    movie1 = Movie("Passengers", 2016)
    with pytest.raises(ValueError):
        movie1.runtime_minutes = 0
