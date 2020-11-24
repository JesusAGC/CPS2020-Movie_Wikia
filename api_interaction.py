import requests
import json
from abc import abstractmethod, ABCMeta 
import sqlite3
from classes import *
import utilities


global_api_key = utilities.bring_api_key()
sql_connection = sqlite3.connect(utilities.bring_data_base_cstring())
sqlite_cursor = sql_connection.cursor()

class search_interface(metaclass=ABCMeta):
    @abstractmethod
    def search_actor(self,id):
        pass
    @abstractmethod
    def search_movie_by_id(self,id):
        pass
    
class api_searchs(search_interface):
    def search_actor(self, _actorid: str):
        url =   f'https://api.themoviedb.org/3/person/{_actorid}?api_key={global_api_key}&language=en-US'
        print(url + "\n")
        json_obj = requests.get(url)
        data = json.loads(json_obj.content)
        return data
    
    def search_movie_by_title(self, _movie_query:str):
        url = f"https://api.themoviedb.org/3/search/movie?api_key={global_api_key}&query={_movie_query}"
        print(url + "\n")
        json_obj = requests.get(url)
        data = json.loads(json_obj.content)
        return data

    def search_movie_by_id(self, _movie_id:str):
        url = f"https://api.themoviedb.org/3/movie/{_movie_id}?api_key={global_api_key}&language=en-US"
        print(url + "\n")
        json_obj = requests.get(url)
        data = json.loads(json_obj.content)
        return data

class database_searchs(search_interface):
    def search_actor(self, _actorid: str):
        sqlite_cursor.execute(f"SELECT * FROM Actors where ID = ?",(_actorid))
        data = sqlite_cursor.fetchone()
        actor_ret = Actor(data[0],data[1],data[2],data[3],data[4])
        return actor_ret
    
    def search_movie_by_title(self, _movie_query:str):
        sqlite_cursor.execute(f"SELECT * FROM Movie where Title like ?",(_movie_query))
        rows = sqlite_cursor.fetchall()
        movie_list = []
        for row in rows:
            temp_movie = Movie(row[0],row[1],row[2],row[3])
            movie_list.append(temp_movie)
        return movie_list

    def search_movie_by_id(self, _movie_id:str):
        sqlite_cursor.execute(f"SELECT * FROM Movie where ID = {_movie_id}")
        data = sqlite_cursor.fetchone()
        movie_ret = Movie(data[0],data[1],data[2],data[3])
        return movie_ret


class database_workclass():
    
    def insert_actor(self,_actor:Actor):
        try:
            sqlite_cursor.execute(f'INSERT INTO Actors VALUES(?,?,?,?,?)',(_actor.actor_id,_actor.name,_actor.biography,_actor.birth_date,_actor.death_date))
            sql_connection.commit()
        except:
            print(f"Hubo un error al insertar el registro de: {_actor.name}, no se inserto en la BD")
        pass

    def insert_movie(self,_movie:Movie):
        try:
            sqlite_cursor.execute(f'INSERT INTO Movies VALUES(?,?,?,?)',(_movie.movie_id,_movie.title,_movie.date_of_release,_movie.overview))
            sql_connection.commit()
        except:
            print(f"Hubo un error al insertar el registro de: {_movie.title}, no se inserto en la BD")
        pass

    def update_actor(self,_actor:Actor):
        try:
            sqlite_cursor.execute(f'UPDATE Actors SET Name = ?, Biography = ?, Birth_date = ?, Death_date = ? where ID = ?',(_actor.name,_actor.biography,_actor.birth_date,_actor.death_date))
            sql_connection.commit()
        except:
            print(f'Hubo un error al actualizar el registro de: {_actor.name}, no se inserto en la BD')
        pass
    def update_movie(self,_movie:Movie):
        sqlite_cursor.execute(f'UPDATE Movies SET Title = ?,Release_date = ?,Overview = ? where ID = ?',(_movie.title,_movie.date_of_release,_movie.overview,_movie.id))
        sql_connection.commit()
        pass

    def delete_actor(self, _id):
        try:
            sqlite_cursor.execute(f'DELETE FROM Actors where ID = ?',(_id))
            sql_connection.commit()
        except:
            print("Hubo un problema al borrar, probablemente el registro no existe")
        pass
    def delete_movie(self, _id):
        try:
            sqlite_cursor.execute(f'DELETE FROM Movies where ID = ?',(_id))
            sql_connection.commit()
        except:
            print("Hubo un problema al borrar, probablemente el registro no existe")
        pass



# def main():

#     # aps = api_searchs()
#     # data = aps.search_actor("1")
#     # pprint.pprint(data)
#     # name = data.get('name')
#     # bio = data.get('biography')
#     # birth = data.get('birthday')
#     # death = data.get('deathday')
#     # actor_search = Actor("1",name,bio,birth,death)
#     # dbwc = database_workclass()
#     # dbwc.insert_actor(actor_search)
#     # data = aps.search_movie_by_id("101")
#     # title = data.get('title')
#     # r_d = data.get('release_date')
#     # overw = data.get('overview')
#     # movie_search = Movie("101",title,r_d,overw)
#     # pprint.pprint(movie_search.overview)
#     # dbwc.insert_movie(movie_search)

#     # dbi = database_searchs()
#     # le_Actor =dbi.search_actor("1")
#     # print(f"{le_Actor.actor_id} {le_Actor.name} {le_Actor.birth_date} {le_Actor.death_date}")
#     # print(le_Actor.biography)
#     # print("geming")

# if __name__ == "__main__":
#     main()
