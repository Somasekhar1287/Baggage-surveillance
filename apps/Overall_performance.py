# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:29:15 2021

@author: eagle
"""

import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def plot(x,y,title,x_title,y_title):
        fig,ax=plt.subplots()
        ax=sns.barplot(x,y,hue=x)
        ax.set_title(title)
        ax.set_xlabel(x_title)
        ax.set_ylabel(y_title)
        st.pyplot(fig)
        
def plot2(df,x,title,x_title,y_title):
    fig,ax=plt.subplots()
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
    


def app():
    st.title("Overall Operator Performance")
    l2=pd.read_csv("C://Data//l2_operator_new.csv")
    l3=pd.read_csv("C://Data//l3_operator_new.csv")
    l2_loginId=l2["L2LoginID"].unique().tolist()
    l3_loginId=l3["L3LoginID"].unique().tolist()
    operator=st.sidebar.radio("Select Operator",("L2 operator","L3 operator") )
    if operator=="L2 operator":
        L2LoginId=st.sidebar.selectbox("L2 Login ID", l2_loginId)
        df=l2.loc[l2["L2LoginID"]==L2LoginId,]
        plot(df["L2Decision"],df["timesecs1"],"Operator decision with time","Decision","Time")
        plot2(df,df["performance"],"Overall Performance","Performance","Performance count")
    elif operator=="L3 operator":
        L3LoginId=st.sidebar.selectbox("L3 Login ID", l3_loginId)
        df=l3.loc[l3["L3LoginID"]==L3LoginId,]
        plot(df["L3Decision"],df["timesecs2"],"Operator decision with time","Decision","Time")
        plot2(df,df["performance"],"Overall Performance","Performance","Performance count")
    