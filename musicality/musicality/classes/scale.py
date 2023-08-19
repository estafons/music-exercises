from musicality.classes.melody import Melody
from musicality.classes.note import Note
class Scale(Melody):
    def __init__(self, root_note, scale_type):
        self.root = Note(root_note)
        self.scale_type = scale_type
        self.notes = []
        self._get_scale()
    
    def _get_scale(self):
        from musicality.constants import SCALES
        scale_pattern = SCALES[self.scale_type]
        scale = [self.root.pitch + semitones for semitones in scale_pattern]
        self.extend(scale)

    def is_tonic(self, note):
        return note.is_octave(self.root)
    
    def is_subtonic(self, note):
        return note.is_octave(self[-1])