import wfdb
import numpy as np
import json

signal = wfdb.rdrecord('data/mit-bih-arrhythmia-database-1.0.0/100')
sampto = 3000
samples = signal.p_signal[0:sampto, 0].tolist()
samples = {'samples': samples}

with open('../data/test_samples.json', 'w') as outfile:
    json.dump(samples, outfile)

print()
