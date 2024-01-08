
import pandas as pd 
import pickle
import streamlit as st
import numpy as np
  
  
# loading the saved model
loaded_model = pickle.load(open('/Users/damlaakilveren/sepsis_model.sav', 'rb'))
    
# creating a function for Prediction

from streamlit_option_menu import option_menu

def sepsis_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The Patient May Be Sepsis. Monitoring Closely is Suggested.'
    else:
      return 'The Patient Does Not Show Signs of Sepsis'
  

def main():
    
    # giving a title
    # sidebar for navigation
    with st.sidebar:
        
        selected = option_menu('Sepsis Onset Prediction System',
                              
                              ['Sepsis Prediction',
                               'Detailed Information',
                               'Support and Help'],
                              icons=['activity','heart','person'],
                              default_index=0)
        
    # Sepsis Prediction Page
    if (selected == 'Sepsis Prediction'):
        st.title('Sepsis Prediction Web App')
    
        Hours = st.text_input('Hours Passed Since Admission')
        SystolicBP = st.text_input('Last 1h max. Systolic BP')
        DiastolicBP	= st.text_input('Last 1h max. Diastolic BP')
        pH = st.text_input('Last 1h Avg. pH')
        SO2	= st.text_input('Last 1h Avg. SO2')
        Temperature	= st.text_input('Last 1h Amax. Temp.')
        HeartRate = st.text_input('Last 1h Avg. Heart Rate')
        RespiratoryRate	= st.text_input('Last 1h Avg. Resp. Rate')
        PaCO2 = st.text_input('Last 1h Avg. PaCO2')
        WBC	= st.text_input('Last 1h max. WBC Count')
    
        diagnosis = ''

        if st.button('Sepsis Test Result'):
            diagnosis = sepsis_prediction([Hours,SystolicBP, DiastolicBP, pH, SO2, Temperature, HeartRate, RespiratoryRate, PaCO2, WBC])
    
        st.success(diagnosis)

if __name__ == '__main__': 
    main()
