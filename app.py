import streamlit as st
import pandas as pd

st.title("🌍 AQI Prediction by Area")

df = pd.read_csv("aqi_data.csv")
df = df.dropna(subset=['AQI', 'AQI_Bucket'])

cities = sorted(df['City'].unique())

city = st.selectbox("Select City", cities)

if st.button("Check AQI"):
    city_data = df[df['City'] == city]
    
    if not city_data.empty:
        latest = city_data.iloc[-1]
        st.success(f"AQI: {latest['AQI']}")
        st.info(f"Category: {latest['AQI_Bucket']}")
    else:
        st.error("No Data Found")
