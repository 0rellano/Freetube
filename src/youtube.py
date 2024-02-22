from pytube import YouTube, exceptions

class YoutubeVideo():

    def __init__(self, url: str):
        self.url_video = url
        self.fetch_video()

    def fetch_video(self):
        try:
            self.video = YouTube(self.url_video)
            self.video.streams
        except exceptions.RegexMatchError:
            raise ValueError("Url no reconocida")
        except exceptions.VideoUnavailable:
            raise ValueError("Video no disponible")
        except exceptions.ExtractError:
            raise ValueError("Error al extraer informacion del video")