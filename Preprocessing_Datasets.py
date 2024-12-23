import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


dataNYC = pd.read_csv('/content/dataset_TSMC2014_NYC.csv')
dataTKY = pd.read_csv('/content/dataset_TSMC2014_TKY.csv')

# Remove data
dataNYC = dataNYC[dataNYC['venueCategory'] == 'Train Station']
dataTKY = dataTKY[dataTKY['venueCategory'] == 'Train Station']

# Memeriksa missing value
dataNYC.isnull().sum()
dataTKY.isnull().sum()

# Memeriksa duplikat data
duplikat=dataNYC[dataNYC.duplicated(keep=False)]
duplikat=dataTKY[dataTKY.duplicated(keep=False)]
# Menghapus Duplikat data
data_cleanedNYC = dataNYC.drop_duplicates()
data_cleanedTKY = dataTKY.drop_duplicates()
print("Jumlah data NYC sebelum : ", dataNYC.shape)
print("Jumlah data NYC setelah : ", data_cleanedNYC.shape)
print("Jumlah data TKY sebelum : ", dataTKY.shape)
print("Jumlah data TKY setelah : ", data_cleanedTKY.shape)

# Merge data
data_cleanedNYC['city'] = 'New York'
data_cleanedTKY['city'] = 'Tokyo'
data = pd.concat([data_cleanedNYC, data_cleanedTKY])

