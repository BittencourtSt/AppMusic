from users import USERS

def get_user_music(username):
    return USERS[username]['musicas']

def add_music(username, titulo, artista):
    USERS[username]['musicas'].append({'titulo': titulo, 'artista': artista})

def remove_music(username, titulo):
    USERS[username]['musicas'] = [m for m in USERS[username]['musicas'] if m['titulo'] != titulo]

def edit_music(username, old_titulo, new_titulo, new_artista):
    for m in USERS[username]['musicas']:
        if m['titulo'] == old_titulo:
            m['titulo'] = new_titulo
            m['artista'] = new_artista
            break
