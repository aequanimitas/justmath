import IPython
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib
import sklearn
import requests
import networkx as nx
import bs4
import mrjob
import pattern
import seaborn

%matplotlib inline

import matplotlib.pyplot as plt

x = np.linspace(0,10,30)
y = np.sin(x)
z = y + np.random.normal(size=30) * .2

plt.plot(x,y, 'ro-', label='A sine wave')
plt.plot(x,z, 'b-', label='Noisy sine')
plt.legend(loc = 'lower right')
plt.xlabel("X Axis")
plt.ylabel("Y axis")
