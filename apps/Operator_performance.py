# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:56:13 2021

@author: eagle
"""

import streamlit as st
import pandas as pd
import pickle

def L2_model(loginid,decision,time):
    model=pickle.load(open("https://github.com/Somasekhar1287/airport-security/blob/master/apps/l2_mlr.pkl","rb"))
    prediction=model.predict([[loginid,decision,time]])
    return prediction

def L3_model(loginid,decision,time):
    model=pickle.load(open("https://github.com/Somasekhar1287/airport-security/blob/master/apps/l3_mlr.pkl","rb"))
    prediction=model.predict([[loginid,decision,time]])
    return prediction

def app():
    L2_operator=pd.read_csv("https://github.com/Somasekhar1287/airport-security/blob/master/l2_operator_new.csv")
    L3_operator=pd.read_csv("https://github.com/Somasekhar1287/airport-security/blob/master/l3_operator_new.csv")
    
    l2_login_ids=L2_operator["L2LoginID"].unique().tolist()
    l2_login_ids.sort()
    l3_login_ids=L3_operator["L3LoginID"].unique().tolist()
    l3_login_ids.sort()
    
    l2_login_ids.insert(0,"Select L2 Operator")
    l3_login_ids.insert(0,"Select L3 Operator")
    
    
    predict_performance={1:"Excellent",2:"Good",3:"Normal",4:"Bad"}
    
    l2_decisions=L2_operator["L2Decision"].unique().tolist()
    l2_decisions.sort()
    
    l2_decisions.insert(0,"Select L2 Decision")
    
    l3_decisions=L3_operator["L3Decision"].unique().tolist()
    l3_decisions.sort()
    
    l3_decisions.insert(0,"Select L3 decision")
    
    st.title("Operator Performance")
    operator=st.sidebar.radio("Select Operator", ["L2 Operator","L3 Operator"])
    if operator=="L2 Operator":
        l2_login=st.selectbox("L2 Operator",options=l2_login_ids)
        L2Decision_selection=st.selectbox("L2 decision", options=l2_decisions)
        if L2Decision_selection=="Accept":
            l2_decision=0
        elif L2Decision_selection=="Reject":
            l2_decision=1
        else:
            l2_decision=2
        l2_time=st.number_input("L2 Time in secs")
        predict=st.button("Predict")
        if predict:
            pred=L2_model(l2_login, l2_decision, l2_time)
            result=predict_performance.get(pred[0])
            st.write("Performance of operator is: "+result)
    elif operator=="L3 Operator":
        l3_login=st.selectbox("L3 Operator",options=l3_login_ids)
        L3Decision_select=st.selectbox("L3 Decision", options=l3_decisions)
        if L3Decision_select=="Accept":
            l3_decision=0
        elif L3Decision_select=="Reject":
            l3_decision=1
        else:
            l3_decision=2
        l3_time=st.number_input("L3 Time in secs")
        predict=st.button("Predict")
        if predict:
            pred=L3_model(l3_login, l3_decision, l3_time)
            result=predict_performance.get(pred[0])
            st.write("Performance of l3 operator is : "+result)
