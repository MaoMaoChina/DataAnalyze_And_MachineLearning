# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:20:37 2019

@author: dell
"""

import pandas as pd
pd.set_option('display.max_rows',10)
pd.set_option('display.max_columns',60)
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib

from flask import Flask

bf = pd.read_csv('BlackFriday.csv')#数据导入
bf.fillna(0,inplace=True)  #空值填充为0

#Regression Model
train = bf.drop(['Product_Category_2', 'Product_Category_3','Product_ID','User_ID'], axis=1)
y = train.pop('Purchase')
#print(train.columns)
#print(train.head(10))
train.loc[:, 'Gender'] = np.where(train['Gender'] == 'M', 1, 0)   

#print(train.columns)
#print(train.head(10))
# One hot encoding other features
featruecoder = ['Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years','Product_Category_1' ]
encoder = OneHotEncoder().fit(train[featruecoder])

#print(train.columns)
#print(train.head(2))
train = pd.concat([train, pd.DataFrame(encoder.transform(train[featruecoder]).toarray(), index=train.index, columns=encoder.get_feature_names(featruecoder))], axis=1)
                    
#print(train.columns)A
#print(train.head(2))
train.drop(featruecoder, axis=1, inplace=True)

#print(train.columns)
#print(train.head(2))

# Splitting train and test setsAA
X_train, X_test, y_train, y_test = train_test_split(train, y )

# Standardizing
scaler = StandardScaler().fit(X_train)
X_train, X_test = scaler.transform(X_train), scaler.transform(X_test)



params = {
    'n_estimators': [10, 30, 100, 300],
    'max_depth': [3, 5, 7]
}

grid_search = GridSearchCV(RandomForestRegressor(), param_grid=params, cv=3, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)
preds = grid_search.predict(X_test)
print("Best params found: {}".format(grid_search.best_params_))
print("MSE score: {}".format(np.mean(preds-y_test)**2) )

model = grid_search.best_estimator_
joblib.dump(model, './model/RandomForestRegressor.pkl')