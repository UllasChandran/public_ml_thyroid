# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 01:26:00 2023

@author: Ullas Chandran
"""

# -*- coding: utf-8 -*-

import numpy as np
import pickle 
import streamlit  as st 


loading_model = pickle.load(open("C:/Users/Ullas Chandran/OneDrive/Desktop/PROJECT_THYROID/trained_project_model.sav","rb"))

def check_thyroid(input_data):
  input_data = np.asarray(input_data)
  input_data = input_data.reshape(1,-1)
# model = loading_model.fit(X_train,y_train)
  result = loading_model.predict(input_data)
  if result == [1] :
    return "Patient has Thyroid"
  else :
    return "Patient has no Thyroid"


def thyroid_predict_fun(input_data):
    if input_data[0] == 1:
        return "PATIENT IS THYROID "
    else :
        return "PATIENT IS NOT THYROID"
def main():
    st.title("THYROID DETECTION SYSTEM")
    TSH = st.text_input("ENTER THE VALUE OF TSH")
    T3 = st.text_input("ENTER THE VALUE OF T3")
    TT4 = st.text_input("ENTER THE VALUE OF TT4")
    FTI = st.text_input("ENTER THE VALUE OF FTI")
    
    diagnosis = ""
    
    if st.button("TEST RESULTS" ):
        diagnosis = check_thyroid((TSH,T3,TT4,FTI))
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    