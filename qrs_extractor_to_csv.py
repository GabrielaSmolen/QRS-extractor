import pandas as pd
from os import listdir
from os.path import isfile, join
import wfdb


def qrs_extractor_to_csv(signal_path):
    """doc"""
    signal = wfdb.rdrecord(signal_path)
    annotation = wfdb.rdann(signal_path, 'atr')

    samples = annotation.sample
    symbols = annotation.symbol

    sampling_frq = signal.fs
    window_len = 150 * sampling_frq / 1000

    normal_qrs = []
    abnormal_qrs = []

    for sample, symbol in zip(samples,symbols):
        qrs = signal.p_signal[int(sample - window_len):int(sample + window_len), 0]
        if symbol in ['N', 'R', 'L', 'j', 'e']:
            normal_qrs.append(qrs.tolist())
        if symbol == 'V':
            abnormal_qrs.append(qrs.tolist())

    extracted_qrs = pd.DataFrame(normal_qrs)
    extracted_qrs.to_csv(signal_path+'_normal.csv', index=False, header=False)

    extracted_qrs = pd.DataFrame(abnormal_qrs)
    extracted_qrs.to_csv(signal_path + '_abnormal.csv', index=False, header=False)


if __name__ == '__main__':

    root = 'data/mit-bih-arrhythmia-database-1.0.0'

    files = [file[0:3] for file in listdir(root) if isfile(join(root, file))]
    files = sorted(list(set(files)))

    for file in files:
        print(file)
        qrs_extractor_to_csv(join(root, file))
