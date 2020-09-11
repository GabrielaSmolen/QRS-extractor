import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt


def calculating_features_with_for(qrs_normal, qrs_abnormal):

    start = time.time()

    features_normal = []
    features_abnormal = []

    for i in range(0, len(qrs_normal.values)):
        qrs = qrs_normal.values[i, :]
        qrs = qrs - np.mean(qrs)
        feature = sum(abs(qrs))
        features_normal.append(feature)

    for i in range(0, len(qrs_abnormal.values)):
        qrs = qrs_abnormal.values[i, :]
        qrs = qrs - np.mean(qrs)
        feature = sum(abs(qrs))
        features_abnormal.append(feature)

    print(time.time() - start)

    return features_normal, features_abnormal


def calculating_features_with_broadcasting(qrs_normal, qrs_abnormal):

    start = time.time()

    qrs_normal_filtered = qrs_normal.values - np.mean(qrs_normal.values, axis=1, keepdims=True)
    qrs_abnormal_filtered = qrs_abnormal.values - np.mean(qrs_abnormal.values, axis=1, keepdims=True)

    features_normal = np.sum(np.abs(qrs_normal_filtered), axis=1)
    features_abnormal = np.sum(np.abs(qrs_abnormal_filtered), axis=1)

    print(time.time() - start)

    return features_normal, features_abnormal


if __name__ == '__main__':

    qrs_normal = pd.read_csv('data/mit-bih-arrhythmia-database-1.0.0/228_normal.csv', header=None)
    qrs_abnormal = pd.read_csv('data/mit-bih-arrhythmia-database-1.0.0/228_abnormal.csv', header=None)

    # features_normal, features_abnormal = calculating_features_with_for(qrs_normal, qrs_abnormal)
    features_normal, features_abnormal = calculating_features_with_broadcasting(qrs_normal, qrs_abnormal)

    my_features = {'normal': features_normal, 'abnormal': features_abnormal}

    fig, ax = plt.subplots()
    ax.boxplot(my_features.values())
    ax.set_xticklabels(my_features.keys())
    ax.set_title('Features comparison')
    plt.show()
