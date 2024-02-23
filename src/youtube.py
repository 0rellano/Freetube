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
    
    def get_video_qualities(self):
        qualities = list()
        streams = self.video.streams.filter(type="video")

        for stream in streams:
            if stream.resolution not in qualities:
                qualities.append(stream.resolution)
        
        return sorted(qualities, reverse=True)


    def get_audio_qualities(self):
        qualities = list()
        streams = self.video.streams.filter(type="audio")

        for stream in streams:
            if stream.abr not in qualities:
                qualities.append(stream.abr)
        
        return sorted(qualities, reverse=True, key=lambda x: int(x[:-4]))

    def get_title(self):
        return self.video.title
    
    def get_url_miniature(self):
        return self.video.thumbnail_url
    
    def get_author(self):
        return self.video.author
    
    def get_duration(self):
        return self.video.length
    
    def get_publish_date(self):
        return self.video.publish_date
