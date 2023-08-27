from musicality.classes.note import Note
class Melody:
    def __init__(self, notes=None):
        self.notes = []
        if notes:
            self.extend(notes)

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
    
    def __add__(self, other):
        new_melody = Melody()
        new_melody.extend(self.notes)
        new_melody.extend(other.notes)
        return new_melody
    
    def append(self, note):
        note.index = len(self.notes)
        previous_note = self.get_previous_note(note)
        if self.notes:
            note.time = previous_note.time + previous_note.duration
        else:
            note.time = 0
        self.notes.append(note)

    def extend(self, notes):
        from copy import deepcopy
        notes = deepcopy(notes)
        for note in notes:
            if isinstance(note, Note):

                self.append(note)
            elif isinstance(note, int):
                self.append(Note(
                    note
                ))
            elif isinstance(note, tuple):
                self.append(Note(
                    note[0],
                    note[1]
                ))
            elif isinstance(note, list):
                if isinstance(note[0], int):
                    for n in note:
                        self.append(Note(n))
                elif isinstance(note[0], tuple):
                    for n in note:
                        self.append(Note(
                            n[0],
                            n[1]
                        ))
                elif isinstance(note[0], Note):
                    for n in note:
                        self.append(n)
            else:
                print(note)
                type(note)
                raise TypeError("Invalid type for note")
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

    def genetize_melody(self, scale):
        from musicality.genetic import genetic
        winner, generations = genetic(self.notes, scale)
        print(f"Generations: {generations}")
        print(winner)
        return Melody(winner)
    
    def write_melody(self, filename, track=0, channel=0, tempo=60, volume=100):
        from midiutil import MIDIFile
        MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
        MyMIDI.addTempo(track, 0, tempo)
        for note in self.notes:    
            MyMIDI.addNote(track, channel, note.pitch, note.time, note.duration, volume)
        with open(filename, "wb") as output_file:
            MyMIDI.writeFile(output_file)

    def create_midi(self, track=0, channel=0, tempo=60, volume=100):
        from midiutil import MIDIFile
        MyMIDI = MIDIFile(1)
        MyMIDI.addTempo(track, 0, tempo)
        for note in self.notes:
            MyMIDI.addNote(track, channel, note.pitch, note.time, note.duration, volume)
        return MyMIDI

