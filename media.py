import webbrowser

class Movie():
    """A Movie class contains certain pieces of information about a movie

    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Constructor of Movie class

        Args:
            movie_title (str): the movie title
            movie_storyline (str): a description of a movie
            poster_image (str): a url of image
            trailer_youtube (str): a url of a movie trailer

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        """show a movie trailer
        """
        webbrowser.open(self.trailer_youtube_url)
