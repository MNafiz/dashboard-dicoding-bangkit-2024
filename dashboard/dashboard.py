import pandas as pd
import streamlit as st

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")


data = pd.read_csv("dashboard/main_data.csv")
data_clean = data.dropna().copy()

data_clean["date"] = data_clean["year"].astype(str) + "-" + data_clean["month"].astype(str) + "-" + data_clean["day"].astype(str)
data_clean["date"] = pd.to_datetime(data_clean["date"])

data_max = data_clean[["date", "NO2"]].groupby("date").max()
data_min = data_clean[["date", "NO2"]].groupby("date").min()
data_mean = data_clean[["date", "NO2"]].groupby("date").mean()

st.write("# Eksplorasi kadar NO2 di Kota Changping")

st.markdown("---")

st.write("## 1. Eksplorasi Nilai Maksimum NO2")
st.line_chart(data_max)
st.write("Terlihat bahwa kadar NO2 paling tinggi di kota ChangPing ketika di penghujung tahun (awal tahun atau akhir tahun)")

st.write("## 2. Eksplorasi Nilai Minimum NO2")
st.line_chart(data_min, color="#FF0000")
st.write("Terlihat bahwa kadar NO2 paling rendah di kota ChangPing ketika berada di pertengahan tahun")

st.write("## 3. Eksplorasi Siklus Musiman NO2")
st.line_chart(data_mean, color="#008000")
st.write("Terlihat bahwa kadar NO2 memilikki siklus musiman tiap 1 tahun sekali")
