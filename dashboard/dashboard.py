import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")
sns.set(style='ticks')

def create_daily_rent_df(df):
    return df.resample(rule='D', on='dteday').agg({"cnt": "sum"}).reset_index()

def create_weather_rent_df(df):
    return df.groupby("weathersit").cnt.mean().reset_index()

def create_hourly_rent_df(df):
    return df.groupby("hr").cnt.mean().reset_index()

day_df = pd.read_csv("dashboard/day_clean.csv")
hour_df = pd.read_csv("dashboard/hour_clean.csv")

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

with st.sidebar:
    # Menggunakan logo bertema sepeda (Open Source Icon)
    st.image("https://cdn-icons-png.flaticon.com/512/2972/2972185.png")
    st.markdown("<h2 style='text-align: center;'>Bike Rent Filter</h2>", unsafe_allow_html=True)
    
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=day_df["dteday"].min(),
        max_value=day_df["dteday"].max(),
        value=[day_df["dteday"].min(), day_df["dteday"].max()]
    )

main_df = day_df[(day_df["dteday"] >= str(start_date)) & (day_df["dteday"] <= str(end_date))]
main_hour_df = hour_df[(hour_df["dteday"] >= str(start_date)) & (hour_df["dteday"] <= str(end_date))]

daily_rent_df = create_daily_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)
hourly_rent_df = create_hourly_rent_df(main_hour_df)

st.title('🚴‍♂️ Bike Sharing Analysis Dashboard')
st.markdown("Dashboard ini menampilkan hasil analisis data penyewaan sepeda berdasarkan tren waktu dan kondisi cuaca.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Order", value=f"{main_df.cnt.sum():,}")
with col2:
    st.metric("Registered Users", value=f"{main_df.registered.sum():,}")
with col3:
    st.metric("Casual Users", value=f"{main_df.casual.sum():,}")

st.divider()

st.subheader('📈 Daily Rental Performance')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(daily_rent_df["dteday"], daily_rent_df["cnt"], marker='o', linewidth=3, color="#2E7D32") # Warna Hijau Hutan
ax.set_title("Tren Penyewaan Harian", fontsize=20)
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

col_left, col_right = st.columns(2)

with col_left:
    st.subheader('⏰ Peak Hours')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x="hr", y="cnt", data=hourly_rent_df, color="#1565C0", linewidth=3, ax=ax)
    ax.set_title("Rata-rata Penyewaan per Jam", fontsize=15)
    st.pyplot(fig)

with col_right:
    st.subheader('🌤 Weather Impact')
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["#81C784", "#FFD54F", "#E57373"] # Hijau, Kuning, Merah
    sns.barplot(x="weathersit", y="cnt", data=weather_rent_df, palette=colors, ax=ax)
    ax.set_title("Rata-rata Penyewaan per Cuaca", fontsize=15)
    st.pyplot(fig)

st.divider()
st.caption('Copyright (c) 2026 | Syahrani R | Informatics Student')
