from musicality.classes.melody import Melody

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

    def arpeggio(self, inversion, length=3):
        ''' return an arpeggio for a given inversion.
         take into account the possibility that there is not an extended note'''
        if self.extended:
            _simple_arpeggio = [self.root, self.third, self.fifth, self.extended]
        else:
            _simple_arpeggio = [self.root, self.third, self.fifth]
        arpeggio_notes = [_simple_arpeggio[index % len(_simple_arpeggio)] + 12*int(index/len(_simple_arpeggio)) for index in range(inversion, length + inversion)]
        arpeggio = Melody()
        arpeggio.extend(arpeggio_notes)
        return arpeggio
