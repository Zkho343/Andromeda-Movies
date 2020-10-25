import pytest
from movie.domainmodels.user import User


def test_init():
    user_one = User("Zkho343", "pass2019200")
    print(user_one)
    user_two = User("", "")
    assert user_two.username == ""


def test_equal():
    equality1 = User("Zkho343", "pass2020")
    equality2 = User("sfas343", "pakor2019")
    assert equality1 != equality2

    equality3 = User("Zkho343", "pass2020")
    equality4 = User("Zkho343", "pass2020")
    assert equality3 == equality4


def test_lt():
    user_one = User('Zoho343', 'pw12452')
    user_two = User('sfas343', 'pw12451')
    assert user_one < user_two
    with pytest.raises(TypeError):
        _ = user_one < 'c'
