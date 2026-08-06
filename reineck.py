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

import gspread
from google.oauth2.service_account import Credentials

def myOHE(df, header):
    #df_list = df[header].values.tolist()
    #df_list = [str(val) for val in df[header].values]
    df_list = df[header].astype(str).tolist()
    myDict = {k:df_list.index(k) for k in df_list}
    #print (myDict)
    df_new = df
    le = preprocessing.LabelEncoder()
    df_new[header] = le.fit_transform(df_new[header].astype(str))
    # for head in myDict.keys():
    #     df_new[df_new[header]==head][head] = myDict[head]
    return df_new
