import abc
from movie.domainmodels.movie import Movie
from movie.domainmodels.user import User
repo_instance: 'AbstractRepository' = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class AbstractRepository(abc.ABC):
    @property
    @abc.abstractmethod
    def movies(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def users(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def genres(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def actors(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def directors(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, title: str, year: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_id(self, movie_id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_n_movies(self, n: int, offset: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_total_number_of_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_actor(self, actor: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_director(self, director: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_genre(self, genre: str):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_movie(self, movie_to_delete: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username: str):
        raise NotImplementedError
