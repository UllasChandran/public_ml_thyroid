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
hyper_loading_model = pickle.load(open("trained_hyper_model.sav","rb"))


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
  
  
  
  



  from sklearn.decomposition import PCA
  pca = PCA(n_components=10)

  v = pca.fit_transform(input_data)

  X_pca = pd.DataFrame(data = v, columns = ['component_1', 'component_2', 'component_3', 'component_4', 'component_5', 'component_6', 'component_7', 'component_8', 'component_9','component_10'])

  from sklearn.preprocessing import MinMaxScaler
  scaler = MinMaxScaler()
  for i in X_pca.columns:
    X_pca[i] = scaler.fit_transform(X_pca[[i]])
# model = loading_model.fit(X_train,y_train)
  result = hyper_loading_model.predict(input_data)
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
        diagnosis = check_hypothyroid((TSH,T3,TT4,FTI))
        
    st.success(diagnosis)
    
if (selected == "Hyperthyroid system") :
    st.title("HYPERTHYROID PREDICTION SYSTEM")
    TSH = st.text_input("ENTER THE VALUE OF TSH")
    T3 = st.text_input("ENTER THE VALUE OF T3")
    TT4 = st.text_input("ENTER THE VALUE OF TT4")
    FTI = st.text_input("ENTER THE VALUE OF FTI")
    
    
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
        diagnosis = check_hyperthyroid((TSH,T3,TT4,FTI))
        
    st.success(diagnosis)

  
