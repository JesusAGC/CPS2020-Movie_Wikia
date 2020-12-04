import unittest
from comms_area import *
from api_interaction import *
from classes import Actor,Movie
import sqlite3

class project_unit_test(unittest.TestCase):
################ API Actor existente#####################################   
    def test_bring_actor_from_api(self):
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
    def test_bring_movie_from_api(self):
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

##################### Traer de BD Actor ################################
    def test_actor_from_BD(self):
        set_1 = Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')
        person = database_searchs.search_actor(self,880)
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(str(person.death_date),set_1.death_date)
############## API Movie Existente por ID ###################################
    def test_bring_movie_from_BD_id(self):
        set_1 = Movie(76341,'Mad Max: Fury Road','2015-05-13','An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.')
        film = database_searchs.search_movie_by_id(self,76341)
        self.assertEqual(film.movie_id,set_1.movie_id)
        self.assertEqual(film.title,set_1.title)
        self.assertEqual(film.date_of_release,set_1.date_of_release)
        self.assertEqual(film.overview,set_1.overview)
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
        sets = [Actor(1,'George Lucas',"George Walton Lucas Jr. (born May 14, 1944) is an American filmmaker and entrepreneur. Lucas is known for creating the Star Wars and Indiana Jones franchises and founding Lucasfilm, LucasArts and Industrial Light & Magic. He served as chairman of Lucasfilm before selling it to The Walt Disney Company in 2012.\n\nAfter graduating from the University of Southern California in 1967, Lucas co-founded American Zoetrope with filmmaker Francis Ford Coppola. Lucas wrote and directed THX 1138 (1971), based on his earlier student short Electronic Labyrinth: THX 1138 4EB, which was a critical success but a financial failure. His next work as a writer-director was the film American Graffiti (1973), inspired by his youth in early 1960s Modesto, California, and produced through the newly founded Lucasfilm. The film was critically and commercially successful, and received five Academy Award nominations including Best Picture.\n\nLucas's next film, the epic space opera Star Wars (1977), had a troubled production but was a surprise hit, becoming the highest-grossing film at the time, winning six Academy Awards and sparking a cultural phenomenon. Lucas produced and co-wrote the sequels The Empire Strikes Back (1980) and Return of the Jedi (1983). With director Steven Spielberg, he created, produced and co-wrote the Indiana Jones films Raiders of the Lost Ark (1981), Temple of Doom (1984), The Last Crusade (1989) and Kingdom of the Crystal Skull (2008). He also produced and wrote a variety of films and television series through Lucasfilm between the 1970s and the 2010s.\n\nIn 1997, Lucas rereleased the Star Wars trilogy as part of a special edition featuring several alterations; home media versions with further changes were released in 2004 and 2011. He returned to directing with a Star Wars prequel trilogy comprising The Phantom Menace (1999), Attack of the Clones (2002), and Revenge of the Sith (2005). He last collaborated on the CGI-animated television series Star Wars: The Clone Wars (2008–2014, 2020), the war film Red Tails (2012), and the CGI film Strange Magic (2015).\n\nLucas is one of history's most financially successful filmmakers and has been nominated for four Academy Awards. His films are among the 100 highest-grossing movies at the North American box office, adjusted for ticket-price inflation. Lucas is considered a significant figure of the 20th-century New Hollywood movement.\n\nDescription above from the Wikipedia article George Lucas, licensed under CC-BY-SA, full list of contributors on Wikipedia.",'1944-05-14','None'), Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')]
        all_actors = database_searchs.get_all_actors(self)
        for x in range(len(all_actors)):
            self.assertEqual(all_actors[x].actor_id, sets[x].actor_id)
            self.assertEqual(all_actors[x].name, sets[x].name)
            self.assertEqual(all_actors[x].biography, sets[x].biography)
            self.assertEqual(all_actors[x].birth_date, sets[x].birth_date)
            self.assertEqual(str(all_actors[x].death_date), sets[x].death_date)
################# Get all Movies ############################################
    def test_get_all_movies(self):
        movie_list = database_searchs.get_all_movies(self)
        sets = [Movie(28,'Apocalypse Now','1979-08-15','At the height of the Vietnam war, Captain Benjamin Willard is sent on a dangerous mission that, officially, "does not exist, nor will it ever exist." His goal is to locate - and eliminate - a mysterious Green Beret Colonel named Walter Kurtz, who has been leading his personal army on illegal guerrilla missions into enemy territory.'), Movie(76341,'Mad Max: Fury Road','2015-05-13','An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order.')]
        for x in range(len(movie_list)):
            self.assertEqual(movie_list[x].movie_id,sets[x].movie_id)
            self.assertEqual(movie_list[x].title,sets[x].title)
            self.assertEqual(movie_list[x].date_of_release,sets[x].date_of_release)
            self.assertEqual(movie_list[x].overview,sets[x].overview)
################# insert  Actor BD ##################################################
    def test_insert_actor(self):
        set_2 = Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')
        database_workclass.insert_actor(self,set_2)
        
        set_1 = Actor(880,'Ben Affleck','Ben Affleck (born Benjamin Géza Affleck-Boldt; August 15, 1972) is an American actor, film director, writer, and producer. He became known in the mid-1990s with his performance in the Kevin Smith films Mallrats (1995) and Chasing Amy (1997). Affleck is an Academy Award as well as a Golden Globe Award winner, along with Matt Damon, for their collaborative screenplay for the 1997 film Good Will Hunting. He established himself as a Hollywood leading man, having starred in several big budget films, such as Armageddon (1998), Pearl Harbor (2001), Changing Lanes (2002), The Sum of All Fears (2002), and Daredevil (2003). Affleck also portrays Bruce Wayne/Batman in the DC Extended Universe. He has portrayed the character in Batman vs Superman: Dawn of Justice (2016), Suicide Squad (2016), and Justice League (2017). He will reprise the role in 2021’s new version of Zack Snyder’s Justice League.  Affleck has drawn critical acclaim for his work as a filmmaker, directing Gone Baby Gone (2007) and The Town (2010), and playing the lead role in the latter. He has worked with his younger brother, actor Casey Affleck, on several projects, including Good Will Hunting and Gone Baby Gone.\n\nAfter a high profile relationship with actress Gwyneth Paltrow in 1998, his relationship with actress/singer Jennifer Lopez attracted worldwide media attention in which Affleck and Lopez were dubbed "Bennifer". Following their breakup in 2004, he began dating Jennifer Garner. The two married in June 2005 and have two daughters, Violet Anne, born December 2005, and Seraphina Rose Elizabeth, born January 2009.\n\nAffleck has been actively involved in politics and charitable causes. He and Matt Damon also founded the production company LivePlanet.\n\nDescription above from the Wikipedia article Ben Affleck, licensed under CC-BY-SA, full list of contributors on Wikipedia.','1972-08-15','None')
        person = database_searchs.search_actor(self,880)
        self.assertEqual(person.actor_id,set_1.actor_id)
        self.assertEqual(person.name,set_1.name)
        self.assertEqual(person.biography,set_1.biography)
        self.assertEqual(person.birth_date,set_1.birth_date)
        self.assertEqual(str(person.death_date),set_1.death_date)
#################Insert 
if __name__=='__main__':
    unittest.main()