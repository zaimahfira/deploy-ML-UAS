#Import library yang dibutuhkan
import pickle
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = (12, 8);
from PIL import Image

import warnings
warnings.filterwarnings("ignore")

#Masukkan model prediksi yang sudah didownload
model = pickle.load(open('D:/deploy/forecast_model.sav','rb'))

#Masukkan dataset beserta index timeseriesnya
df = pd.read_excel("D:/deploy/Suhu dataset.xlsx")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index(['Year'], inplace=True)

#Buat Tampilan Halaman web
st.set_page_config(layout='centered')
image = Image.open('D:/deploy/gambar.png')
st.image(image)
st.title('Prediksi Suhu Rata-Rata Jakarta')
year = st.slider("Tentukan Tahun Prediksi Kedepan",1,50,step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['Tavg'])

if st.button("Prediksi"):
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['Tavg'].plot(style='--', color='gray', legend=True, label='known')
        pred['Tavg'].plot(color='b', legend=True, label='prediction')
        st.pyplot(fig)