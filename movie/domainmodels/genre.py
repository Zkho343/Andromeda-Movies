class Genre:

    def __init__(self, genre_name):
        empty_string = ""
        if genre_name is empty_string:
            genre_name = None

        self.genre_name = genre_name

    @property
    def genre_name(self):
        return self._genre_name

    @genre_name.setter
    def genre_name(self, objects):
        self._genre_name = objects

    #  top print all the operations as a string
    def __repr__(self):
        string = f"<Genre {self._genre_name}>"
        return string

    # to check whether the value is equal or not in the class
    def __eq__(self, object):
        return object and (self._genre_name is
                           object.genre_name)

    def __lt__(self, object):
        lessThanOther = object and (self._genre_name <
                                    object.genre_name)

        return lessThanOther

    # to make sure everything is put to dictionaries and its hashable
    def __hash__(self):
        hashing = hash(self._genre_name)
        return hashing