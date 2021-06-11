import concurrent.futures
import logging
import threading
import time
import matplotlib.pyplot as plt
import plotly as pl


def foo1():
    print('s - foo1')
    # plt.plot([1, 2, 3], [3, 2, 1])
    # plt.show()
    time.sleep(1)
    print('f - foo1')


def foo2():
    print('s - foo2')
    time.sleep(2)
    print('f - foo2')

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(foo1)
        executor.submit(foo2)

    pl.show()
    logging.info("Final")

#