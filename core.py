from midiutil import MIDIFile

class Note:
    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration
        self.index = None
        self.time = None

class Melody:
    def __init__(self):
        self.notes = []

    def __len__(self):
        return len(self.notes)

    def __getitem__(self, index):
    
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            sliced_notes = [self.notes[i] for i in range(start, stop, step)]
            sub_melody = Melody()
            sub_melody.notes = sliced_notes
            return sub_melody
        else:
            return self.notes[index]

    def __reversed__(self):
        return reversed(self.notes)
    
    def append(self, note):
        note.index = len(self.notes)
        previous_note = self.get_previous_note(note)
        if self.notes:
            note.time = previous_note.time + previous_note.duration
        else:
            note.time = 0
        self.notes.append(note)

    def extend(self, notes):
        for note in notes:
            self.append(note)

    def insert(self, index, note):
        self.notes.insert(index, note)
        self.reindex()

    def reindex(self):
        for index, note in enumerate(self.notes):
            note.index = index

        for index, note in enumerate(self.notes):
            previous_note = self.get_previous_note(note)
            if index > 0:
                note.time = previous_note.time + previous_note.duration
            else:
                note.time = 0

    def get_previous_note(self, note):
        if note.index > 0:
            return self.notes[note.index - 1]
        else:
            return None

    def get_next_note(self, note):
        if note.index < len(self.notes) - 1:
            return self.notes[note.index + 1]
        else:
            return None

    def play(self):
        for note in self.notes:
            print(f"Playing {note.pitch} for {note.duration} seconds at {note.time} ")

    def create_nths_melody(self, n, step):
        from copy import deepcopy
        new_melody = Melody()

        # Forward part of the pattern
        for i in range(0, len(self) - n + 1, step):
            notes_chunk = deepcopy(self[i:i + n])
            new_melody.extend(notes_chunk)
            
        for i in range(len(self) - n, -1, -step):
            notes_chunk = reversed(deepcopy(self[i:i + n]))
            new_melody.extend(notes_chunk)
        
        new_melody.reindex()
        return new_melody

    def create_nths_melody_backwards(self, n):
        from copy import deepcopy
        new_melody = Melody()

        # Backward part of the pattern
        for i in range(0, len(self) - n + 1):
            notes_chunk = reversed(deepcopy(self[i:i + n]))
            new_melody.extend(notes_chunk)
        for i in range(len(self) - n, -1, -1):
            notes_chunk = deepcopy(self[i:i + n])
            new_melody.extend(notes_chunk)

        new_melody.reindex()
        return new_melody
    
    def melodic_pattern(self, pattern):
        from itertools import cycle
        new_melody = Melody()
        for note, duration in zip(self, cycle(pattern)):
            new_melody.append(Note(
                note.pitch,
                duration
            ))
        return new_melody

    def write_melody(self, filename):
        MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
        MyMIDI.addTempo(track, time, tempo)
        for note in self.notes:    
            MyMIDI.addNote(track, channel, note.pitch, note.time, note.duration, volume)
        with open(filename, "wb") as output_file:
            MyMIDI.writeFile(output_file)

class Chord:
    def __init__(self, root_note, chord_type, extension=None):
        self.root = root_note
        self.chord_type = chord_type
        self.extension = extension
        self.third = self.get_third()
        self.fifth = self.get_fifth()
        self.extended = self.get_extended()

    def get_third(self):
        if self.chord_type == "major":
            return self.root + 4
        elif self.chord_type == "minor" or self.chord_type == "diminished":
            return self.root + 3

    def get_fifth(self):
        if self.extension == "diminished":
            return self.root + 6
        return self.root + 7
    
    def get_extended(self):
        if self.extension == "seventh":
            return self.root + 10
        elif self.extension == "diminished":
            return self.root + 9

    def arpeggio(self, inversion):
        import itertools
        ''' return an arpeggio for a given inversion.
         take into account the possibility that there is not an extended note'''
        if self.extended:
            arpeggio = [self.root, self.third, self.fifth, self.extended]
        else:
            arpeggio = [self.root, self.third, self.fifth]
        inverted_arpeggio = [arpeggio[index % len(arpeggio)] + 12*int(index/len(arpeggio)) for index in range(inversion, len(arpeggio) + inversion)]
        return inverted_arpeggio

majorChord = Chord(60, "major")
print(majorChord.arpeggio(0))
print(majorChord.arpeggio(1))
print(majorChord.arpeggio(2))
print(majorChord.arpeggio(6))
# Example usage
original_melody = Melody()
degrees  = [40, 42, 44, 45, 47, 49, 51, 52] # MIDI note number
track    = 0
channel  = 0
time     = 0   # In beats
duration = 1   # In beats
tempo    = 60  # In BPM
volume   = 100 
original_melody.extend([
    Note(40, 0.5),
    Note(42, 0.5),
    Note(44, 0.5),
    Note(45, 0.5),
    Note(47, 0.5),
    Note(49, 0.5),
    Note(51, 0.5),
    Note(52, 0.5)
])
original_melody.write_melody("original.mid")
# print(original_melody.notes.indices(0, len(original_melody), 1))
new_melody = original_melody.create_nths_melody(3, 2)


# new_melody.play()
new_melody.write_melody("new.mid")

pattern = [1, 0.5, 0.5, 0.5, 0.5, 1]
melodic_pattern = new_melody.melodic_pattern(pattern)

melodic_pattern.play()
melodic_pattern.write_melody("melodic_pattern.mid")

