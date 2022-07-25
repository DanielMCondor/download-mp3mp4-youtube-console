import re, sys, os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError
from function import BLUE, Color

PATH_SAVE = "/media/daniel/Daniel/personal/"
PATH_MP3 = f"{PATH_SAVE}music"
PATH_MP4 = f"{PATH_SAVE}video"

def connect_to_youtube():
    url = str(input("Ingrese la url del video que quiere descargar: \n>> "))
    if is_url_invalid(url): return None
    yt = YouTube(url=url, on_progress_callback=on_progress_callback)
    return yt

def download_mp3():
    validateYesOrNo = ["s", "n"]
    start = True
    while start:
        try:
            Color.print_info("¿Quieres continuar? (S/N)")
            response = str(input(">> "))
            if not validateYesOrNo.__contains__(response.lower()):
                Color.print_fail("Ingresa una opción válida ...")
                continue
            else:
                start = response.lower() == "s"
                if not start:
                    break

            yt = connect_to_youtube()
            if yt is None: continue
            Color.print_ok("Cargando ...")
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=PATH_MP3)
            base, _ = os.path.splitext(out_file)
            new_file = f"{base}.mp3"
            os.rename(out_file, new_file)
            Color.print_ok(f"{yt.title} se ha descargado con exito.")
            start = False

        except VideoUnavailable:
            Color.print_fail("La url del video no esta disponible ...")
            continue
        except RegexMatchError:
            Color.print_fail("La url ingresada no es válida ...")
            continue

def download_mp4():
    validateYesOrNo = ["s", "n"]
    start = True
    while start:
        try:
            Color.print_info("¿Quieres continuar? (S/N)")
            response = str(input(">> "))
            if not validateYesOrNo.__contains__(response.lower()):
                Color.print_fail("Ingresa una opción válida ...")
                continue
            else:
                start = response.lower() == "s"
                if not start:
                    break

            yt = connect_to_youtube()
            if yt is None: continue
            Color.print_ok("Cargando ...")
            yt.streams.get_highest_resolution().download(output_path=PATH_MP4)
            Color.print_ok(f"{yt.title} se ha descargado con exito.")
            start = False

        except VideoUnavailable:
            Color.print_fail("La url del video no esta disponible ...")
            continue
        except RegexMatchError:
            Color.print_fail("La url ingresada no es válida ...")
            continue

# TODO: callback
def on_progress_callback(video, chunck, bytes_remaining):
    filesize = video.filesize
    current = ((filesize - bytes_remaining) / filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ {download} |{bar}| {percent}%\r'.format(download=BLUE+"Descargando ...", bar=status, percent=percent))
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
