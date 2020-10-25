from movie.domainmodels.person import Person


class Actor(Person):
    def __init__(self, actor_full_name):

        self.actor_name = None
        string_actor_name = str(actor_full_name)
        super().__init__(string_actor_name)
        self.__colleague_set = set()

    @property
    def actor_full_name(self):
        return self._name

    def add_actor_colleague(self, colleague: 'Actor'):
        if type(self) != type(colleague):
            print(f"Expect colleague to be Actor type, instead {type(colleague)} found")
        self.__colleague_set.add(colleague)

    def check_if_this_actor_worked_with(self, colleague: 'Actor'):
        all_colleagues = colleague in self.__colleague_set
        return all_colleagues
