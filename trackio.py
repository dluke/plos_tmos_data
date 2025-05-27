
# %%

import pickle
import sys
import os
import numpy as np

join = os.path.join

sys.path.append("C:/Users/daluk/workspace/pwl/tmos/code/analysis")

from glob import glob

data_path_list = glob("data/track_*.pkl")


path = 'data/track_00000.pkl'
new_folder = 'new/'
os.makedirs(new_folder, exist_ok=True)

for path in data_path_list:
    track_id = int(os.path.splitext(os.path.basename(path))[0].split('_')[-1])
    with open(path, 'rb') as f:
        track = pickle.load(f)
        data = track._track
        target = join(new_folder, 'track_%04d.npy' % track_id)
        print('writing to ', target)
        np.save(target, data)


# %%

