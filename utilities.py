import json

def bring_api_key():
    with open('config.json') as json_file:
        data = json.load(json_file)
        api_key = data.get('api_key')
    return api_key

def bring_data_base_cstring():
    with open('config.json') as json_file:
        data = json.load(json_file)
        db_route = data.get('database_route')
    return db_route
