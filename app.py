# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:50:38 2021

@author: eagle
"""

import streamlit as st
from multiapp import Multipage
from apps import About,Operator_performance,Overall_performance

app=Multipage()

st.title("Baggage Surveillance Analytics")


app.add_app("About", About.app)
app.add_app("Operator Performance",Operator_performance.app)
app.add_app("Overall performance", Overall_performance.app)

app.run()