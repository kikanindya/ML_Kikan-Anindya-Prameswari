import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

st.title("Bike Sharing Dashboard")
st.markdown("Analisis Data Sepeda: Tren, Musim, dan Faktor Cuaca")

df = pd.read_csv('dayy.csv')
df['dteday'] = pd.to_datetime(df['dteday'])
df_clean = df.drop(columns=['instant','casual','registered'])

st.sidebar.header("Filter Data")
season = st.sidebar.selectbox("Pilih Musim", [1, 2, 3, 4])
df_filtered = df_clean[df_clean['season']==season]

st.subheader("Statistik Deskriptif")
st.dataframe(df_clean.describe().T)

st.subheader("Distribusi Jumlah Peminjaman")
fig, ax = plt.subplots()
sns.histplot(df_clean['cnt'], bins=30, kde=True, color='skyblue', ax=ax)
ax.set_xlabel("Jumlah Peminjaman")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

st.subheader("Korelasi Variabel Cuaca")
corr = df_clean[['temp','atemp','hum','windspeed','cnt']].corr()
st.dataframe(corr)

fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.subheader(f"Rata-rata Peminjaman Sepeda - Musim {season}")
season_avg = df_clean.groupby('season')['cnt'].mean()
st.bar_chart(season_avg)

st.subheader(f"Rata-rata Peminjaman per Bulan - Musim {season}")
month_avg = df_filtered.groupby('mnth')['cnt'].mean()
st.bar_chart(month_avg)

st.subheader("Hubungan Suhu dan Jumlah Peminjaman")
fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=df_filtered, ax=ax)
ax.set_xlabel("Suhu (Normalized)")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

X = df_clean[['temp']]
y = df_clean['cnt']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

st.subheader("Regresi Linear: Prediksi Peminjaman dari Suhu")
st.markdown(f"- Koefisien (slope): {model.coef_[0]:.2f}")
st.markdown(f"- Intercept: {model.intercept_:.2f}")
st.markdown(f"- Mean Squared Error: {mse:.2f}")

st.subheader("Insight Utama")
st.markdown(f"""
- Musim yang dipilih: **{season}**
- Musim 3 memiliki rata-rata peminjaman tertinggi dibanding musim lain.
- Bulan 9 memiliki jumlah peminjaman tertinggi sepanjang tahun.
- Suhu (temp & atemp) berpengaruh positif paling kuat terhadap jumlah peminjaman.
- Kelembapan (hum) sedikit menurunkan peminjaman.
- Angin (windspeed) menurunkan peminjaman.
""")
