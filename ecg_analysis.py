from qrs_detection.qrs_detection import detect_qrs
from utils.base_objects import QRS
import wfdb
import numpy as np
import matplotlib.pyplot as plt


def qrs_analysis(signal):
    detected_qrs_samples_indexes = np.array(detect_qrs(signal, cutoff=20, fs=fs, order=3))
    detected_qrs_samples = samples[detected_qrs_samples_indexes[:-1]]
    detected_qrs_samples = detected_qrs_samples.tolist()
    window_len = 150 * fs / 1000
    morphology_class = []
    detected_qrs_samples_indexes = detected_qrs_samples_indexes[:-1].tolist()
    for sample in detected_qrs_samples_indexes:
        one_qrs = []
        for i in range(int(sample - window_len), int(sample + window_len)):
            one_qrs.append(i)
        one_qrs = samples[one_qrs]
        qrs = QRS(one_qrs)
        qrs.process()
        morphology_class.append(QRS.get_label(qrs))

    plt.figure()
    for i in range(0, len(morphology_class)):
        if morphology_class[i] == 'N':
            plt.plot(detected_qrs_samples_indexes[i], detected_qrs_samples[i], color='g', marker='$N$', zorder=3)
        else:
            plt.plot(detected_qrs_samples_indexes[i], detected_qrs_samples[i], color='r', marker='$V$', zorder=3)

    plt.plot(samples, zorder=-1)
    plt.show()

    return morphology_class


if __name__ == '__main__':
    signal = wfdb.rdrecord('data/mit-bih-arrhythmia-database-1.0.0/100')
    samples = np.array(signal.p_signal[:, 0])
    fs = signal.fs

    morphology_class = qrs_analysis(samples)

    print()
