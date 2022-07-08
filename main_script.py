from pokeapi import search_poke_ability
from pastebin_api import post_new_paste
from sys import argv

def main():
    search_term = argv[1]

    poke_dict = search_poke_ability(search_term)

    if poke_dict:
        paste_title = get_paste_title(search_term)

        paste_body = get_paste_body(search_term)

        paste_url = post_new_paste(paste_title, paste_body, '1W')

        print(paste_url)


def get_paste_body(poke_dict):

    pokemon_list = [p['results'] for p in poke_dict['results']]
    paste_body = '\n\n'.join(pokemon_list)
    return paste_body
    
def get_paste_title(search_term):
    return f'Info on {search_term}'

main()