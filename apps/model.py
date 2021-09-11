# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:01:13 2021

@author: eagle
"""

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
    url="https://github.com/Somasekhar1287/airport-security/blob/master/l2_operator_new.csv"
    l2=pd.read_csv(url)
    
    
    labelEnc=LabelEncoder()
    
    l2["L2Decision"]=labelEnc.fit_transform(l2["L2Decision"])
    
    l2=l2[["L2LoginID","L2Decision","timesecs1","performance","op_performance"]]
    
    l2_X=l2.loc[:,["L2LoginID","L2Decision","timesecs1"]]
    l2_Y=l2.loc[:,l2.columns=="op_performance"]
    
    train_X,test_X,train_Y,test_Y=train_test_split(l2_X,l2_Y,test_size=0.2)
    
    l2_model=LogisticRegression(multi_class="multinomial", solver = "newton-cg").fit(train_X,train_Y["op_performance"])
    return l2_model
    


def l3model():
    url="https://github.com/Somasekhar1287/airport-security/blob/master/l3_operator_new.csv"
    l3=pd.read_csv(url)
    
    labelEnc=LabelEncoder()
    
    l3["L3Decision"]=labelEnc.fit_transform(l3["L3Decision"])
    
    
    l3=l3[["L3LoginID","L3Decision","timesecs2","performance","op_performance"]]
    
    l3_X=l3.loc[:,["L3LoginID","L3Decision","timesecs2"]]
    
    l3_Y=l3.loc[:,l3.columns=="op_performance"]
    
    train_X,test_X,train_Y,test_Y=train_test_split(l3_X,l3_Y,test_size=0.2)
    
    l3_model=LogisticRegression(multi_class="multinomial",solver = "newton-cg").fit(train_X,train_Y["op_performance"])
    return l3_model
    

def main():
    l2_model=l2model()
    l3_model=l3model()
    pickle.dump(l2_model,open("l2_mlr.pkl","wb"))
    pickle.dump(l3_model,open("l3_mlr.pkl","wb"))
    #model=[l2_model,l3_model]
    

if __name__=='__main__':
    main()
