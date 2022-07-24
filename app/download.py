import re, sys
from pytube import YouTube
from clint.textui import colored, puts

def connect_to_youtube():
    url = str(input("Ingrese la url del video que quiere descargar: "))
    if is_url_invalid(url): return None
    yt = YouTube(url=url, on_progress_callback=on_progress_callback)

def download_mp3():
    ...

def download_mp4():
    ...


# TODO: callback
def on_progress_callback(video, chunck, bytes_remaining):
    filesize = video.filesize
    current = ((filesize - bytes_remaining) / filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ {download} |{bar}| {percent}%\r'.format(download=colored.blue("Descargando ..."), bar=status, percent=percent))
    sys.stdout.flush()

# TODO: Validaciones
def is_url_invalid(url: str):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]0,61[A-Z0-9])?.)+[A-Z]2,6.?|'  # domain...
        r'localhost|'  # localhost...
        r'd1,3.d1,3.d1,3.d1,3)' # ...or ip
        r'(?::d+)?'  # optional port
        r'(?:/?|[/?]S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)