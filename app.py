from flask import Flask, render_template, request
from movie import get_movie

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/movie', methods=['POST'])
def movie():
    movie = request.form['movie']

    movie_data = get_movie(movie)

    title = movie_data['Title']
    released = movie_data['Released']
    plot = movie_data['Plot']
    poster = movie_data['Poster']

    return render_template('movie.html', title=title, released=released, plot=plot, poster=poster)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
