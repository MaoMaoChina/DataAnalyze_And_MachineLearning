# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:24:20 2019

@author: dell
"""

import pandas as pd
pd.set_option('display.max_rows',10)
pd.set_option('display.max_columns',60)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn.externals import joblib
from yellowbrick.cluster import SilhouetteVisualizer



from flask import request,Flask,make_response
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)


bf = pd.read_csv('BlackFriday.csv')#数据导入
 #总体信息展示
#print(bf.info()) 
#print(bf.describe(include='all')) 
#bf.fillna(0,inplace=True)  #空值填充为0
#print(bf.head())
   
train = bf.drop(['Product_Category_2', 'Product_Category_3'，'User_ID','Product_ID'], axis=1)
y = train.pop('Purchase')
#性别转换成01二进制
train.loc[:, 'Gender'] = np.where(train['Gender'] == 'M', 1, 0)

#产品 ID，用户 ID 分类编码
for col in ['Product_ID', 'User_ID']:    
    train.loc[:, col] = LabelEncoder().fit_transform(train[col])
        
#年龄，城市类别，城市居住年限 独热编码
categoricals = ['Age', 'City_Category', 'Stay_In_Current_City_Years']
encoder = OneHotEncoder().fit(train[categoricals])
train = pd.concat([train, pd.bfFrame(encoder.transform(train[categoricals]).toarray(), index=train.index, columns=encoder.get_feature_names(categoricals))], axis=1)
train.drop(categoricals, axis=1, inplace=True)

#print(train.columns)

X_train, X_test, y_train, y_test = train_test_split(train, y)

#数据正则化
scaler = StandardScaler().fit(X_train)
X_train, X_test = scaler.transform(X_train), scaler.transform(X_test)

#选择模型参数
params = {
    'n_estimators': [10, 30, 100, 150, 300],
    'max_depth': [3, 5, 7, 9, 10]
}

#结果可视化
"""
print("Best params found: {}".format(grid_search.best_params_))
print("MSE score: {}".format(np.mean(preds-y_test)**2) )
sizes, train_scores, test_scores = learning_curve(RandomForestRegressor(**grid_search.best_params_), X_train, y_train, cv=3, n_jobs=-1, scoring='neg_mean_squared_error')
train_scores = np.mean((-1*train_scores)**0.5, axis=1)
test_scores = np.mean((-1*test_scores)**0.5, axis=1)
sns.lineplot(sizes, train_scores, label="Train")
sns.lineplot(sizes, test_scores, label="Test")
plt.xlabel("Size of training set", size=13)
plt.ylabel("Round Mean Squared Error", size=13)
plt.show()
"""

grid_search = GridSearchCV(RandomForestRegressor(), param_grid=params, cv=3, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)
model = grid_search.best_estimator_
joblib.dump(model, './model/RandomForestRegressor3.pkl')
