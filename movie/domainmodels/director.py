class Director:

    def __init__(self, full_name):
        empty_string = ""
        if full_name is empty_string:
            full_name = None

        self.director_full_name = full_name

    @property
    def director_full_name(self):
        return self._director_full_name

    @director_full_name.setter
    def director_full_name(self, elements):
        self._director_full_name = elements

    #  top print all the operations as a string
    def __repr__(self):
        string = f"<Director {self._director_full_name}>"
        return string

    # to check whether the value is equal or not in the class
    def __eq__(self, object):
        return (self._director_full_name is
                object.director_full_name)

    def __lt__(self, objects):
        lessThanOther = (self._director_full_name <
                         objects.director_full_name)

        return lessThanOther

    # to make sure everything is put to dictionaries and its hashable
    def __hash__(self):
        hashing = hash(self._director_full_name)
        return hashing
