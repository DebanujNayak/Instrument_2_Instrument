from .generator import *

import os
import json
import time
import shutil

from scipy.io.wavfile import read as wread

class Dataset:
    def __init__(self):
        self.metadata = {}
        self.metadata_file_loaded = False
        self.metadata_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../data'))
        self.metadata_file = os.path.abspath(os.path.join(self.metadata_dir, 'metadata.json'))


    def load_metadata_file(self):
        try:
            metadata_file = open(self.metadata_file, 'r')
            raw_metadata = metadata_file.read()
            self.metadata = json.loads(raw_metadata)
            self.metadata_file_loaded = True
        except:
            self.metadata = {"files": []}
            self.metadata_file_loaded = True


    def get_dataset(self):
        self.load_metadata_file()
        files = self.metadata['files']
        notes_data = {}
        for entry in files:
            _, entry['list'] = wread(os.path.abspath(os.path.join(self.metadata_dir, entry['name'])))
            if tuple(entry['notes']) in notes_data:
                notes_data[tuple(entry['notes'])].append(entry)
            else:
                notes_data[tuple(entry['notes'])] = [entry]
        return list(notes_data.values())


    def get_file_name(self, notes, synth, dur):
        if not self.metadata_file_loaded:
            self.load_metadata_file()

        timestamp = time.time()
        file_name = "{}.wav".format(timestamp)
        file_info = {'name': file_name, 'notes': notes, 'synth': synth, 'dur':dur}
        self.metadata["files"].append(file_info)
        file_name = os.path.abspath(os.path.join(self.metadata_dir, file_name))
        return file_name


    def generate_dataset(self, number, size):
        for _ in range(number):
            notes = get_random_notes(size)
            generate_wavfile_from_notes(self, notes)
            
            metadata = json.dumps(self.metadata)
            metadata_file = open(self.metadata_file, 'w')
            metadata_file.write(metadata)
            metadata_file.close()

            self.metadata_file_loaded = False
