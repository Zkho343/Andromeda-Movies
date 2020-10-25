from itertools import islice
from typing import Generator
from movie.adapters.repository import AbstractRepository


def get_num_movies(num: int, offset: int, repo: AbstractRepository):
    return repo.get_n_movies(num, offset)


def get_movie_number(repo: AbstractRepository):
    return repo.get_total_number_of_movies()


def get_movies_actor(offset: int, num: int, repo: AbstractRepository, actor: str):
    movies_gen = repo.get_movies_by_actor(actor)
    movies_count = sum(1 for _ in repo.get_movies_by_actor(actor))
    return _get_items_from_offset(offset, num, movies_gen), movies_count


def get_movies_director(offset: int, num: int, repo: AbstractRepository, director: str):
    movies_gen = repo.get_movies_by_director(director)
    movies_count = sum(1 for _ in repo.get_movies_by_director(director))
    return _get_items_from_offset(offset, num, movies_gen), movies_count


def get_movies_genre(offset: int, num: int, repo: AbstractRepository, genre: str):
    movies_gen = repo.get_movies_by_genre(genre)
    movies_count = sum(1 for _ in repo.get_movies_by_genre(genre))
    return _get_items_from_offset(offset, num, movies_gen), movies_count


def _get_items_from_offset(offset: int, num: int, gen: Generator):
    items = list(islice(gen, offset, offset + num))
    return items
