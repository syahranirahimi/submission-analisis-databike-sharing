# 🚴‍♂️ Bike Sharing Analysis Dashboard

## 📊 Project Overview
Proyek ini bertujuan untuk melakukan analisis mendalam terhadap dataset **Bike Sharing** guna mengungkap pola perilaku pengguna dalam penyewaan sepeda. Fokus utama analisis ini mencakup:
1. Analisis Tren Waktu: Mengeksplorasi perbedaan pola penyewaan antara hari kerja dan hari libur pada jam-jam tertentu.
2. Pengaruh Kondisi Cuaca: Menilai sejauh mana faktor cuaca memengaruhi volume penyewaan harian.
3. Analisis Lanjutan (Binning): Mengelompokkan waktu dalam sehari menjadi beberapa kategori (Pagi, Siang, Sore, Malam) untuk mendapatkan wawasan operasional yang lebih praktis.
Seluruh temuan data divisualisasikan secara interaktif melalui dashboard Streamlit, yang dirancang dengan prinsip desain visual yang informatif untuk mendukung pengambilan keputusan bisnis.

## 🧐 Pertanyaan Bisnis
1. Bagaimana tren jumlah penyewaan sepeda per jam pada hari kerja (workingday) dibandingkan hari libur (weekend) sepanjang periode 2011 hingga 2012?
2. Bagaimana pengaruh variasi kondisi cuaca (cuaca cerah hingga ekstrem) terhadap performa jumlah penyewaan sepeda harian selama tahun 2011-2012?

## 📂 Struktur Direktori
- `dashboard/`: Berisi kode utama dashboard (`dashboard.py`) dan dataset hasil pembersihan (`all_data_day.csv`, `all_data_hour.csv`).
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
```
### 2. Menjalankan Dashboard
Setelah semua library terinstal, pastikan Anda berada di direktori utama proyek (folder submission), lalu jalankan perintah berikut:
```bash
streamlit run dashboard/dashboard.py
```
