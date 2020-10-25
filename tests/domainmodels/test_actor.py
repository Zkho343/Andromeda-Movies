import pytest

from movie.domainmodels.actor import Actor


def test_init():
    actor1 = Actor("Angelina Jolie")
    assert repr(actor1) == "<Actor Angelina Jolie>"
    actor2 = Actor("")
    assert actor2.actor_full_name is None
    actor3 = Actor(55)
    assert actor3.actor_full_name is None


def test_lt():
    actor1 = Actor("Actor one")
    actor2 = Actor("Actor two")
    assert actor1 < actor2


def test_type_mismatch():
    actor = Actor("Actor")
    others_actors = "Actor"
    with pytest.raises(TypeError):
        return actor < others_actors
