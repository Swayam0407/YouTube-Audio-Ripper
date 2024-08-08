from flask import Flask, request, render_template, send_file
import yt_dlp
import os

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        output_path = 'output_audio.mp3'
        download_youtube_audio(youtube_url, output_path)
        return send_file(output_path, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
