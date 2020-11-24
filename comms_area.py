import time
from api_interaction import api_searchs,database_searchs,database_workclass
from abc import abstractmethod, ABCMeta
import csv
from classes import *
api_s =api_searchs()
db_s = database_searchs()
db_w = database_workclass()


class data_getter_from_api(Data_Getter):
    def get_actor(self,_id):
        data = api_s.search_actor(_id)
        name = data.get('name')
        bio = data.get('biography')
        birth = data.get('birthday')
        death = data.get('deathday')
        actor_search = Actor(_id,name,bio,birth,death)
        return actor_search

    def get_movie(self,_id):
        data = api_s.search_movie_by_id(_id)
        title = data.get('original_title')
        release_data = data.get('release_date')
        movie_search = Movie(_id,title,release_data)
        return movie_search
    
    def get_movie_by_title(self,_movie_query:str):
        data = api_s.search_movie_by_title(_movie_query)
        movie_dictionary_list = data.get('results')
        movie_list = []
        for x in range(len(movie_dictionary_list)):
            act_dict = movie_dictionary_list[x]
            mov_id =act_dict.get("id")
            mov_title = act_dict.get("original_title")
            mov_date = act_dict.get("release_date")
            mov_ovrw = act_dict.get("overview")
            temp_movie = Movie(mov_id,mov_title,mov_date,mov_ovrw)
            movie_list.append(temp_movie)
        return movie_list

            
class data_getter_from_database(Data_Getter):
    def get_actor(self,_id):
        data = api_searchs.search_actor(_id)
        name = data.get('name')
        bio = data.get('biography')
        birth = data.get('birthday')
        death = data.get('deathday')
        actor_search = Actor(_id,name,bio,birth,death)
        return actor_search

    def get_movie_by_id(self,_id):
        data = api_searchs.search_movie_by_id(_id)
        title = data.get('title')
        r_d = data.get('release_date')
        overw = data.get('overview')
        movie_search = Movie(_id,title,r_d,overw)
        return movie_search

    def get_movie_by_title(self,_title):
        movie_l = []
        return movie_l

class database_interaction():
    def actor_insertion(self, _id:str):
        ac_tor = api_s.search_actor(_id)
        print(f'Se insertara a {ac_tor.name}')
        db_w.insert_actor(ac_tor)

    def movie_insertion(self,_id:str):
        mo_vie = api_s.search_movie_by_id(_id)
        print(f'Se insertara {mo_vie.name}')
        db_w.insert_movie(mo_vie)

    def actor_update(self, _actor:Actor):
        db_w.update_actor(_actor)
        pass

    def movie_update(self, _movie:Movie):
        db_w.update_movie(_movie)
        pass

    def actor_delete(self, _id:str):
        db_w.delete_actor(_id)
        pass

    def movie_delete(self, _id:str):
        db_w.delete_actor(_id)
        pass

    def api_to_db_actor(self,csv_file:str):
        id_list = load_ids(csv_file)
        for x in range(len(id_list)):
            data = api_s.search_actor(id_list[x])
            name = data.get('name')
            bio = data.get('biography')
            birth = data.get('birthday')
            death = data.get('deathday')
            actor_search = Actor(id_list[x],name,bio,birth,death)
            db_w.insert_actor(actor_search)
            print(f'Se inserto: {actor_search.name}')
            time.sleep(0.5)
    
    def api_to_db_movie(self,csv_file:str):
        id_list = load_ids(csv_file)
        for x in range(len(id_list)):
            data = api_s.search_movie_by_id(id_list[x])
            title = data.get('title')
            r_d = data.get('release_date')
            overw = data.get('overview')
            movie_search = Movie(id_list[x],title,r_d,overw)
            db_w.insert_movie(movie_search)
            print(f'Se inserto: {movie_search.title}')
            time.sleep(0.5)

def load_ids(csv_path:str):
    charac_list = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        for row in csv_reader:
            charac_list.append(row[0])
    return charac_list


# def main():
#     dga = data_getter_from_api()
#     title = "Spider-Man"
#     movies = dga.get_movie_by_title(title)
#     for x in range(len(movies)):
#         movies[x].show_info()
#         print("\n")

# if __name__ == "__main__":
#     main()