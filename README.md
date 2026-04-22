# 🚴‍♂️ Bike Sharing Analysis Dashboard

## 📊 Project Overview
Proyek ini merupakan hasil analisis data dari dataset **Bike Sharing** yang bertujuan untuk memahami pola penggunaan penyewaan sepeda. Analisis ini mengeksplorasi pengaruh waktu (jam) terhadap volume penyewaan serta bagaimana faktor kondisi cuaca memengaruhi minat pengguna. Temuan dari proyek ini disajikan dalam bentuk dashboard interaktif menggunakan **Streamlit**.

## 🧐 Pertanyaan Bisnis
1. Bagaimana distribusi penyewaan sepeda per jamnya dan apakah terdapat perbedaan pola antara hari kerja dan hari libur?
2. Sejauh mana kondisi cuaca dan suhu udara memengaruhi total penyewaan sepeda setiap harinya?

## 📂 Struktur Direktori
- `dashboard/`: Berisi kode utama dashboard (`dashboard.py`) dan dataset hasil pembersihan (`day_clean.csv`, `hour_clean.csv`).
- `data/`: Berisi dataset mentah asli (`day.csv`, `hour.csv`).
- `Proyek_Analisis_Data.ipynb`: File Jupyter Notebook yang mencakup seluruh proses analisis (Wrangling, EDA, Visualisasi).
- `README.md`: Dokumentasi proyek.
- `requirements.txt`: Daftar library Python yang digunakan.
- `url.txt`: Keterangan mengenai deployment.

## 💻 Cara Menjalankan
### 1. Persiapan Environment (Local)
Pastikan Anda telah menginstal Anaconda atau Python di komputer Anda. Buka Terminal/Command Prompt, lalu jalankan:
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
### 2. Menjalankan Dashboard
Setelah semua library terinstal, pastikan Anda berada di direktori utama proyek, lalu jalankan perintah berikut:
```bash
streamlit run dashboard/dashboard.py
