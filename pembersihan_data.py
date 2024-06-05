import pandas as pd

# 1. Memuat data
data = pd.read_csv('data.csv')

# Langkah 1: Deteksi dan Perbaikan Nilai yang Hilang (Missing Values)
print("Langkah 1: Deteksi dan Perbaikan Nilai yang Hilang")

# 1.1 Identifikasi kolom yang memiliki nilai yang hilang
print("\nJumlah nilai yang hilang di setiap kolom:")
print(data.isnull().sum())

# 1.2 Gantikan nilai yang hilang pada kolom numerik dengan median dari kolom tersebut
numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].median())

# 1.3 Gantikan nilai yang hilang pada kolom kategorikal dengan mode dari kolom tersebut
categorical_cols = data.select_dtypes(include=['object']).columns
for col in categorical_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Langkah 2: Koreksi Kesalahan dalam Data
print("\nLangkah 2: Koreksi Kesalahan dalam Data")

# 2.1 Perbaiki kesalahan pengetikan pada kolom 'department'
# Misalnya: Jika ada entri seperti 'Financ', ubah menjadi 'Finance'
# Anda dapat menambahkan lebih banyak koreksi sesuai dengan dataset Anda
data['department'] = data['department'].replace({
    'Financ': 'Finance', 
    'Saless': 'Sales',
    'Markting': 'Marketing',
    'Human Resources': 'HR',
    'Information Technology': 'IT'
})

# 2.2 Hapus entri duplikat berdasarkan kolom 'id'
data = data.drop_duplicates(subset='id')

# Langkah 3: Standarisasi Format Data untuk Konsistensi
print("\nLangkah 3: Standarisasi Format Data untuk Konsistensi")

# 3.1 Standarisasi format kolom 'join_date' menjadi format tanggal ('YYYY-MM-DD')
data['join_date'] = pd.to_datetime(data['join_date'], errors='coerce').dt.strftime('%Y-%m-%d')

# 3.2 Pastikan kolom 'name' memiliki format title case
data['name'] = data['name'].str.title()

# Tampilkan data yang sudah dibersihkan
print("\nData yang sudah dibersihkan:")
print(data)

# Simpan data yang sudah dibersihkan ke file baru
data.to_csv('cleaned_data.csv', index=False)
print("\nData yang sudah dibersihkan disimpan ke 'cleaned_data.csv'.")
