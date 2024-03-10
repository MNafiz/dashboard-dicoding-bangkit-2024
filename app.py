import pandas as pd
import streamlit as st



zat_colnames = ["PM2.5","PM10","SO2","NO2","CO","O3","TEMP","PRES","DEWP","RAIN","WSPM"]

@st.cache_resource
def load_data():
    data = pd.read_csv("dashboard/main_data.csv")
    data_clean = data.dropna().copy()
    data_clean["date"] = pd.to_datetime(data_clean["year"].astype(str) + "-" + data_clean["month"].astype(str) + "-" + data_clean["day"].astype(str))
    return data_clean[["date"] + zat_colnames]

@st.cache_resource
def explore(zat):
    global data_clean
    data_max = data_clean[["date", zat]].groupby("date").max()
    data_min = data_clean[["date", zat]].groupby("date").min()
    data_mean = data_clean[["date", zat]].groupby("date").mean()

    st.write(f"# Eksplorasi kadar {zat} di Kota Changping")

    st.markdown("---")

    st.write(f"## 1. Eksplorasi Nilai Maksimum Kadar Zat {zat}")
    st.line_chart(data_max)

    st.write(f"## 2. Eksplorasi Nilai Minimum Kadar Zat {zat}")
    st.line_chart(data_min, color="#FF0000")

    st.write(f"## 3. Eksplorasi Siklus Musiman Kadar Zat {zat}")
    st.line_chart(data_mean, color="#008000")



with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

    zat = st.selectbox("Pilih Zat", zat_colnames ,index=None)


data_clean = load_data()

if zat:
    explore(zat)
else:
    st.warning("Pilih zat terlebih dahulu !")