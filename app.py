import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

st.set_page_config(page_title="Example Application")

st.title("Normal Distribution generator - Utkarsh Gaikwad")

m = st.number_input("Enter Mean : ", min_value=0.00, step=0.01)
s = st.number_input("Enter standard deviation : ", min_value=0.00, step=0.01)

x = np.random.normal(loc=m, scale=s, size=1000)

df = pd.DataFrame(x, columns=['dist'])

fig = px.histogram(data_frame=df, x='dist')

submit = st.button("Plot")

st.subheader("Plotted results : ")
if submit:
    st.plotly_chart(fig)
