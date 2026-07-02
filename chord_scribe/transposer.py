CHROMATIC_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def transpose_chord(chord, steps):
    """Shifts a single chord token by a given interval step count."""
    if not chord or chord == "N":
        return ""
    
    is_minor = chord.endswith('m')
    root = chord[:-1] if is_minor else chord
        
    if root not in CHROMATIC_SCALE:
        return chord
        
    current_index = CHROMATIC_SCALE.index(root)
    new_index = (current_index + steps) % 12
    new_root = CHROMATIC_SCALE[new_index]
    
    return f"{new_root}m" if is_minor else new_root

def transpose_song(song_data, steps):
    """Iterates through layout structure elements to transpose all active chord blocks."""
    transposed_song = []
    for line_type, content in song_data:
        if line_type == "chords" and content.strip():
            tokens = content.split('   ')
            transposed_tokens = [transpose_chord(t, steps) for t in tokens]
            transposed_song.append((line_type, "   ".join(filter(None, transposed_tokens))))
        else:
            transposed_song.append((line_type, content))
    return transposed_song
