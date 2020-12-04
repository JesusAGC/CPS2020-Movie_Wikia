import unittest
from unittest import mock
from unittest.mock import patch
from comms_area import *
from classes import Actor,Movie

class project_unit_test(unittest.TestCase):
########################## API Actor Existente ##############################################
    mock_data = {'id':'1','name':'George Lucas','biography':'Creador de Star Wars','birthday':'1944-05-14','deathday':'None'}
    @patch('api_interaction.api_searchs.search_actor', return_value = mock_data)
    def test_bring_actor_from_api(self, search_actor):
        person = data_getter_from_api.get_actor(self,1)
        set_1 = Actor(1,'George Lucas','Creador de Star Wars','1944-05-14','None')
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(person.death_date,set_1.death_date)

################################ API Actor no existente ######################################
    mock_data = {'id':'0','name':'Not found','biography':'No data','birthday':'No data','deathday':'No data'}
    @patch('api_interaction.api_searchs.search_actor', return_value = mock_data)
    def test_bring_actor_from_api(self, search_actor):
        person = data_getter_from_api.get_actor(self,0)
        set_1 = Actor(0,'Not found','No data','No data','No data')
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(person.death_date,set_1.death_date)

############################## API Movie Existente ###########################################
    mock_data = {'id':'1', 'original_title':'Spider-Man','release_date':'2002','overview':'Really cool movie'}
    @patch('api_interaction.api_searchs.search_movie_by_id',return_value = mock_data)
    def test_bring_movie_from_api(self,search_movie_by_id):
        set_1 = Movie(1,'Spider-Man','2002','Really cool movie')
        film = data_getter_from_api.get_movie(self,1)
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(film.title,set_1.title)
        self.assertEqual(film.date_of_release,set_1.date_of_release)
        self.assertEqual(film.overview,set_1.overview)
########################### API Movie No existente ############################################3
 mock_data = {'id':'0', 'original_title':'no found','release_date':'no data','overview':'no data'}
    @patch('api_interaction.api_searchs.search_movie_by_id',return_value = mock_data)
    def test_bring_movie_from_api(self,search_movie_by_id):
        set_1 = Movie(0,'no found','no data','no data')
        film = data_getter_from_api.get_movie(self,0)
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(film.title,set_1.title)
        self.assertEqual(film.date_of_release,set_1.date_of_release)
        self.assertEqual(film.overview,set_1.overview)
    
################################## Mostrar todas las peliculas ##############################################################    
    mock_data ={'results':[{'id':1, 'original_title':'Spider-Man','release_date':'2002','overview':'Really cool movie'},
                            {'id':2, 'original_title':'Scarface','release_date':'1983','overview':'Retro movie'}]}
    @patch('api_interaction.api_searchs.search_movie_by_title',return_value = mock_data)
    def test_bring_movies_list_api(self,search_movie_by_title):
        set_1 = Movie(1,'Spider-Man','2002','Really cool movie')
        set_2 = Movie(2,'Scarface','1983','Retro movie')
        sets = []
        sets.append(set_1)
        sets.append(set_2)
        movie_list = data_getter_from_api.get_movie_by_title(self,'Mokceado')
        for x in range(len(movie_list)):
            self.assertEqual(movie_list[x].movie_id,sets[x].movie_id)
            self.assertEqual(movie_list[x].title,sets[x].title)
            self.assertEqual(movie_list[x].date_of_release,sets[x].date_of_release)
            self.assertEqual(movie_list[x].overview,sets[x].overview)
################################### Mostar todas los Actores ##########################################################3
    mock_data = Actor(1,'George Lucas','Creador de Star Wars','1944-05-14','None')
    @patch('api_interaction.database_searchs.search_actor', return_value = mock_data)
    def test_bring_actor_from_DB(self,search_actor):
        person = data_getter_from_database.get_actor(self,'Mock')
        set_1 = Actor(1,'George Lucas','Creador de Star Wars','1944-05-14','None')
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(person.death_date,set_1.death_date)        
########################### Traer pelicula de BD ##################################################
    mock_data = Movie(1,'Spider-Man','2002','Really cool movie')
    @patch('api_interaction.database_searchs.search_movie_by_id', return_value = mock_data)
    def test_bring_movie_from_DB(self,search_movie_by_id):
        film = data_getter_from_database.get_movie_by_id(self,'MOck')
        set_1 = Movie(1,'Spider-Man','2002','Really cool movie')
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(film.title,set_1.title)
        self.assertEqual(film.date_of_release,set_1.date_of_release)
        self.assertEqual(film.overview,set_1.overview)

    mock_data = [Movie(1,'Spider-Man','2002','Really cool movie'), Movie(2,'Scarface','1983','Retro movie')]
    @patch('api_interaction.database_searchs.search_movie_by_title', return_value = mock_data)
    def test_bring_movies_list_from_DB(self,search_movie_by_title):
        movie_list = data_getter_from_database.get_movie_by_title(self,'_Mocks_')
        sets = [Movie(1,'Spider-Man','2002','Really cool movie'), Movie(2,'Scarface','1983','Retro movie')]
        for x in range(len(movie_list)):
            self.assertEqual(movie_list[x].movie_id,sets[x].movie_id)
            self.assertEqual(movie_list[x].title,sets[x].title)
            self.assertEqual(movie_list[x].date_of_release,sets[x].date_of_release)
            self.assertEqual(movie_list[x].overview,sets[x].overview)

    mock_data = [Actor(1,'George Lucas','Creador de Star Wars','1944-05-14','None'), Actor(2,'Al Pacino','Finge ser Gangstre','1940-04-25','None')]
    @patch('api_interaction.database_searchs.get_all_actors', return_value = mock_data)
    def test_bring_all_actors_from_DB(self,get_all_actors):
        all_actors = data_getter_from_database.get_all_actors_from_db(self)
        sets = [Actor(1,'George Lucas','Creador de Star Wars','1944-05-14','None'), Actor(2,'Al Pacino','Finge ser Gangstre','1940-04-25','None')]
        for x in range(len(all_actors)):
            self.assertEqual(all_actors[x].actor_id, sets[x].actor_id)
            self.assertEqual(all_actors[x].name, sets[x].name)
            self.assertEqual(all_actors[x].biography, sets[x].biography)
            self.assertEqual(all_actors[x].birth_date, sets[x].birth_date)
            self.assertEqual(all_actors[x].death_date, sets[x].death_date)

    mock_data = [Movie(1,'Spider-Man','2002','Really cool movie'), Movie(2,'Scarface','1983','Retro movie')]
    @patch('api_interaction.database_searchs.get_all_movies', return_value = mock_data)
    def test_bring_movies_list_from_DB(self,get_all_movies):
        movie_list = data_getter_from_database.get_all_movies_from_db(self)
        sets = [Movie(1,'Spider-Man','2002','Really cool movie'), Movie(2,'Scarface','1983','Retro movie')]
        for x in range(len(movie_list)):
            self.assertEqual(movie_list[x].movie_id,sets[x].movie_id)
            self.assertEqual(movie_list[x].title,sets[x].title)
            self.assertEqual(movie_list[x].date_of_release,sets[x].date_of_release)
            self.assertEqual(movie_list[x].overview,sets[x].overview)


if __name__=='__main__':
    unittest.main()