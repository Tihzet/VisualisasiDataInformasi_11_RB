import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


dataNYC = pd.read_csv('/content/dataset_TSMC2014_NYC.csv')
dataTKY = pd.read_csv('/content/dataset_TSMC2014_TKY.csv')

# Pertanyaan 1

data['local_time'] = pd.to_datetime(data['utcTimestamp']) + pd.to_timedelta(data['timezoneOffset'], unit='m')
data['hour'] = data['local_time'].dt.hour
data['day'] = data['local_time'].dt.date
bank_data = data[data['venueCategory'] == 'Bank']
grouped = bank_data.groupby(['city', 'venueId', 'hour']).size().reset_index(name='visits')
city_patterns = bank_data.groupby(['city', 'hour']).size().reset_index(name='total_visits')
plt.figure(figsize=(10, 6))
sns.lineplot(data=city_patterns, x='hour', y='total_visits', hue='city', marker='o')
plt.title('Pola Kunjungan Bank Setiap Jam di New York dan Tokyo')
plt.xlabel('Jam dalam sehari')
plt.ylabel('Total Kunjungan')
plt.xticks(range(0, 24))
plt.legend(title='Kota')
plt.grid(True)
plt.show()

# Pertanyaan 2

bank_data = data[data['venueCategory'] == 'Bank']
bank_visits = bank_data.groupby(['city', 'venueId']).size().reset_index(name='total_visits')
city_visits = bank_data.groupby('city').size().reset_index(name='total_visits')
plt.figure(figsize=(10, 6))
sns.barplot(data=city_visits, x='city', y='total_visits', palette='Set2')
plt.title('Total Kunjungan Bank di NYC and Tokyo')
plt.xlabel('Kota')
plt.ylabel('Total Kunjungan')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# Pertanyaan 3

data['utc_time'] = pd.to_datetime(data['utcTimestamp'], utc=True)
data['utc_hour'] = data['utc_time'].dt.hour
utc_activity = data.groupby(['city', 'utc_hour']).size().reset_index(name='activity_count')
plt.figure(figsize=(12, 6))
sns.lineplot(data=utc_activity, x='utc_hour', y='activity_count', hue='city', marker='o')
plt.title('Perbandingan Pengguna Aktif Bank berdasarkan waktu di NYC dan Tokyo')
plt.xlabel('Jam')
plt.ylabel('Pengguna Aktif')
plt.xticks(range(0, 24))
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='City')
plt.show()


