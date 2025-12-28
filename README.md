# Bike Sharing Analysis

Proyek ini melakukan analisis data peminjaman sepeda harian, mulai dari EDA hingga visualisasi interaktif dengan Streamlit.

## Dataset
- Dataset: Bike Sharing Dataset (dayy.csv)
- Kolom utama: dteday, season, temp, atemp, hum, windspeed, cnt

## Cara Menjalankan
1. Install library:
pip install -r requirements.txt

markdown
Salin kode
2. Jalankan notebook:
jupyter notebook notebook.ipynb

markdown
Salin kode
3. Jalankan dashboard Streamlit:
streamlit run dashboard.py

markdown
Salin kode

## Insight Utama
- Musim 3 dan bulan 9 memiliki jumlah peminjaman tertinggi.
- Suhu (temp & atemp) berpengaruh positif terhadap peminjaman.
- Kelembapan dan angin sedikit menurunkan peminjaman.
