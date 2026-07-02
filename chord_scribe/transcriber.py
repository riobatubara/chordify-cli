import whisper

def transcribe_lyrics_with_timestamps(audio_path, model_size="tiny"):
    """Transcribes text and returns structural timestamps using Whisper AI."""
    print(f"[2/4] Running Whisper AI ({model_size}) to map lyric segments...")

    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    
    segments = []
    for seg in result['segments']:
        segments.append({
            'start': seg['start'],
            'end': seg['end'],
            'text': seg['text'].strip()
        })

    return segments
