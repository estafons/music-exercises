# Overview

This repo holds a PoC for writting a tool to generate music excercises ideas.

For an easy to run CLI for this package checkout: https://github.com/estafons/musicality-cli

### Given an initial idea (melody) we can:

- Play "nths'" (sixteenth's, triplets etc). 
    For example given a melody: C, D, E, F, G, A. If we apply the triplets it will become:
    C, D, E, D, E, F, E, F, G, F, G, A, A, G, F, G, F, E, F, E, D, E, D, C

- Change the rythmic pattern of the initial idea. For example we could provide [1, 1/2, 1/2, 1]
    In this case we will change the duration of the first note to a whole the second note to a half and so on. When the pattern "runs out" it simply cycles and start at the begging! So in our example the 5th notes duration would be a whole.

### Arpeggios:

- Given a root note and chord type we can create arpeggios for that chord. For example:
    ```
    DmajorChordArpeg = Chord(50, "major").arpeggio(inversion=0, length=5)
    GminorChordArpeg = Chord(55, "minor").arpeggio(1, 5)
    AmajorChordArpeg = Chord(57, "major").arpeggio(2, 5)
    chordArpegios = DmajorChordArpeg + GminorChordArpeg + AmajorChordArpeg
    chordArpegios.write_melody("chordArpegios.mid")
    ```
    arpeggio on a Chord object takes as input the inversion (any int. If greater than 3 then it starts from the octave + the inversion) and the length of the arpegio to create. 

    Run it to see what happens!

### Genetic Algorithm Generation

- Given an initial idea, we have implemented a genetic algorithm to output a new idea. We aim to generate small patterns that can then be *chained* and altered to create novel excercises on the fly. We should aim at the **musicality** of the outcome.

# Ideas

## Random rythmic patterns
- Add a random pattern function that takes as input a time signature and then returns a random rythmic pattern that fits in it.

## Arpeggios
- Given a list of notes, return an arpeggio for each note starting from that note. For example:
    given note sequence D, B, G
    Returns: D, F#, A, B, M G, G, B, D. This corresponds to Dmajor, E minor and Gmajor (This could be part of Dmajor scale)

    NOTE: Partially implemented. See Arpeggios section for more.

- Expand the above to include major 7ths, minor 7ths and diminished chords. 

- Do the above with respect to some scale. So this would be a two step process:
    i)Chose a probable scale given a list of notes,
    ii) return the list of arpeggios for that scale as well as the scale you chose. 

    NOTE: This should also have an option to provide a scale as well with the notes.
    
