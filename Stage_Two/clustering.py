# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:05:45 2019

@author: dell
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

bf = pd.read_csv('E:\FranchProject\BlackFriday.csv')#数据导入
bf.fillna(0,inplace=True)  #空值填充为0
#把Product_ID, Product_Category_1, Product_Category_2, Product_Category_3, Purchase相关性不强的特征舍去
train = bf.drop(['Product_ID', 'Product_Category_1', 'Product_Category_2', 'Product_Category_3', 'Purchase'], axis=1).groupby('User_ID')

train = train.agg(lambda x: x.value_counts().index[-1])
feaures_list = list(train.columns.values)
print(feaures_list)
#产品
encoder = OneHotEncoder().fit(train[feaures_list])
train = pd.concat([train, pd.DataFrame(encoder.transform(train[feaures_list]).toarray(), index=train.index, columns=encoder.get_feature_names(feaures_list))], axis=1)
train.drop(feaures_list, axis=1, inplace=True)

columns = ['Product_ID', 'Product_Category_1']
for column in columns:
    top_100 = bf[column].value_counts().index[:100]    
    user_purchase = pd.pivot_table(
        bf[['User_ID', column, 'Purchase']],
        values='Purchase',
        index='User_ID',
        columns=column,
        aggfunc=np.sum
    ).fillna(0)[top_100]  
    train = train.join(user_purchase)
    
train = train.join(bf[['User_ID', 'Purchase']].groupby('User_ID').agg('sum'))

train_scaled = StandardScaler().fit_transform(train)

k_values = np.arange(1, 11)
models = []
dists = []
for k in k_values:
    model = KMeans(k).fit(train_scaled)
    models.append(model)
    dists.append(model.inertia_)

plt.figure(figsize=(9, 6))
plt.plot(k_values, dists, '*-')
plt.ylabel('Sum of squared distances', size=13)
plt.xlabel('K', size=13)
plt.xticks(k_values)
plt.show()

for k in k_values:
    model = models[k]
    #print("{} model".format(k))
    print("{} model Silhouette score: {:.2f}".format(k,silhouette_score(train_scaled, model.predict(train_scaled))) )
