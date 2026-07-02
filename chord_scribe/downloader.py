import yt_dlp

def download_youtube_audio(url, output_filename="downloaded_song.wav"):
    """Downloads a YouTube video audio track as a high-quality WAV file."""
    print("\n[1/4] Downloading audio from YouTube...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_filename.replace('.wav', '.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return output_filename
