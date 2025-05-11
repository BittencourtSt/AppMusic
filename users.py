USERS = {
    'samara': {'password': '0228', 'musicas': []},
    'holly': {'password': '0405', 'musicas': []}
}

def authenticate(username, password):
    user = USERS.get(username)
    return user and user['password'] == password
