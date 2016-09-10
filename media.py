import webbrowser

class Movie():

    def __init__(self, title, storyline, poster_image_url, youtube_trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.youtube_trailer_url = youtube_trailer_url

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
