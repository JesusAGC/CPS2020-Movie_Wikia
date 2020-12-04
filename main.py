from comms_area import *
from classes import Actor, Movie


def look_up_actor(_id, dga:data_getter_from_api):
    actor_search = dga.get_actor(_id)
    actor_search.show_info()

def look_up_movie(_id, dga:data_getter_from_api):
    movie_search = dga.get_movie(_id)
    movie_search.show_info()

def look_up_movie_by_title(title:str, dga:data_getter_from_api):
    title = title.replace(" ","-")
    movie_title_search = []
    movie_title_search = dga.get_movie_by_title(title)
    for x in range(len(movie_title_search)):
        movie_title_search[x].show_info()
        print("\n")


def look_up_actor_local(_id, dgd:data_getter_from_database):
    actor_search = dgd.get_actor(_id)
    actor_search.show_info()

def look_up_movie_local(_id, dgd:data_getter_from_database):
    movie_search = dgd.get_movie_by_id(_id)
    movie_search.show_info()

def look_up_movie_by_title_local(title:str, dgd:data_getter_from_database):
    movie_title_search = []
    movie_title_search = dgd.get_movie_by_title(title)
    for x in range(len(movie_title_search)):
        movie_title_search[x].show_info()
        print("\n")

def look_up_all_actors_local(dgd:data_getter_from_database):
    all_actors_db = dgd.get_all_actors_from_db()
    for x in range(len(all_actors_db)):
        all_actors_db[x].show_info()
        print("\n")

def look_up_all_movies_local(dgd:data_getter_from_database):
    all_movies_db = dgd.get_all_movies_from_db()
    for x in range(len(all_movies_db)):
        all_movies_db[x].show_info()
        print("\n")



def insert_actor_locally(_id:str, dgw:database_interaction):
    dgw.actor_insertion(_id)

def insert_movie_locally(_id:str, dgw:database_interaction):
    dgw.movie_insertion(_id) 

def update_actor_locally(_actor:Actor, dbi:database_interaction):
    dbi.actor_update(_actor)
    pass

def update_movie_locally(_movie:Movie, dbi:database_interaction):
    dbi.movie_update(_movie)
    pass

def delete_actor_locally(_id:str, dbi:database_interaction):
    dbi.actor_delete(_id)
    pass

def delete_movie_locally(_id:str, dbi:database_interaction):
    dbi.movie_delete(_id)
    pass

def scrap_csv_file_actor(fpath:str, dbi : database_interaction):
    dbi.api_to_db_actor(fpath) 

def scrap_csv_file_movies(fpath:str,dbi:database_interaction):
    dbi.api_to_db_movie(fpath)
    

def main():
    active = True
    while active:
        # print("Por favor introduzca un nombre de usuario:")
        # user_name = input() 
        print('\n')
        print("Bienvenido a la wiki de actores y peliculas en terminal, las opciones de lo que puede hacer son:")
        print('Busqueda en la api:')
        print("1 Consulte un actor\n2 Consulte una pelicula\n3 Consulte peliculas por titulo\n")
        print('Busqueda en BD local:')
        print("4 Consulte un actor\n5 Consulte una pelicula\n6 Consulte peliculas por titulo")
        print('17 Mostrar todos los actores\n18 Mostrar todas la películas\n')
        print('Edicion de BD local:')
        print("7 Insert manual de actor\n8 Insert manual de pelicula\n9 Editar la informacion de un actor\n10 Editar la informacion de una pelicula\n11 Eliminar un actor de la bd\n12 Eliminar una pelicula de la bd")
        print('Scrapeo:')
        print('19 Insert masivo de actores con csv\n20 Insert masivo de peliculas con csv ')
        print('21 Salir del software\n')
        option = int(input())
        if option == 1:
            print("Escriba el id del actor")
            _id = str(input())
            d_g_a =data_getter_from_api()
            look_up_actor(_id,d_g_a)
        elif option == 2:
            print("Escriba el id de la pelicula")
            _id = str(input())
            d_g_a = data_getter_from_api()
            look_up_movie(_id,d_g_a)
        elif option == 3:
            print("Escriba el titulo a buscar")
            title = str(input())
            d_g_a =data_getter_from_api()
            look_up_movie_by_title(title,d_g_a)
        elif option == 4:
            print("Escriba el id del actor")
            _id = str(input())
            d_g_d = data_getter_from_database()
            look_up_actor_local(_id,d_g_d)
        elif option == 5:
            print("Escriba el id de la pelicula")
            _id = str(input())
            d_g_d = data_getter_from_database()
            look_up_movie_local(_id,d_g_d)
        elif option == 6:
            print('Escriba el titulo de la pelicula')
            title = str(input())
            d_g_d = data_getter_from_database()        
            look_up_movie_by_title_local(title,d_g_d)
        elif option == 7:
            print("Escriba el id del actor a insertar desde api")
            _id = str(input())
            d_b_i = database_interaction()
            insert_actor_locally(_id,d_b_i)
        elif option == 8:
            print("Escriba el id de la pelicula a insertar desde api")
            _id = str(input())
            d_b_i = database_interaction()
            insert_movie_locally(_id,d_b_i)
        elif option == 9:
            print("Escriba los datos del actor a editar")
            print('ID del actor:')
            _id = str(input())
            print('Nuevo nombre del actor:')
            name = str(input())
            print('Nueva Bio del actor:')
            bio = str(input())
            print('Nueva fecha de nacimiento del actor:')
            bd = str(input())
            print('Nueva fecha de defunción del actor:')
            dd = str(input())
            d_b_i = database_interaction()
            update_actor_locally(Actor(_id,name,bio,bd,dd),d_b_i)
        elif option == 10:
            print("Escriba los datos de la pelicula a editar")
            print('ID de la película:')
            _id = str(input())
            print('Nuevo título de la película:')
            title = str(input())
            print('Nueva fecha de lanzamiento de la película:')
            release = str(input())
            print('Nueva descripción de la película:')
            overv = str(input())
            d_b_i = database_interaction()
            update_movie_locally(Movie(_id,title,release,overv),d_b_i)
        elif option == 11:
            print("Escriba el id del actor a borrar")
            _id = str(input())
            d_b_i = database_interaction()
            delete_actor_locally(_id,d_b_i)
        elif option == 12:
            print("Escriba el id de la pelicula a borrar")
            _id = str(input())
            d_b_i = database_interaction()
            delete_movie_locally(_id,d_b_i)
        elif option == 19:
            print("Se cargarán actores desde la api con el csv que de a continuacion")
            file_path = str(input())
            dbi = database_interaction()
            scrap_csv_file_actor(file_path,dbi)
        elif option == 20:
            print("Se cargarán pelis desde la api con el csv que de a continuacion")
            file_path = str(input())
            dbi = database_interaction()
            scrap_csv_file_movies(file_path,dbi)
        elif option == 21:
            active = False
        elif option == 17:
            d_g_d = data_getter_from_database()
            look_up_all_actors_local(d_g_d)
        elif option == 18:
            d_g_d = data_getter_from_database()
            look_up_all_movies_local(d_g_d)
        else:
            print("Opción no existente")
        

if __name__ == "__main__":
   main()
