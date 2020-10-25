import csv

from movie.domainmodels.actor import Actor
from movie.domainmodels.director import Director
from movie.domainmodels.genre import Genre
from movie.domainmodels.movie import Movie


class MovieFileCSVReader:
    def __init__(self, file_name):
        self.file_name = file_name

        self.movies = []

        self.actors = set()
        self.directors = set()
        self.genres = set()

    @property
    def dataset_of_movies(self):
        return self.movies

    @dataset_of_movies.setter
    def dataset_of_movies(self, newMovies):
        self.movies = newMovies

    @property
    def dataset_of_actors(self):
        return self.actors

    @dataset_of_actors.setter
    def dataset_of_actors(self, newActors):
        self.actors = newActors

    @property
    def dataset_of_directors(self):
        return self.directors

    @dataset_of_directors.setter
    def dataset_of_directors(self, newDirectors):
        self.directors = newDirectors

    @property
    def dataset_of_genres(self):
        return self.genres

    @dataset_of_genres.setter
    def dataset_of_genres(self, newGenres):
        self.genres = newGenres

    def read_csv_file(self):
        try:
            TheCVS_file = open(self.file_name, encoding='utf-8-sig', newline='')
            to_reader = csv.DictReader(TheCVS_file)

            for All_row in to_reader:
                try:
                    movie = Movie(All_row['Title'].strip(), int(All_row['Year'].strip()))
                    actors = All_row['Actors'].split(',')

                    for num in range(len(actors)):
                        actors[num] = Actor(actors[num].strip())

                    split_rows = All_row['Genre'].split(',')
                    director = Director(All_row['Director'].strip())
                    genres = split_rows

                    for num in range(len(genres)):
                        genres[num] = Genre(genres[num].strip())

                    self.movies.append(movie)
                    self.actors.update(set(actors))

                    self.directors.add(director)
                    self.genres.update(set(genres))

                except:
                    continue

            TheCVS_file.close()

        except:
            raise Exception("Error while reading CSV file!")
