#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:22:05 2023

@author: apple
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:11:19 2023

@author: apple
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('trained_model.sav','rb'))
heart_model = pickle.load(open('trained_heart_model.sav','rb'))

# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['diabetes Prediction',
                            'Heart disease Prediction'],
                           
                           icons= ['activity','heart'],
                             default_index=0) 
    
# diabetes Prediction page
if (selected == 'diabetes Prediction'):
    
    # page title
    st.title('Diabtetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
  
    col1, col2, col3 = st.columns(3)
  
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
      
    with col2:
      Glucose = st.text_input('Glucose Level')
  
    with col3:
      BloodPressure = st.text_input('Blood Pressure value')
  
    with col1:
      SkinThickness = st.text_input('Skin Thickness value')
  
    with col2:
      Insulin = st.text_input('Insulin Level')
  
    with col3:
      BMI = st.text_input('BMI value')
  
    with col1:
      DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
  
    with col2:
      Age = st.text_input('Age of the Person')
  
  
  # code for Prediction
    diab_diagnosis = ''
  
  # creating a button for Prediction
  
    if st.button('Diabetes Test Result'):
       diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
      
       if (diab_prediction[0] == 1):
        diab_diagnosis = 'The person is diabetic'
       else:
        diab_diagnosis = 'The person is not diabetic'
      
    st.success(diab_diagnosis)

      
  


    
if (selected == 'Heart disaese Prediction'):
    
    st.title('Heart Disease prediction using ML')