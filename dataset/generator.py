import pysynth as ps_a
import pysynth_b as ps_b
import pysynth_c as ps_c
import pysynth_d as ps_d
import pysynth_e as ps_e
import pysynth_p as ps_p


import random

basic_notes = ['a0', 'a#0', 'b0', 'c1', 'c#1', 'd1', 'd#1', 'e1', 'f1', 'f#1', 'g1', 'g#1', 'a1', 'a#1', 'b1', 'c2', 'c#2', 'd2', 'd#2', 'e2', 'f2', 'f#2', 'g2', 'g#2', 'a2', 'a#2', 'b2', 'c3', 'c#3', 'd3', 'd#3', 'e3', 'f3', 'f#3', 'g3', 'g#3', 'a3', 'a#3', 'b3', 'c4', 'c#4', 'd4', 'd#4', 'e4', 'f4', 'f#4', 'g4', 'g#4', 'a4', 'a#4', 'b4', 'c5', 'c#5', 'd5', 'd#5', 'e5', 'f5', 'f#5', 'g5', 'g#5', 'a5', 'a#5', 'b5', 'c6', 'c#6', 'd6', 'd#6', 'e6', 'f6', 'f#6', 'g6', 'g#6', 'a6', 'a#6', 'b6', 'c7', 'c#7', 'd7', 'd#7', 'e7', 'f7', 'f#7', 'g7', 'g#7', 'a7', 'a#7', 'b7', 'c8']

basic_synths = {ps_a: 'pysynth_a', ps_b: 'pysynth_b', ps_c: 'pysynth_c',ps_d:'pysynth_d',ps_e: 'pysynth_e', ps_p:'pysynth_p'}

def get_random_notes(size):
    basic_notes_len = len(basic_notes)
    notes = []
    for _ in range(size):
        random_index = random.randint(1, basic_notes_len - 1)
        random_note = basic_notes[random_index]
        notes.append(random_note)
    return notes


def generate_wavfile_from_notes(dataset, notes):
    size = len(notes)
    dur = random.uniform(1,9)    
    text = tuple(zip(notes, [dur]))
    for synth in basic_synths:
        file_name = dataset.get_file_name(notes, basic_synths[synth],dur)
        synth.make_wav(text, fn=file_name)

