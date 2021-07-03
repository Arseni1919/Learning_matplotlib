# Learning `matplotlib`

## About

A picture is worth a thousand words, and with Python’s matplotlib library,
it fortunately takes far less than a thousand words of code to create a production-quality graphic.

However, matplotlib is also a massive library,
and getting a plot to look just right is often achieved through trial and error.
Using one-liners to generate basic plots in matplotlib is fairly simple,
but skillfully commanding the remaining 98% of the library can be daunting.

## The construction

![](static/plot_objects.png)

## Examples

### Example 1 - [`example1.py`](example1.py)

<!-- ![](static/e1.png) -->
<img src="static/e1.png" alt="drawing" width="400"/>

### Example 2 - [`example2.py`](example2.py)

<!-- ![](static/e2.png) -->
<img src="static/e2.png" alt="drawing" width="400"/>

### Example 3 - Plotting During The Run

Plot live examples in [`plot_live_1.py`](plot_live_1.py) and [`plot_live_2.py`](plot_live_2.py).

<!-- ![](static/e3.gif) -->
<img src="static/e3.gif" alt="drawing" width="400"/>

### Tricks

#### Change `figsize` in `plt` mode

You need to plug `plt.rcParams["figure.figsize"] = [6.4, 6.4]` before plotting.

## Credits

- [plot live - 1 (stackoverflow)](https://stackoverflow.com/questions/28269157/plotting-in-a-non-blocking-way-with-matplotlib)
- [plot live - 2 (stackoverflow)](https://stackoverflow.com/questions/11874767/how-do-i-plot-in-real-time-in-a-while-loop-using-matplotlib)
- [clr - clear figure (stackoverflow)](https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib)
- [Live Updating Graphs with Matplotlib Tutorial](https://pythonprogramming.net/python-matplotlib-live-updating-graphs/)
- [Real Python Tutorial - Python Plotting With Matplotlib (Guide)](https://realpython.com/python-matplotlib-guide/)
- [Real Python Tutorial - An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/#using-a-threadpoolexecutor)
- [Real Python Tutorial - https://realpython.com/python-concurrency/](https://realpython.com/python-concurrency/)
- [Matplotlib - Docs](https://matplotlib.org/2.0.2/examples/showcase/anatomy.html)














