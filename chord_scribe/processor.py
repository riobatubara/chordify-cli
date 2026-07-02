def merge_chords_and_lyrics(lyric_segments, chord_timeline):
    """Combines isolated chord timelines and lyric timestamps into a unified sheet."""
    print("[4/4] Aligning AI chords with lyric timelines...")

    song_structure = [("header", "AI Automatically Generated Chord Sheet")]
    
    for segment in lyric_segments:
        start_time = segment['start']
        end_time = segment['end']
        
        # Filter chords matching current text segment timeline
        chords_in_segment = [
            chord for time, chord in chord_timeline 
            if start_time <= time <= end_time and chord != "N"
        ]
        
        # Strip identical sequential chords to clean up layout presentation
        unique_chords = []
        last_chord = None
        for c in chords_in_segment:
            if c != last_chord:
                unique_chords.append(c)
                last_chord = c
                
        chord_line = "   ".join(unique_chords) if unique_chords else ""
        
        song_structure.append(("chords", chord_line))
        song_structure.append(("text", segment['text']))
        
    return song_structure
