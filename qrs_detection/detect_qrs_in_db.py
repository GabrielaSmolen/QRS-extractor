from qrs_detection.qrs_detection import detect_qrs
import wfdb
import numpy as np
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    root = '../data/mit-bih-arrhythmia-database-1.0.0'

    files = [file[0:3] for file in listdir(root) if isfile(join(root, file))]
    files = sorted(list(set(files)))

    for file in files:
        print(file)
        signal = wfdb.rdrecord(join(root, file))
        samples = signal.p_signal[:, 0]
        fs = signal.fs
        final_peaks = detect_qrs(samples, cutoff=20, fs=fs, order=3)
        wfdb.wrann(file, 'pred', np.array(final_peaks), symbol=['N'] * len(final_peaks), write_dir=root)
