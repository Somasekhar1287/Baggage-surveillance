# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 23:02:09 2021

@author: eagle
"""

import streamlit as st

class Multipage():
    def __init__(self):
        self.apps=[]
    
    def add_app(self,title,func):
        self.apps.append({
            "title":title,
            "function":func
            })
        
    def run(self):
        app=st.sidebar.selectbox(
            'Operator Performance',
            self.apps,
            format_func=lambda app: app["title"]
            )
        
        app['function']()