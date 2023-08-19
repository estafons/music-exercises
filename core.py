from musicality.classes.note import Note
from musicality.classes.melody import Melody
from musicality.classes.scale import Scale







Dnotes = Melody()
Dnotes.extend([
    Note(50, 0.5),
    Note(54, 0.5),
    Note(61, 0.5),
    Note(62, 0.5)
])
if __name__ == "__main__":
    for i in range(1, 10):
        Dscale = Scale(50, "MAJOR_SCALE")
        Dnotes = Melody()
        Dnotes.extend([
        Note(50, 0.5),
        Note(52, 0.5),
        Note(53, 0.5),
        Note(54, 0.5),
        Note(61, 0.5),
        Note(62, 0.5)
        ])
        Dnotes.write_melody("original.mid")
        winner = Dnotes.genetize_melody(Dscale)
        winner.play()
        winner.write_melody("genetic" + str(i) + ".mid")

# 
