from flask import Flask, render_template, request, redirect, url_for, session, flash
from users import USERS, authenticate
from music import get_user_music, add_music, remove_music, edit_music

app = Flask(__name__)
app.secret_key = 'chave_supersecreta'

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('user_home'))
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if authenticate(username, password):
        session['username'] = username
        return redirect(url_for('user_home'))
    flash('Usuário ou senha incorretos.')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/home')
def user_home():
    if 'username' not in session:
        return redirect(url_for('index'))
    musicas = get_user_music(session['username'])
    return render_template('user_home.html', musicas=musicas)

@app.route('/musicas')
def music_page():
    if 'username' not in session:
        return redirect(url_for('index'))
    musicas = get_user_music(session['username'])
    return render_template('music.html', musicas=musicas)

@app.route('/musicas/add', methods=['POST'])
def add_musica():
    if 'username' in session:
        titulo = request.form['titulo']
        artista = request.form['artista']
        add_music(session['username'], titulo, artista)
    return redirect(url_for('music_page'))

@app.route('/musicas/remove', methods=['POST'])
def remove_musica():
    if 'username' in session:
        titulo = request.form['titulo']
        remove_music(session['username'], titulo)
    return redirect(url_for('music_page'))

@app.route('/musicas/edit', methods=['POST'])
def edit_musica():
    if 'username' in session:
        old_titulo = request.form['old_titulo']
        new_titulo = request.form['new_titulo']
        new_artista = request.form['new_artista']
        edit_music(session['username'], old_titulo, new_titulo, new_artista)
    return redirect(url_for('music_page'))

@app.route('/musicas/search')
def search_musica_page():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('search_music.html', musicas=None)

@app.route('/musicas/search', methods=['POST'])
def search_musica():
    if 'username' not in session:
        return redirect(url_for('index'))
    
    termo = request.form['termo'].lower()
    todas_musicas = get_user_music(session['username'])
    filtradas = [m for m in todas_musicas if termo in m['titulo'].lower() or termo in m['artista'].lower()]
    return render_template('search_music.html', musicas=filtradas, termo=termo)

if __name__ == '__main__':
    app.run(debug=True)
