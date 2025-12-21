import pandas as pd
import numpy ad np
import sklearn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn import preprocessing
import sys
import matplotlib.pyplot as plt
%matplotlib inline
import numpy.random as nr

import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import SGDClassifier, Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, train_test_split

from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPRegressor
#from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error