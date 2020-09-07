import pandas as pd

import wfdb


if __name__ == '__main__':

    signal = wfdb.rdrecord('data/mit-bih-arrhythmia-database-1.0.0/100')

    annotation = wfdb.rdann('data/mit-bih-arrhythmia-database-1.0.0/100', 'atr')

    samples = annotation.sample

    sampling_frq = signal.fs

    window_len = 150*sampling_frq/1000

    qrs_list = []

    for sample in samples:
        qrs = signal.p_signal[int(sample-window_len):int(sample+window_len), 0]
        qrs_list.append(qrs.tolist())

    extracted_qrs = pd.DataFrame(qrs_list)
    extracted_qrs.to_csv('data/extracted_qrs.csv', index=False, header=False)

