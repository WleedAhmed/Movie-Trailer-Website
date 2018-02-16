import webbrowser
class Movie:
	"""This class provides a way to store information about some movies"""
	def __init__(self,movie_title,poster_img,trailer_url):
		self.title = movie_title
		self.poster_image_url = poster_img
		self.trailer_youtube_url = trailer_url


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

