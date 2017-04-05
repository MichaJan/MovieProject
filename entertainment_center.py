import fresh_tomatoes
import media

# Creating specific instances of classes patterns from media
toy_story = media.Movie(title='Toy Story',
                        poster_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Toy_Story.svg/375px-Toy_Story.svg.png",
                        story ='Story of a boy and his toys that came alive',
                        trailer_youtube_url = "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        duration=148)

avatar = media.Movie(title ='Avatar',
                     poster_image_url = "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     story = 'Story of a marine who falls in love with an alien',
                     trailer_youtube_url = "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     duration = 148)
school_of_rock = media.Movie(title ='School of Rock',
                             poster_image_url = "https://adammarxsmind.files.wordpress.com/2015/03/2003_the_school_of_rock_wallpaper_002.jpg",
                             story = 'Story of failed rock star who starts a rock band in a classroom',
                             trailer_youtube_url = "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
                             duration = 148
                             )

matrix = media.Movie(title ='Matrix',
                     poster_image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                     story = 'We live in a fictional world created by computers. What happens when we wake up?',
                     trailer_youtube_url = "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                     duration = 148
                     )

pirates_of_carribean_2 = media.Movie(title ='Pirates of Carribean',
                                     poster_image_url = "https://i.jeded.com/i/pirates-of-the-caribbean-2-dead-mans-chest.10847.jpg",
                                     story = 'Story a pirate who needs to decide what is more important. His life or his friends.',
                                     trailer_youtube_url = "https://www.youtube.com/watch?v=XN3omw9o0Jk",
                                     duration = 148
                                     )
inception = media.Movie(title ='Inception',
                        poster_image_url = "http://www.impawards.com/2010/posters/inception.jpg",
                        story = 'Story of a man who ventures into people\'s dreams',
                        trailer_youtube_url = "https://www.youtube.com/watch?v=d3A3-zSOBT4",
                        duration = 148
                        )
lost = media.TvShow(title ='Lost',
                    poster_image_url='''
http://vignette3.wikia.nocookie.net/lostpedia/images/9/9a/PosterTwo.jpg/revision/latest?cb=20100916012434
''',
                    story = 'After a planecrash a group of survivors find themselves stranded on a mysterious island.',
                    duration = 60,
                    trailer_youtube_url = 'https://www.youtube.com/watch?v=KTu8iDynwNc',
                    season = 6)


# A list of previous class instances
movies = [inception,pirates_of_carribean_2,matrix,avatar,school_of_rock,toy_story,lost]

#  Will execute creation of HTML file and opening the browser window.
fresh_tomatoes.open_movies_page(movies)

