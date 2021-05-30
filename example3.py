import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(np.arange(5), index=list('abcde'))
ax = s.plot()


print(type(ax))


print(id(plt.gca()) == id(ax))

plt.show()