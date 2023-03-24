# %%
from classes.DataGenerator import Generator
from classes.DataIngester import Ingester
from classes.DataPlotter import Plotter

import numpy as np
import pandas as pd
import chardet

# %%
def load_data(data_path):
    with open(data_path, "rb") as f:
        result = chardet.detect(f.read())
    return pd.read_csv(data_path, encoding=result["encoding"])

def get_list_of_composers(data):
    return data["canonical_composer"].unique()

def get_data_for_composer(data, composer_names, data_dir='./data'):
    composer_indexes = []
    composer_list = get_list_of_composers(data)
    for idx, composer in enumerate(composer_list):
        for composer_name in composer_names:
            if composer.find(composer_name) >= 0:
                composer_indexes.append(idx)

    assert len(composer_indexes) > 0, f"Composer name: \"{composer_name}\" not recognized!!"

    all_midi_files = []
    for composer_idx in composer_indexes:
        composer_df = data.query(f"canonical_composer == '{composer_list[composer_idx]}'")
        composer_midi_paths = composer_df["midi_filename"].to_list()
        all_midi_files += composer_midi_paths

    generator = Generator()
    midi_data = []
    for midi_file in all_midi_files:
        new_idx = len(midi_data)
        midi_data.append(generator.returnArrayOfNotes(generator.convertMidiToObject(f'{data_dir}/{midi_file}')))
        
        if new_idx > 0:
            prev_file = midi_data[new_idx - 1]
            last_event = max(prev_file[:,1])
            midi_data[new_idx][:,0:2] += last_event + 25 # a little bit of padding

    return np.concatenate(midi_data)

# %%
# main_data = load_data('../data/maestrov3.csv')
# composers = get_list_of_composers(main_data)
# midi_data = get_data_for_composer(main_data, 'Nikolai Medtner', '../data')
# print(len(midi_data))
# print(midi_data)

# %%
