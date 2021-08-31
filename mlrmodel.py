# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 12:01:08 2021

@author: eagle
"""



import pandas as pd

import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression 



def l2model():
    l2=pd.read_csv("C://Data/l2_operator.csv")
    
    labelEnc=LabelEncoder()
    
    l2["L2Decision"]=labelEnc.fit_transform(l2["L2Decision"])
    
    l2_X=l2.loc[:,l2.columns!="performance"]
    l2_Y=l2.loc[:,l2.columns=="performance"]
    
    train_X,test_X,train_Y,test_Y=train_test_split(l2_X,l2_Y,test_size=0.2)
    
    l2_model=LogisticRegression(multi_class="multinomial", solver = "newton-cg").fit(train_X,train_Y)
    
    test_predict = l2_model.predict(test_X)
    
    accuracy_score(test_Y, test_predict)
    
    train_predict = l2_model.predict(train_X) # Train predictions 
    # Train accuracy 
    accuracy_score(train_Y, train_predict) 
    
    pickle_model=open("l2_mlr.pkl","wb")
    pickle.dump(l2_model,pickle_model)
    
    pickle_model.close()
    
    
l2model()

def l3model():
    l3=pd.read_csv("C://Data//l3_operator.csv")
    
    labelEnc=LabelEncoder()
    
    l3["L3Decision"]=labelEnc.fit_transform(l3["L3Decision"])
    
    l3_X=l3.loc[:,l3.columns!="performance"]
    
    l3_Y=l3.loc[:,l3.columns=="performance"]
    
    train_X,test_X,train_Y,test_Y=train_test_split(l3_X,l3_Y,test_size=0.2)
    
    l3_model=LogisticRegression(multi_class="multinomial",solver = "newton-cg").fit(train_X,train_Y["performance"])
    
    test_predict=l3_model.predict(test_X)
    
    print(accuracy_score(test_Y, test_predict))
    
    train_predict=l3_model.predict(train_X)
    
    print(accuracy_score(train_Y, train_predict))
    
    pickle.dump(l3_model,open("l3_mlr.pkl","wb"))
    
    
l3model()


