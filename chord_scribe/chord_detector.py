import librosa
import numpy as np

CHROMATIC_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def detect_chords_automatically(audio_path):
    """Analyzes audio frequencies and maps estimated chords over time."""
    print("[3/4] Analyzing audio frequencies for Automatic Chord Detection...")
    
    y, sr = librosa.load(audio_path, sr=22050)
    chroma = librosa.feature.chroma_cens(y=y, sr=sr)
    
    # Sync analysis frames to detected musical beats
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_chroma = librosa.util.sync(chroma, beat_frames, aggregate=np.median)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    
    # Chord Templates (Binary representations of notes)
    major_template = np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])
    minor_template = np.array([1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0])
    
    detected_chords = []
    
    for i in range(beat_chroma.shape[1]):
        chroma_vector = beat_chroma[:, i]
        best_score = -1
        best_chord = "N"
        
        for note_idx in range(12):
            maj_shifted = np.roll(major_template, note_idx)
            min_shifted = np.roll(minor_template, note_idx)
            
            maj_score = np.dot(chroma_vector, maj_shifted)
            min_score = np.dot(chroma_vector, min_shifted)
            
            if maj_score > best_score:
                best_score = maj_score
                best_chord = CHROMATIC_SCALE[note_idx]
            if min_score > best_score:
                best_score = min_score
                best_chord = CHROMATIC_SCALE[note_idx] + "m"
                
        detected_chords.append((beat_times[i], best_chord))
        
    return detected_chords
