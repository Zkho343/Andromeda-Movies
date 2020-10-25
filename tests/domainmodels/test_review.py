from datetime import datetime
import pytest
from movie.domainmodels.movie import Movie, Review


@pytest.fixture
def movie():
    return Movie("Passenger", 2016)


@pytest.fixture
def movie2():
    return Movie("Passenger2", 2016)


def test_init_invalid(movie):
    username = 'The user'
    review_text = "The movie was great."
    rating = 15
    timestamp = datetime.now().timestamp()
    review = Review(movie, username, review_text, rating, timestamp)

    assert review.movie == movie
    assert review.review_text == review_text
    assert review.rating is None
    assert review.timestamp == timestamp



