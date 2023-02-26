from midiutil import MIDIFile

# Set the tempo and time signature
tempo = 120
time_signature = (4, 4)

# Create a MIDI file with three tracks
midi = MIDIFile(3)

# Add track names and tempos
for track in range(3):
    midi.addTrackName(track, 0, f"Track {track}")
    midi.addTempo(track, 0, tempo)

# Set the duration of each note
duration = 1

# Add notes to the first track
for i in range(16):
    midi.addNote(0, 0, 60, i * duration, duration, 100)  # C4
    midi.addNote(0, 0, 64, i * duration + duration / 2, duration, 100)  # E4
    midi.addNote(0, 0, 67, i * duration + duration * 3 / 4, duration, 100)  # G4

# Add notes to the second track
for i in range(16):
    midi.addNote(1, 0, 60, i * duration, duration, 60)  # C4
    midi.addNote(1, 0, 64, i * duration + duration / 2, duration, 60)  # E4
    midi.addNote(1, 0, 67, i * duration + duration * 3 / 4, duration, 60)  # G4

# Add notes to the third track
for i in range(16):
    midi.addNote(2, 0, 36, i * duration, duration, 80)  # Bass drum
    midi.addNote(2, 0, 44, i * duration + duration / 2, duration, 80)  # Hi-hat

# Save the MIDI file
with open("beautiful.mid", "wb") as output_file:
    midi.writeFile(output_file)
