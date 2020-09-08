import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

qrs_normal = pd.read_csv('data/mit-bih-arrhythmia-database-1.0.0/228_normal.csv', header=None)
qrs_abnormal = pd.read_csv('data/mit-bih-arrhythmia-database-1.0.0/228_abnormal.csv', header=None)

# features = []
# for i in range(0, len(qrs_normal.values)):
#     qrs = qrs_normal.values[i, :]
#     feature = sum(abs(qrs))
#     features.append(feature)

features_normal = np.sum(np.abs(qrs_normal.values), axis=1)
features_abnormal = np.sum(np.abs(qrs_abnormal.values), axis=1)

# plt.boxplot(features_normal)
# plt.boxplot(features_abnormal)
# plt.show()

my_features = {'normal': features_normal, 'abnormal': features_abnormal}

fig, ax = plt.subplots()
ax.boxplot(my_features.values())
ax.set_xticklabels(my_features.keys())
ax.set_title('Features comparison')
plt.show()
