import pandas as pd
import matplotlib.pyplot as plt


def plot_single_qrs(path):

    data = pd.read_csv(path, header=None)
    values = data.values

    for i in range(0, len(values)):
        qrs = values[i, :]
        if 'abnormal' in path:
            plt.plot(qrs, color='r')
            plt.show()
        else:
            plt.plot(qrs)
            plt.show()


if __name__ == '__main__':

    path = '../data/mit-bih-arrhythmia-database-1.0.0/232_normal.csv'
    plot_single_qrs(path)
