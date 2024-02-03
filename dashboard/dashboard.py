import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='dark')

# Load data
bikeSharing_df = pd.read_csv("C:/Users/bagus/Downloads/dashboard/all_data.csv") 

# Mapping label cuaca
weather_cond = {
    1: 'Jernih',
    2: 'Kabut',
    3: 'Curah Hujan Ringan',
    4: 'Curah Hujan Lebat'
}

bikeSharing_df['weather_cond'] = bikeSharing_df['weathersit_daily'].map(weather_cond)

# Mapping label musim
season_mapping = {
    1: 'Musim Dingin',
    2: 'Musim Semi',
    3: 'Musim Panas',
    4: 'Musim Gugur'
}

bikeSharing_df['season_name'] = bikeSharing_df['season_daily'].map(season_mapping)

# Streamlit App
st.title('Dashboard Analisis Data Bike Sharing')

# Sidebar
st.sidebar.title('Pilih Analisis Data:')
analysis_choice = st.sidebar.selectbox('Pilihan Analisis', ['Pengaruh Cuaca', 'Perbedaan Sewa', 'Tren Persewaan Sepeda'])

# Analisis 1: Pengaruh cuaca pada persewaan sepeda per harinya (bar chart)
if analysis_choice == 'Pengaruh Cuaca':
    st.subheader('Pengaruh Cuaca pada Persewaan Sepeda per Hari')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weather_cond', y='cnt_daily', data=bikeSharing_df, palette='coolwarm', ax=ax)
    plt.title('Rata-rata Persewaan Sepeda per Cuaca')
    plt.xlabel('Cuaca')
    plt.ylabel('Rata-rata Persewaan Sepeda')
    st.pyplot(fig)

# Analisis 2: Perbedaan sewa pada workingday dan holiday (bar chart)
elif analysis_choice == 'Perbedaan Sewa':
    st.subheader('Perbedaan Sewa pada Workingday dan Holiday')
    fig, ax = plt.subplots(figsize=(10, 6))
    workingday_holiday_rentals = bikeSharing_df.groupby('workingday_daily')['cnt_daily'].mean()
    workingday_holiday_rentals.plot(kind='bar', color=['green', 'orange'], ax=ax)
    plt.title('Rata-rata Persewaan Sepeda pada Workingday dan Holiday')
    plt.xlabel('Hari')
    plt.ylabel('Rata-rata Persewaan Sepeda')
    plt.xticks([0, 1], ['Holiday', 'Workingday'], rotation=0)
    st.pyplot(fig)

# Analisis 3: Pada musim apa persewaan sepeda mengalami tren tertinggi (boxplot)
elif analysis_choice == 'Tren Persewaan Sepeda':
    st.subheader('Tren Persewaan Sepeda per Musim')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='season_name', y='cnt_daily', data=bikeSharing_df, palette='viridis', ax=ax)
    plt.title('Persewaan Sepeda per Musim (Boxplot)')
    plt.xlabel('Musim')
    plt.ylabel('Persewaan Sepeda')
    st.pyplot(fig)
