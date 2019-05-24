import sys
sys.version
sys.version_info

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import ElasticNet, ElasticNetCV, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from scipy import stats


train_df = pd.read_csv('C:/Users/apple/Desktop/dataAnalysis/van_ai_coding_challenge_4-master/van_ai_coding_challenge_4-master/data/train.csv')
train_df.shape
# convert the discrete columns into dummy variables

dummy_cols = ['Product_ID', 'Gender', 'Age', 'City_Category', 'Stay_In_Current_City_Years']
train_df_with_dummies = pd.get_dummies(train_df, columns= dummy_cols)
# drop NaN in the dataframe
train_df_with_dummies_noNaN = train_df_with_dummies.dropna()

