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
    def test_bring_actor_from_api_not_exist(self, search_actor):
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
    def test_bring_movie_from_api_not_exist(self,search_movie_by_id):
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
########################### traer peliculas de BD ############################################################
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
#################### traer Actores de BD ########################################
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
    def test_bring_movies_list_from_DB_(self,get_all_movies):
        movie_list = data_getter_from_database.get_all_movies_from_db(self)
        sets = [Movie(1,'Spider-Man','2002','Really cool movie'), Movie(2,'Scarface','1983','Retro movie')]
        for x in range(len(movie_list)):
            self.assertEqual(movie_list[x].movie_id,sets[x].movie_id)
            self.assertEqual(movie_list[x].title,sets[x].title)
            self.assertEqual(movie_list[x].date_of_release,sets[x].date_of_release)
            self.assertEqual(movie_list[x].overview,sets[x].overview)
##########################################################################################################################            
################################################ Test api_interaction ####################################################
##########################################################################################################################

################ API Actor existente#####################################   
    def test_bring_actor_from_api_inte(self):
        person = data_getter_from_api.get_actor(self,880)
        set_1 = Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(str(person.death_date),set_1.death_date)
############## API Actor no existente##################################
    def test_bring_actor_from_api_no_existente(self):
        person = data_getter_from_api.get_actor(self,3123135414124124123)
        set_1 = Actor(3123135414124124123,'None','None','None','None')
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(str(person.name),set_1.name)
        self.assertEqual(str(person.biography),set_1.biography)
        self.assertEqual(str(person.birth_date),set_1.birth_date)
        self.assertEqual(str(person.death_date),set_1.death_date)
############## API Movie Existente ###################################
    def test_bring_movie_from_api_inte(self):
        set_1 = Movie(76341,'Mad Max: Fury Road','2015-05-13','An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.')
        film = data_getter_from_api.get_movie(self,76341)
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(film.title,set_1.title)
        self.assertEqual(film.date_of_release,set_1.date_of_release)
        self.assertEqual(film.overview,set_1.overview)
############## API Movie no Existente ###################################
    def test_bring_movie_from_api_no_existente(self):
        set_1 = Movie(31241232351234324,'None','None','None')
        film = data_getter_from_api.get_movie(self,31241232351234324)
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(str(film.title),set_1.title)
        self.assertEqual(str(film.date_of_release),set_1.date_of_release)
        self.assertEqual(str(film.overview),set_1.overview)
        
############################################################################################
############################### unitarios ###################################################
#############################################################################################
##################### Traer de BD Actor ################################
    def test_actor_from_BD(self):

        set_1 = Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')
        database_workclass.insert_actor(self,set_1)
        person = database_searchs.search_actor(self,880)
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(str(person.death_date),set_1.death_date)
        database_workclass.delete_actor(self,set_1.actor_id)

############## BD Movie Existente por ID ###################################
    def test_bring_movie_from_BD_id(self):
        set_1 = Movie(76341,'Mad Max: Fury Road','2015-05-13','An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.')
        database_workclass.insert_movie(self,set_1)        
        film = database_searchs.search_movie_by_id(self,76341)
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(film.title,set_1.title)
        self.assertEqual(film.date_of_release,set_1.date_of_release)
        self.assertEqual(film.overview,set_1.overview)
        database_workclass.delete_movie(self,set_1.movie_id)

############## API Movie Existente por Nombre ###################################
   # def test_bring_movie_from_BD_Title(self):
   #     set_1 = Movie(557,'Spider-Man','2002-05-01','After being bitten by a genetically altered spider, nerdy high school student Peter Parker is endowed with amazing powers to become the Amazing superhero known as Spider-Man.')
   #     film = database_searchs.search_movie_by_title(self,'Mad Max: Fury Road')
   #     self.assertEqual(film.movie_id,set_1.movie_id)
   #     self.assertEqual(film.title,set_1.title)
   #     self.assertEqual(film.date_of_release,set_1.date_of_release)
   #     self.assertEqual(film.overview,set_1.overview)
############  Get All Actors ################################################
    def test_get_all_actors(self):
        set_1 =  Actor(1,'George Lucas',"George Walton Lucas Jr. (born May 14, 1944) is an American filmmaker and entrepreneur. Lucas is known for creating the Star Wars and Indiana Jones franchises and founding Lucasfilm, LucasArts and Industrial Light & Magic. He served as chairman of Lucasfilm before selling it to The Walt Disney Company in 2012.\n\nAfter graduating from the University of Southern California in 1967, Lucas co-founded American Zoetrope with filmmaker Francis Ford Coppola. Lucas wrote and directed THX 1138 (1971), based on his earlier student short Electronic Labyrinth: THX 1138 4EB, which was a critical success but a financial failure. His next work as a writer-director was the film American Graffiti (1973), inspired by his youth in early 1960s Modesto, California, and produced through the newly founded Lucasfilm. The film was critically and commercially successful, and received five Academy Award nominations including Best Picture.\n\nLucas's next film, the epic space opera Star Wars (1977), had a troubled production but was a surprise hit, becoming the highest-grossing film at the time, winning six Academy Awards and sparking a cultural phenomenon. Lucas produced and co-wrote the sequels The Empire Strikes Back (1980) and Return of the Jedi (1983). With director Steven Spielberg, he created, produced and co-wrote the Indiana Jones films Raiders of the Lost Ark (1981), Temple of Doom (1984), The Last Crusade (1989) and Kingdom of the Crystal Skull (2008). He also produced and wrote a variety of films and television series through Lucasfilm between the 1970s and the 2010s.\n\nIn 1997, Lucas rereleased the Star Wars trilogy as part of a special edition featuring several alterations; home media versions with further changes were released in 2004 and 2011. He returned to directing with a Star Wars prequel trilogy comprising The Phantom Menace (1999), Attack of the Clones (2002), and Revenge of the Sith (2005). He last collaborated on the CGI-animated television series Star Wars: The Clone Wars (2008–2014, 2020), the war film Red Tails (2012), and the CGI film Strange Magic (2015).\n\nLucas is one of history's most financially successful filmmakers and has been nominated for four Academy Awards. His films are among the 100 highest-grossing movies at the North American box office, adjusted for ticket-price inflation. Lucas is considered a significant figure of the 20th-century New Hollywood movement.\n\nDescription above from the Wikipedia article George Lucas, licensed under CC-BY-SA, full list of contributors on Wikipedia.",'1944-05-14','None')
        set_2 = Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')
        database_workclass.insert_actor(self,set_1)
        database_workclass.insert_actor(self,set_2)

        sets = [Actor(1,'George Lucas',"George Walton Lucas Jr. (born May 14, 1944) is an American filmmaker and entrepreneur. Lucas is known for creating the Star Wars and Indiana Jones franchises and founding Lucasfilm, LucasArts and Industrial Light & Magic. He served as chairman of Lucasfilm before selling it to The Walt Disney Company in 2012.\n\nAfter graduating from the University of Southern California in 1967, Lucas co-founded American Zoetrope with filmmaker Francis Ford Coppola. Lucas wrote and directed THX 1138 (1971), based on his earlier student short Electronic Labyrinth: THX 1138 4EB, which was a critical success but a financial failure. His next work as a writer-director was the film American Graffiti (1973), inspired by his youth in early 1960s Modesto, California, and produced through the newly founded Lucasfilm. The film was critically and commercially successful, and received five Academy Award nominations including Best Picture.\n\nLucas's next film, the epic space opera Star Wars (1977), had a troubled production but was a surprise hit, becoming the highest-grossing film at the time, winning six Academy Awards and sparking a cultural phenomenon. Lucas produced and co-wrote the sequels The Empire Strikes Back (1980) and Return of the Jedi (1983). With director Steven Spielberg, he created, produced and co-wrote the Indiana Jones films Raiders of the Lost Ark (1981), Temple of Doom (1984), The Last Crusade (1989) and Kingdom of the Crystal Skull (2008). He also produced and wrote a variety of films and television series through Lucasfilm between the 1970s and the 2010s.\n\nIn 1997, Lucas rereleased the Star Wars trilogy as part of a special edition featuring several alterations; home media versions with further changes were released in 2004 and 2011. He returned to directing with a Star Wars prequel trilogy comprising The Phantom Menace (1999), Attack of the Clones (2002), and Revenge of the Sith (2005). He last collaborated on the CGI-animated television series Star Wars: The Clone Wars (2008–2014, 2020), the war film Red Tails (2012), and the CGI film Strange Magic (2015).\n\nLucas is one of history's most financially successful filmmakers and has been nominated for four Academy Awards. His films are among the 100 highest-grossing movies at the North American box office, adjusted for ticket-price inflation. Lucas is considered a significant figure of the 20th-century New Hollywood movement.\n\nDescription above from the Wikipedia article George Lucas, licensed under CC-BY-SA, full list of contributors on Wikipedia.",'1944-05-14','None'), Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')]
        all_actors = database_searchs.get_all_actors(self)
        for x in range(len(all_actors)):
            self.assertEqual(all_actors[x].actor_id, sets[x].actor_id)
            self.assertEqual(all_actors[x].name, sets[x].name)
            self.assertEqual(all_actors[x].biography, sets[x].biography)
            self.assertEqual(all_actors[x].birth_date, sets[x].birth_date)
            self.assertEqual(str(all_actors[x].death_date), sets[x].death_date)
        database_workclass.delete_actor(self,set_1.actor_id)
        database_workclass.delete_actor(self,set_2.actor_id)
################# Get all Movies ############################################
    def test_get_all_movies(self):
        set_1 = Movie(28,'Apocalypse Now','1979-08-15','At the height of the Vietnam war, Captain Benjamin Willard is sent on a dangerous mission that, officially, "does not exist, nor will it ever exist." His goal is to locate - and eliminate - a mysterious Green Beret Colonel named Walter Kurtz, who has been leading his personal army on illegal guerrilla missions into enemy territory.')
        set_2 = Movie(76341,'Mad Max: Fury Road','2015-05-13','An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.')
        database_workclass.insert_movie(self,set_1)
        database_workclass.insert_movie(self,set_2)

        movie_list = database_searchs.get_all_movies(self)
        sets = [Movie(28,'Apocalypse Now','1979-08-15','At the height of the Vietnam war, Captain Benjamin Willard is sent on a dangerous mission that, officially, "does not exist, nor will it ever exist." His goal is to locate - and eliminate - a mysterious Green Beret Colonel named Walter Kurtz, who has been leading his personal army on illegal guerrilla missions into enemy territory.'), Movie(76341,'Mad Max: Fury Road','2015-05-13','An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.')]
        for x in range(len(movie_list)):
            self.assertEqual(movie_list[x].movie_id,sets[x].movie_id)
            self.assertEqual(movie_list[x].title,sets[x].title)
            self.assertEqual(movie_list[x].date_of_release,sets[x].date_of_release)
            self.assertEqual(movie_list[x].overview,sets[x].overview)
        database_workclass.delete_movie(self,set_1.movie_id)
        database_workclass.delete_movie(self,set_2.movie_id)
        

################# insert  Actor BD ##################################################
    def test_insert_actor(self):
        set_2 = Actor(2219,'Tobey Maguire',"Tobias Vincent Maguire is an American actor and film producer. He gained recognition for his role as Peter Parker / Spider-Man in Sam Raimi's Spider-Man trilogy. His other major films include Pleasantville, The Cider House Rules, Wonder Boys, Seabiscuit, The Good German, Brothers, and The Great Gatsby. Wikipedia",'1975-06-27','None')
        database_workclass.insert_actor(self,set_2)
        
        set_1 = Actor(2219,'Tobey Maguire',"Tobias Vincent Maguire is an American actor and film producer. He gained recognition for his role as Peter Parker / Spider-Man in Sam Raimi's Spider-Man trilogy. His other major films include Pleasantville, The Cider House Rules, Wonder Boys, Seabiscuit, The Good German, Brothers, and The Great Gatsby. Wikipedia",'1975-06-27','None')
        person = database_searchs.search_actor(self,2219)
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(str(person.death_date),set_1.death_date)
        database_workclass.delete_actor(self,2219)

    
################# Insert Movie BD #################################################
    def test_insert_movie(self):
        set_2 = Movie(238,'The Godfather','1972-03-14','Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.')
        database_workclass.insert_movie(self,set_2)
        
        set_1 = Movie(238,'The Godfather','1972-03-14','Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.')
        film = database_searchs.search_movie_by_id(self,238)
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(film.title,set_1.title)
        self.assertEqual(film.date_of_release,set_1.date_of_release)
        self.assertEqual(film.overview,set_1.overview)
        database_workclass.delete_movie(self,238)

################ Update Actor BD #################################################
    def test_update_actor(self):
        set_2 = Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')
        database_workclass.insert_actor(self,set_2)
        set_3 = Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')
        
        database_workclass.update_actor(self,set_3)
        
        set_1 = Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')
        person = database_searchs.search_actor(self,880)
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(str(person.death_date),set_1.death_date)
        database_workclass.delete_actor(self,set_1.actor_id)
        
################# Update Movie BD #################################################
    def test_update_movie(self):
        set_2 = Movie(76341,'Mad Max: Fury Road','2015-05-13','An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.')
        database_workclass.insert_movie(self,set_2)
        set_3 = Movie(76341,'Mad Max: Fury Road','2015-05-13','An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.')
        database_workclass.update_movie(self,set_3)
        
        set_1 = Movie(76341,'Mad Max: Fury Road','2015-05-13','An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.')
        film = database_searchs.search_movie_by_id(self,76341)
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(film.title,set_1.title)
        self.assertEqual(film.date_of_release,set_1.date_of_release)
        self.assertEqual(film.overview,set_1.overview)
        database_workclass.insert_movie(self,set_3)

############# Delete Actor BD #############################
    def test_delete_actor(self):
        set_2 = Actor(1327,'Ian McKellen',"Sir Ian Murray McKellen, CH, CBE (born 25 May 1939) is an English actor. He is the recipient of six Laurence Olivier Awards, a Tony Award, a Golden Globe Award, a Screen Actors Guild Award, a BIF Award, two Saturn Awards, four Drama Desk Awards and two Critics' Choice Awards. He has also received two Academy Award nominations, eight BAFTA film and TV nominations and five Emmy Award nominations. McKellen's work spans genres ranging from Shakespearean and modern theatre to popular fantasy and science fiction. His notable film roles include Gandalf in The Lord of the Rings and The Hobbit trilogies and Magneto in the X-Men films.",'1939-05-25','None')
        database_workclass.insert_actor(self,set_2)
        database_workclass.delete_actor(self,1327)
        
        set_1 = Actor('0','Not found','No data','No data','No data')
        person = database_searchs.search_actor(self,1327)
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(str(person.death_date),set_1.death_date)

############# Delete Movie BD #############################
    def test_delete_movie(self):
        set_2 = Movie(105,'Back to the Future','1985-07-03',"Eighties teenager Marty McFly is accidentally sent back in time to 1955, inadvertently disrupting his parents' first meeting and attracting his mother's romantic interest. Marty must repair the damage to history by rekindling his parents' romance and - with the help of his eccentric inventor friend Doc Brown - return to 1985.")
        database_workclass.insert_movie(self,set_2)
        database_workclass.delete_movie(self,105)        
        set_1 = Movie('0','Not found','No data','No data')
        film = database_searchs.search_movie_by_id(self,105)
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(film.title,set_1.title)
        self.assertEqual(film.date_of_release,set_1.date_of_release)
        self.assertEqual(film.overview,set_1.overview)

if __name__=='__main__':
    unittest.main()