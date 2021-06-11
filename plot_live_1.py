import concurrent.futures
import logging
import random
import threading
import time
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = list(range(3))
    y = [np.sin(i)*10 for i in x]

    plt.plot(x, y)
    # plt.show(block=False)

    for i in range(len(x), len(x) + 10):
        x.append(i)
        y.append(np.sin(i))
        print(f'x: {x}, y: {y}')

        plt.clf()
        # plt.scatter(1,2)
        if i % 2:
            plt.plot(x, y, c='r')
        else:
            plt.scatter(x, y, c='r')
        # Necessary to view frames before they are unrendered
        plt.pause(0.001)
        # some other calculations
        time.sleep(0.1)
