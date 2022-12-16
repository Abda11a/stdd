import streamlit as st
import pandas as pd


file= st.file_uploader ("Input file")
if file is not None :
    df=pd.read_excel (file) 
    st.write(df)
