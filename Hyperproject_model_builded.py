# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:25:55 2023

@author: Ullas Chandran
"""


# -*- coding: utf-8 -*-

import numpy as np
import pickle 
import streamlit  as st 
from streamlit_option_menu import option_menu


hypo_loading_model = pickle.load(open("trained_project_model.sav","rb"))
# hyper_loading_model = pickle.load(open("C:/Users/Ullas Chandran/OneDrive/Desktop/PROJECT_THYROID/hyperthyroidmodelnew.sav","rb"))
# hyper_loading_model = pickle.load(open("trained__model.sav","rb"))


def check_hypothyroid(input_data):
  input_data = np.asarray(input_data)
  input_data = input_data.reshape(1,-1)
# model = loading_model.fit(X_train,y_train)
  result = hypo_loading_model.predict(input_data)
  if result == [1] :
    return "Patient has Thyroid"
  else :
    return "Patient has no Thyroid"


def check_hyperthyroid(input_data):
  input_data = np.asarray(input_data)
  input_data = input_data.reshape(1,-1)
  
  result = hypo_loading_model.predict(input_data)
  if result == [1] :
    return "Patient has Thyroid"
  else :
    return "Patient has no Thyroid"

def hypothyroid_predict_fun(input_data):
    if input_data[0] == 1:
        return "PATIENT IS THYROID "
    else :
        return "PATIENT IS NOT THYROID"
    
    
def hyperthyroid_predict_fun(input_data):
    if input_data[0] == 1:
        return "PATIENT IS THYROID "
    else :
        return "PATIENT IS NOT THYROID"
    
    
with st.sidebar :
    selected = option_menu("COMPLETE THYROID PREDICTION SYSTEM",["Hypothyroid system","Hyperthyroid system"] , icons=["heart","person"] , default_index=0)

if (selected == "Hypothyroid system"):
    st.title("HYPOTHYROID PREDICTION SYSTEM")
    
    
    
    TSH = st.text_input("ENTER THE VALUE OF TSH")
    T3 = st.text_input("ENTER THE VALUE OF T3")
    TT4 = st.text_input("ENTER THE VALUE OF TT4")
    FTI = st.text_input("ENTER THE VALUE OF FTI")

    
   # col1 , col2 , col3 ,col4 = st.columns(4)
   # with col1 :
       # TSH = st.text_input("ENTER THE VALUE OF TSH")
    #with col2 :
     #   T3 = st.text_input("ENTER THE VALUE OF T3")
    #with col3 :
     #   TT4 = st.text_input("ENTER THE VALUE OF TT4")
    #with col4 :
     #   FTI = st.text_input("ENTER THE VALUE OF FTI")
    
    diagnosis = ""
    
    if st.button("TEST RESULTS" ):
        if int(TSH) not in range(0,6) :
            st.info("Give TSH Values between 0.5 and 5.0")
        elif int(TT4) not in range(5,13) :
            st.info("Give TT4 Values between 5.0 and 12.0")
        elif int(T3) not in range(80,221) :
            st.info("Give T3 Values between 80 and 220")
        elif int(FTI) not in range(80,221) :
            st.info("Give FTI Values between 80 and 220")
       else :
            diagnosis = check_hypothyroid((TSH,T3,TT4,FTI))
        
    st.success(diagnosis)
    
if (selected == "Hyperthyroid system") :
    st.title("HYPERTHYROID PREDICTION SYSTEM")
    TSH1 = st.text_input("ENTER THE VALUE OF TSH")
    T31 = st.text_input("ENTER THE VALUE OF T3")
    TT41 = st.text_input("ENTER THE VALUE OF TT4")
    FTI1 = st.text_input("ENTER THE VALUE OF FTI")
    
    
    #col1 , col2 , col3 ,col4 = st.columns(4)
    #with col1 :
     #   TSH = st.text_input("ENTER THE VALUE OF TSH")
    #with col2 :
     #   T3 = st.text_input("ENTER THE VALUE OF T3")
    #with col3 :
     #   TT4 = st.text_input("ENTER THE VALUE OF TT4")
    #with col4 :
        #FTI = st.text_input("ENTER THE VALUE OF FTI")
    
    
    
    
    diagnosis = ""
    print("djbjsklkj")
    
    if st.button("TEST RESULTS" ):
        diagnosis = check_hyperthyroid((TSH1,T31,TT41,FTI1))
        
    st.success(diagnosis)

  
