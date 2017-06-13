
"""
 This class module gives all the information of the instance created for a movie.
		
		Attributes:
			movie_title: It is the title of the movie.
			movie_storyline: It is the description of the movie.
			poster_image: It is the art or poster of the movie.
			trailer_youtube: It is the video of the trailer for the movie.
"""
import webbrowser
class Movie():

    
       
        def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
            """Constructor of the class."""
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube
            
        def show_trailer(self):
           """It is a method which opens the trailer of the movie in a browser window."""
           webbrowser.open(self.trailer_youtube_url)