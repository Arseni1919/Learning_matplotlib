import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    # plt.clf()
    plt.scatter(i, y)
    plt.pause(0.05)
    time.sleep(1)


# plt.show()