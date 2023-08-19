class Note:
    def __init__(self, pitch, duration=0.5):
        self.pitch = pitch
        self.duration = duration
        self.index = None
        self.time = None

    def __eq__(self, other):
        return self.pitch == other.pitch and self.duration == other.duration # and self.index == other.index and self.time == other.time
    
    def is_octave(self, other):
        return self.pitch % 12 == other.pitch % 12
