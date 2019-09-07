# standard imports

# print everything
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import sys
print('python:', sys.version_info[:3])

import numpy as np
print('numpy:', np.__version__)

import pandas as pd
print('pandas:', pd.__version__)

import sklearn as sk
print('sklearn:', sk.__version__)

import tensorflow as tf
print('tensorflow:', tf.__version__)

import matplotlib.pyplot as plt
%matplotlib inline

import seaborn as sns
print('seaborn:', sns.__version__)
plt.style.use('ggplot')
