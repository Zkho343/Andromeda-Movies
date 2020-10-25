from movie.domainmodels.movie import Movie, Review


class User:
    def __init__(self, username, password):
        num = 0
        self.the_username = str(username.strip().lower())
        self.the_password = str(password)

        self.all_watched_movies = []
        self.list_of_reviews = []

        self.total_time_watched_movie = num

    @property
    def username(self):
        return self.the_username

    @property
    def password(self):
        return self.the_password

    @property
    def watched_movies(self):
        return self.all_watched_movies

    @property
    def reviews(self):
        allReviews = self.list_of_reviews
        return allReviews

    @property
    def time_spent_watching_movies_minutes(self):
        full_time = self.total_time_watched_movie
        return full_time

    def __repr__(self):
        string = f"<User {self.username}>"
        return string

    def __eq__(self, other: 'User'):
        if type(other) == User:
            return self.username == other.username
        else:
            return False

    def __lt__(self, other: 'User'):
        if type(other) == User:
            return self.username < other.username
        elif type(other) == User:
            print("Cannot compare User type with ", type(other))

    def __hash__(self):
        hashing = hash(self.username)
        return hashing

    def watch_movie(self, movie: Movie):
        if movie in self.watched_movies:
            pass
        else:
            self.all_watched_movies.append(movie)
            self.total_time_watched_movie = self.total_time_watched_movie + movie.runtime_minutes

    def add_review(self, review: Review):
        if review in self.review:
            pass
        else:
            self.list_of_reviews.append(review)

    def remove_review(self, review):
        self.list_of_reviews.remove(review)

    def to_dict(self):
        string = {'username': self.username, 'password': self.password}
        return string
