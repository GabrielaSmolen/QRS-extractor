import matplotlib.pyplot as plt
import numpy as np

import wfdb


def plot_wfdb(signal, annotation, samp_to):
    part = signal.p_signal[0:samp_to, 0]
    plt.plot(part)

    indexes = np.where(annotation.sample < samp_to)
    sample = annotation.sample[indexes]

    length = len(sample)
    values = np.ones(length)

    plt.plot(sample, values, 'o')
    plt.show()


if __name__ == '__main__':

    signal = wfdb.rdrecord('../data/mit-bih-arrhythmia-database-1.0.0/100', sampto=15000)

    annotation = wfdb.rdann('../data/mit-bih-arrhythmia-database-1.0.0/100', 'atr', sampto=15000)
    wfdb.plot_wfdb(record=signal, annotation=annotation)

    samp_to = 2000

    plot_wfdb(signal, annotation, samp_to)
