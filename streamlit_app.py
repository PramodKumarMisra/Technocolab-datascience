import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image
pickle_in = open("default_of_credit_card_clients.pkl","rb")
classifier=pickle.load(pickle_in)
def welcome():
    return "Welcome All"
def predict_note_authentication(PAY_2,PAY_4,PAY_6,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6,Deafault_amt):
   
    prediction=classifier.predict([[PAY_2,PAY_4,PAY_6,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6,Deafault_amt]])
    print(prediction)
    return prediction

def main():
    st.title("Prediction of Default credit card ")
    html_temp = """
    <style>
    body{
        background-color: #99ffff;
    }
    </style>
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">  Defaulter Credit Card prediction  Machine Learning  App(Under Guidence of Technocolab) </h2>
    <p style ="color:white"> Created By Pramod Kumar</p>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    PAY_2 = st.text_input("PAY_2")
    PAY_4= st.text_input("PAY_4")
    PAY_6 = st.text_input("PAY_6")
    BILL_AMT4 = st.text_input("BILL_AMT4")
    BILL_AMT5 = st.text_input("BILL_AMT5")
    BILL_AMT6 = st.text_input("BILL_AMT6")
    PAY_AMT1 = st.text_input("PAY_AMT1")
    PAY_AMT2 = st.text_input("PAY_AMT2")
    PAY_AMT3 = st.text_input("PAY_AMT3")
    PAY_AMT4 = st.text_input("PAY_AMT4")
    PAY_AMT5 = st.text_input("PAY_AMT5")
    PAY_AMT6 = st.text_input("PAY_AMT6")
    Deafault_amt = st.text_input("default_amout")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(PAY_2,PAY_4,PAY_6,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6,Deafault_amt)
    st.success('The output isss {}'.format(result))
    if st.button("Pramod"):
        st.text("Lets Find  it ")
        st.text("Build with streamlit under guidance of Technocolab")

if __name__=='__main__':
    main()
    