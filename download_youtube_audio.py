import yt_dlp
from pydub import AudioSegment
import os

def download_youtube_audio(url, output_path='audio.mp3'):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


    os.rename('temp_audio.mp3', output_path)
    print(f"Audio saved as {output_path}")

# Example usage
youtube_url = 'https://www.youtube.com/watch?v=Eo-KmOd3i7s'
download_youtube_audio(youtube_url, 'output_audio.mp3')
