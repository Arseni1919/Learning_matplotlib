import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
dataArray = [i for i in range(50)]


def animate(i):
    print(i)
    time.sleep(0.1)
    xar = []
    yar = []
    for item in dataArray:
        if item > 1:
            x, y = item, random.randint(0, 10)
            xar.append(x)
            yar.append(y)
    if i < 3:
        ax1.clear()
        ax1.plot(xar, yar)
    else:
        plt.close()


if __name__ == '__main__':
    ani = animation.FuncAnimation(fig, animate, interval=10)
    print('before show')
    plt.show()
    print('after show')
