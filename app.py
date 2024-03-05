import pandas as pd
import streamlit as st

data = pd.read_csv("dashboard/main_data.csv")
data_clean = data.dropna().copy()

data_clean["date"] = data_clean["year"].astype(str) + "-" + data_clean["month"].astype(str) + "-" + data_clean["day"].astype(str)
data_clean["date"] = pd.to_datetime(data_clean["date"])

data_max = data_clean[["date", "NO2"]].groupby("date").max()
data_min = data_clean[["date", "NO2"]].groupby("date").min()

st.write("# Eksplorasi kadar NO2 di Kota Changping")

st.markdown("---")

st.write("## 1. Eksplorasi Nilai Maksimum NO2")
st.line_chart(data_max)
st.write("Terlihat bahwa nilai NO2 paling tinggi di kota ChangPing ketika di penghujung tahun (awal tahun atau akhir tahun)")

st.write("## 2. Eksplorasi Nilai Minimum NO2")
st.line_chart(data_min, color="#FF0000")
st.write("Terlihat bahwa nilai NO2 paling rendah di kota ChangPing ketika berada di pertengahan tahun")

st.write("Berdasarkan kedua visualisasi tersebut, pola NO2 memiliki siklus musiman yaitu tiap 1 tahun sekali")

