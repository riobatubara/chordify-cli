from .transposer import transpose_song

def display_song(song_data):
    """Clears layout space and renders formatted visual lines in the Terminal console."""
    print("\n" + "="*60)
    for line_type, content in song_data:
        if line_type == "header":
            print(f"\n\033[1;33m[{content}]\033[0m")
        elif line_type == "chords" and content.strip():
            print(f"\033[1;36m{content}\033[0m") 
        elif line_type == "text":
            print(content)
    print("="*60 + "\n")

def run_interactive_loop(song_data):
    """Starts execution command listener for interactive transposing manipulation."""
    current_key_offset = 0
    while True:
        current_song = transpose_song(song_data, current_key_offset)
        display_song(current_song)
        
        print(f"Current Transposition: {current_key_offset} semitones")
        print("Commands: Enter an integer to shift keys (e.g. '3', '-2'). Type 'exit' to quit.")
        
        user_command = input("\nEnter command: ").strip().lower()
        if user_command == 'exit':
            print("Exiting application. Goodbye!")
            break
        try:
            current_key_offset += int(user_command)
        except ValueError:
            print("\033[91mPlease enter a valid shift number or 'exit'.\033[0m")
