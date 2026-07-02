import os
import sys

from chord_scribe.downloader import download_youtube_audio
from chord_scribe.transcriber import transcribe_lyrics_with_timestamps
from chord_scribe.chord_detector import detect_chords_automatically
from chord_scribe.processor import merge_chords_and_lyrics
from chord_scribe.ui import run_interactive_loop

def main():
    print("AI Automatic Lyric & Chord Detector")
    url = input("Enter YouTube Link: ").strip()
    
    audio_file = "downloaded_song.wav"
    try:
        # Pipeline execution across modular elements
        download_youtube_audio(url, audio_file)
        chord_timeline = detect_chords_automatically(audio_file)
        lyric_segments = transcribe_lyrics_with_timestamps(audio_file)
        song_data = merge_chords_and_lyrics(lyric_segments, chord_timeline)
        
        # Pass structured data matrix straight to display interface handler
        run_interactive_loop(song_data)
        
    except Exception as e:
        print(f"\033[91mProcessing execution failure: {e}\033[0m")
        sys.exit(1)
        
    finally:
        # Cleanup temporary media assets
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == "__main__":
    main()
