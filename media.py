import webbrowser


# VIDEO CLASS
class Video(object):
    '''
    This class provides a way to store Video related information in general.
    '''
    def __init__(self, title, duration, trailer_youtube_url,  poster_image_url, story, **kwargs):
        self.title = title
        self.duration = duration
        self.poster_image_url = poster_image_url
        self.story = story
        self.trailer_youtube_url = trailer_youtube_url

        for key, value in kwargs.items():  # insurance for future keys
            setattr(self, key, value)

    def show_info(self):
        # print(self.title + f' - {title}')
        pass

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# TVSHOW CLASS
class TvShow(Video):
    '''
    This class provides a way to store TvShow related information.
    '''
    def __init__(self,title, duration, poster_image_url, story, season, trailer_youtube_url,**kwargs):
        Video.__init__(self,title, duration, poster_image_url, trailer_youtube_url, story,**kwargs)
        self.season = season
        self.poster_image_url = poster_image_url
        self.story = story
        self.trailer_youtube_url = trailer_youtube_url
        for key, value in kwargs.items():  # insurance for future keys
            setattr(self, key, value)

# MOVIE CLASS
class Movie(Video):
    '''
This class provides a way to store movie related information.
    '''
    VALID_RATINGS = ['G','PG', 'PG-13', 'R']

    def __init__(self,title, duration, poster_image_url, story,trailer_youtube_url,**kwargs):
        Video.__init__(self, title, duration, poster_image_url,story, trailer_youtube_url, **kwargs)
        self.poster_image_url = poster_image_url
        self.story = story
        self.trailer_youtube_url = trailer_youtube_url

        for key, value in kwargs.items():  # insurance for future keys
            setattr(self, key, value)


