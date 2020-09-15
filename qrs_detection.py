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
    y = lfilter(b, a, data)
    return y


def derivative_filter(samples):
    derivative = np.append(0, samples[1:] - samples[:-1])
    return derivative


def squaring(samples):
    square = np.square(samples)
    return square


def moving_average_filter(samples):
    convolution = np.convolve(samples, np.ones(int(150*fs/1000))/int((150*fs/1000)), mode='same')
    return convolution


if __name__ == '__main__':
    signal = wfdb.rdrecord('data/mit-bih-arrhythmia-database-1.0.0/100')
    samp_to = 1000
    samples = signal.p_signal[0:samp_to, 0]

    order = 3
    fs = signal.fs
    cutoff = 20

    b, a = butter_lowpass(cutoff, fs, order)
    lowpass = butter_lowpass_filter(samples, cutoff, fs, order)

    b, a = butter_highpass(cutoff, fs, order)
    highpass = butter_highpass_filter(lowpass, cutoff, fs, order)

    derivative = derivative_filter(highpass)

    square = squaring(derivative)

    moving_average = moving_average_filter(square)
    plot_filtration_result(square, moving_average)
