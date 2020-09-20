from qrs_detection.qrs_detection import detect_qrs
from utils.base_objects import QRS
import wfdb
import numpy as np


def qrs_analysis(signal):
    detected_qrs_samples = np.array(detect_qrs(signal, cutoff=20, fs=fs, order=3))
    window_len = 150 * fs / 1000
    analysed_samples = []
    detected_qrs_samples = detected_qrs_samples[:-1]
    for sample in detected_qrs_samples:
        one_qrs = []
        for i in range(int(sample - window_len), int(sample + window_len)):
            one_qrs.append(i)
        one_qrs = samples[one_qrs]
        qrs = QRS(one_qrs)
        qrs.process()
        analysed_samples.append(QRS.get_label(qrs))

    return analysed_samples


if __name__ == '__main__':
    signal = wfdb.rdrecord('../data/mit-bih-arrhythmia-database-1.0.0/228')
    samples = np.array(signal.p_signal[:, 0])
    fs = signal.fs

    analysed_signal = qrs_analysis(samples)

    print()
