import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header('st.write')
st.write('Hello, *World!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
st.write(df)