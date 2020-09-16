from typing import Any, Union

import numpy as np
from scipy.signal import butter, lfilter, freqz, filtfilt
import matplotlib.pyplot as plt
import wfdb


def plot_freqz(b, a):
    plt.figure()
    w, h = freqz(b, a, worN=8000)
    plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    plt.plot(cutoff, 0.5 * np.sqrt(2), 'ko')
    plt.axvline(cutoff, color='k')
    plt.xlim(0, 0.5 * fs)
    plt.title("Lowpass Filter Frequency Response")
    plt.xlabel('Frequency [Hz]')
    plt.grid()
    plt.show()


def plot_filtration_result(original, filtered):
    plt.figure()
    plt.plot(original, 'b', label='data')
    plt.plot(filtered, 'g', linewidth=2, label='filtered data')
    plt.xlabel('Samples')
    plt.grid()
    plt.legend()
    plt.show()


def butter_lowpass(cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y


def butter_highpass(cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a


def butter_highpass_filter(data, cutoff, fs, order):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y


def derivative_filter(samples):
    derivative = np.append(0, samples[1:] - samples[:-1])
    return derivative


def square(samples):
    square = np.square(samples)
    return square


def moving_average_filter(samples):
    convolution = np.convolve(samples, np.ones(int(150*fs/1000))/int((150*fs/1000)), mode='same')
    return convolution


def find_peaks(samples, fs):
    initial_peaks = []
    for i in range(3, len(samples)-3):
        if samples[i - 3] < samples[i - 2] < samples[i - 1] < samples[i] > samples[i + 1] > samples[i + 2] > samples[i + 3]:
            if samples[i] > 0.001 * np.max(samples):
                initial_peaks.append(i)
    peaks = []
    for i in range(0, len(initial_peaks)-1):
        if (initial_peaks[i+1] - initial_peaks[i]) >= fs*200/1000:
            peaks.append(initial_peaks[i])
    peaks.append(initial_peaks[-1])

    print(peaks)
    return peaks, initial_peaks


def choose_qrs_peaks(samples, fs, peaks, peakes_indexes):
    noiselevel = np.average(samples[0:fs*2])
    signallevel = np.max(samples[0:fs*2])

    noiselevel_list = []
    signallevel_list = []
    threshold_list = []
    final_peaks_indexes = []

    for peak, peak_index in zip(peaks, peaks_indexes):
        threshold = noiselevel + 0.25 * (signallevel - noiselevel)
        if peak < threshold:
            noiselevel = 0.125 * peak + 0.875 * noiselevel
        else:
            signallevel = 0.125 * peak + 0.875 * signallevel
            final_peaks_indexes.append(peak_index)

        threshold_list.append(threshold)
        signallevel_list.append(signallevel)
        noiselevel_list.append(noiselevel)

    return noiselevel_list, signallevel_list, threshold_list, final_peaks_indexes


if __name__ == '__main__':
    signal = wfdb.rdrecord('data/mit-bih-arrhythmia-database-1.0.0/100')
    samp_to = 10000
    samples = signal.p_signal[0:samp_to, 0]

    order = 3
    fs = signal.fs
    cutoff = 20

    b, a = butter_lowpass(cutoff, fs, order)
    lowpass = butter_lowpass_filter(samples, cutoff, fs, order)

    b, a = butter_highpass(cutoff, fs, order)
    highpass = butter_highpass_filter(lowpass, cutoff, fs, order)

    derivative = derivative_filter(highpass)
    square = square(derivative)
    averaged_signal = moving_average_filter(square)

    peaks_indexes, initial_peaks_indexes = find_peaks(averaged_signal, fs)
    initial_peaks = averaged_signal[initial_peaks_indexes]
    peaks = averaged_signal[peaks_indexes]

    noise, signal, threshold, final_peaks = choose_qrs_peaks(averaged_signal, fs, peaks, peaks_indexes)

    plt.figure()
    plt.plot(peaks_indexes, peaks, 'o')
    plt.plot(initial_peaks_indexes, initial_peaks, '.')
    plt.plot(averaged_signal)
    plt.plot(peaks_indexes, noise, '--')
    plt.plot(peaks_indexes, signal, '--')
    plt.plot(peaks_indexes, threshold, '--')
    plt.show(block=False)

    plt.figure()
    plt.plot(samples)
    plt.plot(final_peaks, samples[final_peaks], 'ro')
    plt.show(block=False)
    print()
