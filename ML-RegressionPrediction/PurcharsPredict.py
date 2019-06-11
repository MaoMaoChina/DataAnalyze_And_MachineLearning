# -*- coding: utf-8 -*-
"""
Created on Wed May  15 19:20:57 2019

@author: dell
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from flask import request,Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def upload(User_ID,Product_ID,Gender,Age,Occupation,City,CityStay,Marital_Status,Category):
    uploadset = pd.read_csv('testset(3).csv')#数据导入
    uploadset = uploadset.append([{'User_ID':User_ID,'Product_ID':Product_ID,'Gender':Gender,'Age':Age,'Occupation':Occupation,'City_Category':City,'Stay_In_Current_City_Years':CityStay,'Marital_Status':Marital_Status,'Product_Category_1':Category}], ignore_index=True)
    uploadset.fillna(0,inplace=True)
    uploadset.to_csv('testset(3).csv',index=False)

def testpredict():
    testset = pd.read_csv('testset(3).csv')#数据导入
    #print(testset.tail(5))
    testset.loc[:, 'Gender'] = np.where(testset['Gender'] == 'M', 1, 0)
    for col in ['Product_ID', 'User_ID']:    
        testset.loc[:, col] = LabelEncoder().fit_transform(testset[col])
    featruecoder = ['Age', 'City_Category', 'Stay_In_Current_City_Years']
    encoder = OneHotEncoder().fit(testset[featruecoder])
    testset = pd.concat([testset, pd.DataFrame(encoder.transform(testset[featruecoder]).toarray(), index=testset.index, columns=encoder.get_feature_names(featruecoder))], axis=1) 
    testset.drop(featruecoder, axis=1, inplace=True)
    scaler = StandardScaler().fit(testset)
    testset = scaler.transform(testset)
    model=joblib.load('./model/RandomForestRegressor3.pkl')
    len_test = len(testset)
    resultset=model.predict(testset)
    #print(model.predict(testset))
    return resultset[len_test-1]


@app.route('/RegressionPredict', methods=['POST'])  
def RegressionPredict():
    print(request.json)
    data = request.json
    User_ID = data['User_ID']
    Product_ID = data['Product_ID']
    Gender = data['Gender']
    Age    = data['Age']
    Occupation = data['Occupation']
    City = data['City']
    CityStay = data['CityStay']
    Marital_Status =data['Marital_Status']
    Category = data['Category']
    upload(User_ID,Product_ID,Gender,Age, Occupation,City,CityStay,Marital_Status,Category)
    result=testpredict()
    print(result)
    #response = make_response(jsonify({'result': result}))
    #print (response)
    return jsonify({'result': result})







if __name__ == '__main__':
    app.run(host='127.0.0.1',
    port= 5000,
    debug=True,
    use_reloader=False
)
