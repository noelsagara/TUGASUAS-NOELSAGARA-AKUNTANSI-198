import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Memuat data
data = pd.read_csv('data.csv')

# 2. Memahami struktur data
print("Beberapa baris pertama dari data:")
print(data.head())

print("\nTipe data dari setiap kolom:")
print(data.dtypes)

# 3. Membersihkan data
# Mengecek nilai yang hilang
print("\nJumlah nilai yang hilang di setiap kolom:")
print(data.isnull().sum())

# Mengisi nilai yang hilang di kolom numerik dengan median dari masing-masing kolom
numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].median())

# 4. Eksplorasi data awal
# Menghitung statistik deskriptif
print("\nStatistik deskriptif:")
print(data.describe())

# Visualisasi dasar
# Histogram untuk distribusi kolom numerik
data.hist(bins=30, figsize=(10, 10))
plt.suptitle('Distribusi Kolom Numerik')
plt.show()

# Scatter plot untuk melihat hubungan antara dua variabel numerik
# Gantilah 'age' dan 'salary' dengan nama kolom yang ingin Anda lihat
sns.scatterplot(x='age', y='salary', data=data)
plt.title('Scatter Plot antara age dan salary')
plt.show()

# Heatmap dari matriks korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap dari Matriks Korelasi')
plt.show()