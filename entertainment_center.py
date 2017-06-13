import os                                                   # For importing modules in the program              
__path__=[os.path.dirname(os.path.abspath(__file__))]       # For setting directory for the module (found on stackoverflow.com)
from . import media           # class module for Movie
from . import fresh_tomatoes  # template for the webpage


# Iron Man
Iron_Man = media.Movie("Iron Man",
                        'A wealthy American business magnate, playboy, and ingenious engineer,Tony Stark suffers a severe chest injury during a kidnapping in which... ',
                        "https://s-media-cache-ak0.pinimg.com/736x/e5/e8/a7/e5e8a744ab691f61a4afe09bdf36d8aa.jpg",
						"https://www.youtube.com/watch?v=8hYlB38asDY")

# Harry Potter DH part 2
Harry_Potter = media.Movie("Harry Potter ",
						   'Harry, Ron and Hermione face a race against time to destroy the remaining horcruxes',
                        "http://img.moviepostershop.com/harry-potter-and-the-deathly-hallows-part-ii-movie-poster-2011-1010702626.jpg",
						"https://www.youtube.com/watch?v=mObK5XD8udk")

# Dark_Knight_Rises
Dark_Knight = media.Movie("The Dark Knight Rises",
                       'Bane, an imposing terrorist, attacks Gotham City and disrupts its eight-year-long period of peace',
                        "http://www.moviesonline.ca/wp-content/uploads/2012/07/the-dark-knight-rises-imax.jpeg",
						"https://www.youtube.com/watch?v=g8evyE9TuYk")


movies = [Iron_Man,Harry_Potter,Dark_Knight,Harry_Potter,Dark_Knight,Iron_Man]  # list to pass in the open_movies_page method

fresh_tomatoes.open_movies_page(movies)       # exporting the list to template for generating webpage



print(media.__doc__)
