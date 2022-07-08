import requests

URL = 'https://pokeapi.co/api/v2/ability/'

def search_poke_ability(search_term='', id=1):

    #Clean the search term

    search_term = str(search_term).strip().lower()

    print (f'Searching for pokemon ability with id {search_term}...', end='')

    header = {'accept' : 'application/json'}

    params = {
        'id': id,
        'term': search_term        
    }
    
    search_url = URL + search_term
    
    resp_msg = requests.get(search_url, headers=header, params=params)

    if resp_msg.status_code == requests.codes.ok:
        print('Success')
        return resp_msg.json()
    else:
        print('Failure')
        print(f'Error Code: {resp_msg.status_code}, Error Reason: {resp_msg.reason}')


poke_dict = search_poke_ability(14)

pass
