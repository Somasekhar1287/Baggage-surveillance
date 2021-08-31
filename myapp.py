# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:18:33 2021

@author: eagle
"""

import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle


def L3predict(loginid,decision,time):
    l3_model=pickle.load(open("l3_mlr.pkl","rb"))
    prediction=l3_model.predict([[decision,loginid,time]])
    return prediction[0]



def L2predict(loginid,decision,time):
    l2_model=pickle.load(open("l2_mlr.pkl","rb"))
    prediction=l2_model.predict([[decision,loginid,time]])
    return prediction[0]

def plot(x,y,title,x_title,y_title):
    with st.container():
        fig,ax=plt.subplots(figsize=(5,5))
        ax=sns.barplot(x,y,hue=x)
        ax.set_title(title)
        ax.set_xlabel(x_title)
        ax.set_ylabel(y_title)
        st.pyplot(fig)
        
def plot2(df,x,title,x_title,y_title):
    fig,ax=plt.subplots(figsize=(5,5))
    ax=sns.countplot(x,hue=x)
    ax.set_title(title)
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    total=float(len(df))
    for p in ax.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/total)
        x = p.get_x() + p.get_width()
        y = p.get_height()
        ax.annotate(percentage, (x, y),ha='center')
    st.pyplot(fig)
    


def main():
    
    l2=pd.read_csv("C://Data//l2_operator.csv")
    l3=pd.read_csv("C://Data//L3_operator.csv")
    
    l2_loginId=l2["L2LoginID"].unique().tolist()
    l2_loginId.sort()
    l3_loginId=l3["L3LoginID"].unique().tolist()
    l3_loginId.sort()
    
    
    
    
    st.title("Airport Security Analytics")
    choices={1:"Individual Performance of operator",2:"Overall Performance of operator"}
    def form_func(option):
        return choices[option]
    
    
    Performance=st.sidebar.selectbox("Operator Performance", options=list(choices.keys()),format_func=form_func)
    if Performance==2:
        col1,col2=st.columns([2,2])
        operator=st.sidebar.radio("Select Operator",("L2 operator","L3 operator") )
        if operator=="L2 operator":
        
            L2LoginId=st.sidebar.selectbox("L2 Login ID", l2_loginId)
            df=l2.loc[l2["L2LoginID"]==L2LoginId,]
            with col1:
                plot(df["L2Decision"],df["timesecs1"],"Operator decision with time","Decision","Time")
            with col2:
                plot2(df,df["performance"],"Overall Performance","Performance","Performance count")
            
        else: 
            L3LoginID=st.sidebar.selectbox("L3 Login IDs", l3_loginId)
            
            df=l3.loc[l3["L3LoginID"]==L3LoginID,]
            
            with col1:
                plot(df["L3Decision"],df["timesecs2"],"Operator decision with time","Decision","Time")
            with col2:
                plot2(df,df["performance"],"Overall performance","Performance","Performance count")
        
    elif Performance==1:
        operator=st.sidebar.radio("Select Operator",("L2 operator","L3 operator") )
        if operator=="L2 operator":
            
            st.write("L2 operator performance")
            
            L2LoginId=st.selectbox("L2 Login ID", l2_loginId)
            
            
            L2Time=st.number_input("Time in secs")
            if L2Time<=25:
                L2Decision_selection=st.selectbox("L2 Decision",options=("Select the decision","Accept","Reject"))
                if L2Decision_selection=="Accept":
                    decision=0
                else:
                    decision=1
            
            else:
                L2Decision_selection=st.selectbox("L2 Decision", options=("Select the decision","Time out"))
                if L2Decision_selection=="Time out":
                    decision=2
                
            
            
            if st.button("Predict"):
                result=L2predict(L2LoginId,decision,L2Time)
                #st.write(result)
                st.write("Performance of operator is: "+result)
                
                
                
            
        else:
            st.write("L3 Operator performance")
            L3LoginID=st.selectbox("L3 Login IDs", l3_loginId)
            
            L3Time=st.number_input("Time in secs")
            
            #l3_decision=l3["L3Decision"].unique().tolist()
            if L3Time<=60:
                L3Decision_select=st.selectbox("L3 Decision",options=("Select the decision","Accept","Reject"))
                
                if L3Decision_select=="Reject":
                    decision=1
                else:
                    decision=0
                
            else:
                L3Decision_select=st.selectbox("L3 Decision",("Select the decision","Time out"))
                if L3Decision_select=="Time out":
                    decision=2
            
            L3_predict=st.button("Predict")
            if L3_predict:
                result=L3predict(L3LoginID,decision,L3Time)
                #st.write(result)
                st.write("Performance of operator is:"+result)
                
    
                
        
    
if __name__=='__main__':
    main()


    
    
