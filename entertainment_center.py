#!/usr/bin/python
# -*- coding: utf-8 -*-
# For importing modules in the program

import os

# For setting directory for the module (found on stackoverflow.com)

__path__ = [os.path.dirname(os.path.abspath(__file__))]
from . import media  # class module for Movie
from . import fresh_tomatoes  # template for the webpage

# Iron Man

Iron_Man = media.Movie('Iron Man',
                       'A wealthy American business magnate, playboy,'
                       'and ingenious engineer,Tony Stark suffers a'
                       'severe chest injury during a kidnapping in'
                       ' which...',
                       'https://s-media-cache-ak0.pinimg.com/736x/e5/e8/a7/e5e8a744ab691f61a4afe09bdf36d8aa.jpg',  # noqa
                       'https://www.youtube.com/watch?v=8hYlB38asDY')

# Harry Potter DH part 2

Harry_Potter = media.Movie('Harry Potter ',
                           'Harry, Ron and Hermione face a race against time'
                           ' to destroy the remaining horcruxes',
                           'http://img.moviepostershop.com/harry-potter-and-the-deathly-hallows-part-ii-movie-poster-2011-1010702626.jpg',  # noqa
                           'https://www.youtube.com/watch?v=mObK5XD8udk'
                           )

# Dark_Knight_Rises

Dark_Knight = media.Movie('The Dark Knight Rises',
                          'Bane, an imposing terrorist, attacks Gotham City'
                          ' and disrupts its eight-year-long period of peace',
                          'http://www.moviesonline.ca/wp-content/uploads/2012/07/the-dark-knight-rises-imax.jpeg',  # noqa
                          'https://www.youtube.com/watch?v=g8evyE9TuYk')

# Bahubali 2

Bahubali = media.Movie('Baahubali 2 - The Conclusion',
                       'Kattappa (Sathyaraj) continues to narrate how he ended'
                       ' up killing Amarendra Baahubali (Prabhas)',
                       'https://www.desiretrees.in/wp-content/uploads/2017/02/Baahubali-2-New-Poster-Maha-Shivaratri.jpg',  # noqa
                       'https://www.youtube.com/watch?v=G62HrubdD6o')

# Dhoom 2

Dhoom = media.Movie('Dhoom 2',
                    'Mr. A, a fearless thief, steals valuable artefacts',
                    'http://www.impawards.com/intl/india/2006/posters/dhoom_2_xlg.jpg',  # noqa
                    'https://www.youtube.com/watch?v=gUelnhpgUQ4')

# 3 Idiots

idiots = media.Movie('3 idiots',
                     'In college, Farhan and Raju form a great bond with'
                     'Rancho due to his refreshing outlook. Years later, '
                     'a bet gives them a chance to look for their long-lost'
                     ' friend whose existence seems rather elusive.',
                     'https://images-na.ssl-images-amazon.com/images/M/MV5BZWRlNDdkNzItMzhlZC00YTdmLWIwNjktYjY5NjQ1ZmQ3N2FkXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY1200_CR133,0,630,1200_AL_.jpg',  # noqa
                     'https://www.youtube.com/watch?v=xvszmNXdM4w')

movies = [  # list to pass in the open_movies_page method
    Iron_Man,
    Harry_Potter,
    Dark_Knight,
    Bahubali,
    Dhoom,
    idiots,
]

# exporting the list to template for generating webpage

fresh_tomatoes.open_movies_page(movies)

print(media.__doc__)
