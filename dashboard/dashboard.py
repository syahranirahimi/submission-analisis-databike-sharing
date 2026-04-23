import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")
sns.set(style='ticks')

# --- Helper Functions ---
def create_daily_rent_df(df):
    return df.resample(rule='D', on='dteday').agg({"cnt": "sum"}).reset_index()

def create_weather_rent_df(df):
    weather_mapping = {1: "Cerah", 2: "Mendung", 3: "Hujan Ringan", 4: "Ekstrem"}
    df_copy = df.copy()
    df_copy["weathersit_label"] = df_copy["weathersit"].map(weather_mapping)
    return df_copy.groupby("weathersit_label", observed=False).cnt.mean().sort_values(ascending=False).reset_index()

def create_hourly_rent_df(df):
    return df.groupby(by=["workingday", "hr"], observed=False).cnt.mean().reset_index()

# --- Load Data ---
current_dir = os.path.dirname(os.path.abspath(__file__))
path_day = os.path.join(current_dir, "all_data_day.csv")
path_hour = os.path.join(current_dir, "all_data_hour.csv")

day_df = pd.read_csv(path_day)
hour_df = pd.read_csv(path_hour)

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2972/2972185.png")
    # PERBAIKAN DI SINI: unsafe_allow_html=True
    st.markdown("<h2 style='text-align: center;'>Bike Rent Filter</h2>", unsafe_allow_html=True)
    
    date_range = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=day_df["dteday"].min(),
        max_value=day_df["dteday"].max(),
        value=[day_df["dteday"].min(), day_df["dteday"].max()]
    )

# Logic Filter
if len(date_range) == 2:
    start_date, end_date = date_range
    main_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & (day_df["dteday"] <= pd.to_datetime(end_date))]
    main_hour_df = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) & (hour_df["dteday"] <= pd.to_datetime(end_date))]
else:
    main_df = day_df
    main_hour_df = hour_df

daily_rent_df = create_daily_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)
hourly_rent_df = create_hourly_rent_df(main_hour_df)

# --- Main Page ---
st.title('🚴‍♂️ Bike Sharing Analysis Dashboard')

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Order", value=f"{main_df.cnt.sum():,}")
with col2:
    st.metric("Registered Users", value=f"{main_df.registered.sum():,}")
with col3:
    st.metric("Casual Users", value=f"{main_df.casual.sum():,}")

st.divider()

# 1. Daily Rental Performance
st.subheader('📈 Daily Rental Performance')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(daily_rent_df["dteday"], daily_rent_df["cnt"], marker='o', linewidth=2, color="#72BCD4")
ax.set_title("Tren Penyewaan Harian", fontsize=20)
ax.set_ylabel("Jumlah Penyewaan")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

col_left, col_right = st.columns(2)

with col_left:
    # 2. Peak Hours (Warna Sinkron: Kerja=Hijau, Libur=Oranye)
    st.subheader('⏰ Peak Hours: Working Day vs Weekend')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Palette 0=Libur (Oranye), 1=Kerja (Hijau)
    sns.lineplot(
        data=hourly_rent_df, 
        x="hr", y="cnt", 
        hue="workingday", 
        palette={0: "#FF914D", 1: "#2E7D32"}, 
        marker="o", 
        ax=ax
    )
    
    ax.set_title("Rata-rata Penyewaan per Jam", fontsize=15)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, ["Hari Libur", "Hari Kerja"], title="Status Hari")
    st.pyplot(fig)

with col_right:
    # 3. Weather Impact (Warna Seragam & Highlight Hijau untuk Cerah)
    st.subheader('🌤 Weather Impact')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Hijau untuk bar tertinggi (index 0), Abu-abu untuk lainnya
    colors = ["#2E7D32" if i == 0 else "#D3D3D3" for i in range(len(weather_rent_df))]
    
    sns.barplot(x="cnt", y="weathersit_label", data=weather_rent_df, palette=colors, ax=ax)
    ax.set_title("Rata-rata Penyewaan Berdasarkan Kondisi Cuaca", fontsize=15)
    ax.set_xlabel("Rata-rata Penyewaan")
    st.pyplot(fig)

st.divider()
st.caption('Copyright (c) 2026 | Syahrani R | Informatics Student')
