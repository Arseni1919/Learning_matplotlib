import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random
import asyncio


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


class My_data:
    dataArray = []

my_data = My_data()
my_data.dataArray = [i for i in range(50)]
print(my_data.dataArray)

def animate(i):
    print(my_data.dataArray)
    xar = []
    yar = []
    for item in my_data.dataArray:
        if item > 1:
            x, y = item, random.randint(0, 10)
            xar.append(x)
            yar.append(y)
    print(my_data.dataArray, xar, yar)
    if i < 3:
        ax1.clear()
        ax1.plot(xar, yar)
    else:
        plt.close()


async def plotting():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    print('before show')
    # await plt.show()
    for i in range(3):
        await asyncio.sleep(1)
    print('after show')


async def plot_things():
    print(f'inside plot_things')
    await asyncio.sleep(1)
    await plotting()


async def change_length():
    print('inside change_length')
    for i in range(3):
        if i % 2:
            my_data.dataArray = [i in range(5)]
        else:
            my_data.dataArray = [i in range(10)]
        await asyncio.sleep(1)
        print(f'iteration {i} in change_length')


async def main():
    await asyncio.gather(plot_things(), change_length())

if __name__ == '__main__':
    asyncio.run(main())
