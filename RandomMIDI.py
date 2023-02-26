# Install the package: !pip install MIDIUtil

from midiutil import MIDIFile
import random

# Set the tempo and time signature
tempo = 120
time_signature = (4, 4)

# Create a MIDI file with one track
midi = MIDIFile(1)

# Add a track name and tempo
track = 0
midi.addTrackName(track, 0, "Random MIDI")
midi.addTempo(track, 0, tempo)

# Set the duration of each note
duration = 1

# Generate 16 random notes
for i in range(16):
    # Choose a random pitch and velocity
    pitch = random.randint(40, 80)
    velocity = random.randint(80, 127)
    
    # Add the note to the MIDI file
    midi.addNote(track, 0, pitch, i * duration, duration, velocity)

# Save the MIDI file
with open("random.mid", "wb") as output_file:
    midi.writeFile(output_file)
