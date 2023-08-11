# Overview

This repo holds a PoC for writting a tool to generate music excercises ideas.

Given an initial idea (melody) we can:

- Play "nths'" (sixteenth's, triplets etc). 
    For example given a melody: C, D, E, F, G, A. If we apply the triplets it will become:
    C, D, E, D, E, F, E, F, G, F, G, A, A, G, F, G, F, E, F, E, D, E, D, C

- Change the rythmic pattern of the initial idea. For example we could provide [1, 1/2, 1/2, 1]
    In this case we will change the duration of the first note to a whole the second note to a half and so on. When the pattern "runs out" it simply cycles and start at the begging! So in our example the 5th notes duration would be a whole.


# Ideas

## Random rythmic patterns
- Add a random pattern function that takes as input a time signature and then returns a random rythmic pattern that fits in it.

## Arpeggios
- Given a list of notes, return an arpeggio for each note starting from that note. For example:
    given note sequence D, B, G
    Returns: D, F#, A, B, M G, G, B, D. This corresponds to Dmajor, E minor and Gmajor (This could be part of Dmajor scale)

- Expand the above to include major 7ths, minor 7ths and diminished chords. This should be done with respect to some scale. So this would be a two step process:
    Chose a probable scale given a list of notes, return the list of arpeggios for that scale as well as the scale you chose. 

    This should also have an option to provide a scale as well with the notes.
    