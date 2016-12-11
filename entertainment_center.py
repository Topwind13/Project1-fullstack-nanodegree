import fresh_tomatoes
import media
"""project 1: Movie trailer website

Description: this file storages the list of the movies and executes fresh_tomatoes.py file in order to open the website in the browser.

"""
# list of movies
toy_story = media.Movie(
    'Toy Story',
    'a boy with life toy',
    'https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg',
    'https://youtu.be/KYz2wyBy3kc')

who_am_i = media.Movie(
    'Who Am I',
    'hacker',
    'https://upload.wikimedia.org/wikipedia/en/5/5c/Who_am_I_movie_poster.jpg',
    'https://youtu.be/5vnjheCqRIs')

interstellar = media.Movie(
    'Interstellar',
    'American epic science fiction film ',
    'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
    'https://youtu.be/0vxOhd4qlnA')

# storage movies to the list for fresh_tomatoes library
movies = [toy_story, who_am_i, interstellar]

# executes function from fresh_tomatoes.py to open the website
fresh_tomatoes.open_movies_page(movies)
