class Person:
    def __init__(self, name):
        empty_string = ""
        if name == empty_string:
            if type(name) is not str:
                self._name = None
        else:
            self._name = name.strip()

    def __eq__(self, other):
        if type(self) == type(other):
            if self._name == other._name:
                return True
        else:
            return False

    def __hash__(self):
        return hash(self._name)

    def __lt__(self, other):
        if type(self) == type(other):
            if self._name < other._name:
                return True
        elif type(self) != type(other):
            raise TypeError(f"Cannot compare {type(self)} with {type(other)}")
        else:
            return False

    def __repr__(self):
        string = f"<{self.__class__.__name__} {self._name}>"
        return string
