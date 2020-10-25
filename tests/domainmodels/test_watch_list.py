import pytest

from movie.domainmodels.movie import Movie
from movie.domainmodels.watch_list import WatchList


@pytest.fixture
def watch_list():
    return WatchList()


def test_add_movie(watch_list):
    assert watch_list.size() == 0
    watch_list.add_movie(Movie("Passenger", 2016))
    watch_list.add_movie(Movie("avenger first solder", 2011))
    watch_list.add_movie(Movie("gravity", 2017))
    assert watch_list.size() == 3
    watch_list.add_movie(Movie("avenger first solder", 2011))
    assert watch_list.size() == 3


def test_remove_movie(watch_list):
    watch_list.add_movie(Movie("Passenger", 2016))
    watch_list.add_movie(Movie("avenger first solder", 2011))
    watch_list.add_movie(Movie("gravity", 2017))
    watch_list.remove_movie(Movie("avenger first solder", 2011))
    assert watch_list.size() == 2
    watch_list.remove_movie(Movie("Moana", 2017))
    assert watch_list.size() == 2






