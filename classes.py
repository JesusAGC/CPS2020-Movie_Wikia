from abc import abstractmethod, ABCMeta

class Entity(metaclass=ABCMeta):
    @abstractmethod
    def show_info(self):
        pass

class Data_Getter(metaclass=ABCMeta):
    @abstractmethod
    def get_actor(self):
        pass
    def get_movie(self):
        pass

class Actor(Entity):
    def __init__(self,_actor_id:str, _name:str, _biography:str, _birth_date:str, _death_date:str):
        self.actor_id = _actor_id
        self.name = _name
        self.biography = _biography
        self.birth_date = _birth_date
        self.death_date = _death_date
    
    def show_info(self):
        print(self.actor_id)
        print(self.name+"\n")
        print(self.biography+"\n")
        print(self.birth_date)
        print(self.death_date)

class Movie(Entity):
    def __init__(self,_movie_id:str,_title : str,_date_of_release:str,_overview:str):
        self.movie_id = _movie_id
        self.title = _title
        self.date_of_release = _date_of_release
        self.overview = _overview
    def show_info(self):
        print(self.movie_id)
        print(self.title)
        print(self.date_of_release)
        print(self.overview)