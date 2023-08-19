from musicality.constants import INSTRUMENT_RANGE





def mutate(melody):
    from musicality.classes.note import Note
    from musicality.constants import NOTE_MUTATION_RATE
    from random import randint
    from random import random 
    from copy import deepcopy
    new_melody = deepcopy(melody)
    # Either add or change a note
    if random() > NOTE_MUTATION_RATE:
        # Change note
        index = randint(0, len(new_melody) - 1)
        note = new_melody[index]
        note.pitch = randint(*INSTRUMENT_RANGE)
    else:
        # Add note
        index = randint(0, len(new_melody))
        new_melody.insert(index, Note(
            randint(*INSTRUMENT_RANGE)
        ))
    return new_melody

def evaluate(melody, scale):
    return _in_scale_score(melody, scale) + _semitone_extension_of__melody_score(melody) + _is_subtonic(melody, scale), 0


def _in_scale_score(melody, scale):
    from musicality.constants import IN_SCALE_REWARD_FACTOR
    score = 0
    for note in melody:
        if note in scale:
            score += 1
    return score/IN_SCALE_REWARD_FACTOR

def _semitone_extension_of__melody_score(melody):
    from musicality.constants import SEMITONE_EXTENSION_REWARD_FACTOR
    from statistics import variance
    pitches = [note.pitch for note in melody]
    return variance(pitches)/SEMITONE_EXTENSION_REWARD_FACTOR

def _is_subtonic(melody, scale):
    from musicality.constants import HAS_SUBTONIC_REWARD
    scale_subtonic = scale[-1]
    for i, k in zip(melody[0::2], melody[1::2]):
        if scale.is_subtonic(i) and scale.is_tonic(k) and (k.pitch-i.pitch) < 3:
            return HAS_SUBTONIC_REWARD
    return 0
        
def _difference_with_original(melody, original_melody):
    """
    We count the percentage of notes in the melody that are not in the original melody
    """
    pass
