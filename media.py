import webbrowser


class Movie:
    """class storing information about some movies, 
    it will be used to create instances for different movies.

	Args:
        movie_title (str): Movie's title.
        poster_img (str): url of the poster image.
        trailer_url (str): url of the movie's trailer.
    """

    def __init__(self, movie_title, poster_img, trailer_url):
        self.title = movie_title
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        """To open the Trailer in the webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
