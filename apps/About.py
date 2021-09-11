# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:51:33 2021

@author: eagle
"""

import streamlit as st
import pandas as pd

def app():
    st.title("About page")
    data=pd.read_csv("https://raw.githubusercontent.com/Somasekhar1287/Baggage-surveillance/blob/master/BagTrack%20Report%20new.csv",encoding="ISO-8859-1")
    data.head(20)
