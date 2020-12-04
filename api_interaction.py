from os import name
import requests
import json
from abc import abstractmethod, ABCMeta 
import sqlite3
from classes import *
import utilities


global_api_key = utilities.bring_api_key()
sql_connection = sqlite3.connect(utilities.bring_data_base_cstring())
sqlite_cursor = sql_connection.cursor()


not_found_actor = Actor('0','Not found','No data','No data','No data')
not_found_movie = Movie('0','Not found','No data','No data')

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
        try:
            sqlite_cursor.execute(f"SELECT * FROM Actors where ID = ?",(_actorid,))
            data = sqlite_cursor.fetchone()
            if data == None:
                return not_found_actor
            else:
                return Actor(data[0],data[1],data[2],data[3],data[4])
        except Exception as e:
            print('Sucedio un error al consultar, el error es: \n'+str(e))
    
    def search_movie_by_title(self, _movie_query:str):
        query=f'SELECT * FROM Movies where Title like "%{_movie_query}%"'
        try:
            sqlite_cursor.execute(query)
            rows = sqlite_cursor.fetchall()
            if rows != None:
                movie_list = []
                for row in rows:
                    temp_movie = Movie(row[0],row[1],row[2],row[3])
                    movie_list.append(temp_movie)
                return movie_list
            else:
                return not_found_movie
        except Exception as e:
            print('Sucedio un error al consultar, el error es: \n'+str(e))

    def search_movie_by_id(self, _movie_id:str):
        try:
            sqlite_cursor.execute(f"SELECT * FROM Movies where ID = {_movie_id}")
            data = sqlite_cursor.fetchone()
            if data != None:
                movie_ret = Movie(data[0],data[1],data[2],data[3])
                return movie_ret
            else: 
                return not_found_movie
        except Exception as e:
            print('Sucedio un error al consultar, el error es: \n'+str(e))


    def get_all_actors(self):
        try:
            sqlite_cursor.execute(f"SELECT * FROM Actors")
            rows = sqlite_cursor.fetchall()
            actor_list = []
            if rows != None:
                for row in rows:
                    temp_actor = Actor(row[0],row[1],row[2],row[3],row[4])
                    actor_list.append(temp_actor)
                return actor_list
            else:
                return not_found_actor
        except Exception as e:
            print('Sucedio un error al consultar, el error es: \n'+str(e))
    
    def get_all_movies(self):
        try:
            sqlite_cursor.execute(f"SELECT * FROM Movies")
            rows = sqlite_cursor.fetchall()
            movie_list = []
            if rows != None:
                for row in rows:
                    temp_movie = Movie(row[0],row[1],row[2],row[3])
                    movie_list.append(temp_movie)
                return movie_list
            else:
                return not_found_movie
        except Exception as e:
            print('Sucedio un error al consultar, el error es: \n'+str(e))


class database_workclass():
    
    def insert_actor(self,_actor:Actor):
        try: 
            if str(_actor.name) == 'None' or str(_actor.name) == None:
                print(f'No se insertó el registro porque no tiene contenido. ID = {_actor.actor_id}\n')
                
            else:
                sqlite_cursor.execute(f'INSERT INTO Actors VALUES(?,?,?,?,?)',(_actor.actor_id,_actor.name,_actor.biography,_actor.birth_date,_actor.death_date))
                sql_connection.commit()
        except Exception as e:
            if str(e) == 'UNIQUE constraint failed: Actors.ID':
                print(f'El registro {_actor.actor_id} - {_actor.name} ya esta en la base de datos, no se inserto de nuevo\n')
            else:
                print(f"Hubo un error al insertar el registro de: {_actor.name}, no se inserto en la BD\n")
                print(f'El error fue:\n{e}')
        pass

    def insert_movie(self,_movie:Movie):
        try:
            if str(_movie.title) != 'None' or str(_movie.title) != 'None':
                sqlite_cursor.execute(f'INSERT INTO Movies VALUES(?,?,?,?)',(_movie.movie_id,_movie.title,_movie.date_of_release,_movie.overview))
                sql_connection.commit()
            else:
                print(f'No se insertó el registro porque no tiene contenido. ID = {_movie.movie_id}\n')
        except Exception as e:
            if str(e) == 'UNIQUE constraint failed: Movies.ID':
                print(f'El registro {_movie.movie_id} - {_movie.title} ya esta en la base de datos, no se inserto de nuevo\n')
            else:
                print(f"Hubo un error al insertar el registro de: {_movie.title}, no se inserto en la BD\n")
                print(f'El error fue:\n{e}')
        pass

    def update_actor(self,_actor:Actor):
        try:
            sqlite_cursor.execute(f'UPDATE Actors SET Name = ?, Biography = ?, Birth_date = ?, Death_date = ? where ID = ?',(_actor.name,_actor.biography,_actor.birth_date,_actor.death_date,_actor.actor_id))
            sql_connection.commit()
        except Exception as e:
            print(f'Hubo un error al actualizar el registro de: {_actor.name}, no se inserto en la BD, el error es:')
            print(e)
        pass
    def update_movie(self,_movie:Movie):
        try:
            sqlite_cursor.execute(f'UPDATE Movies SET Title = ?,Release_date = ?,Overview = ? where ID = ?',(_movie.title,_movie.date_of_release,_movie.overview,_movie.movie_id))
            sql_connection.commit()
        except Exception as e:
            print(f'Hubo un error al actualizar el registro de: {_movie.title}, no se inserto en la BD, el error es:')
            print(e)

    def delete_actor(self, _id):
        try:
            sqlite_cursor.execute(f'DELETE FROM Actors where ID = ?',(_id,))
            sql_connection.commit()
            print(f'Se elimino el actor con el ID: {_id}')
        except Exception as e:
            print("Hubo un problema al borrar, el error es:")
            print(e)
        pass

    def delete_movie(self, _id):
        try:
            sqlite_cursor.execute(f'DELETE FROM Movies where ID = ?',(_id,))
            sql_connection.commit()
            print(f'Se elimino la película con el ID: {_id}')
        except Exception as e:
            print("Hubo un problema al borrar, el error es:")
            print(e)
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
