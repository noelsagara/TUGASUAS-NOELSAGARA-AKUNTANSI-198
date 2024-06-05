Soal Kasus Analisis Data Karyawan
Deskripsi Kasus
Perusahaan ABC memiliki data karyawan yang berisi informasi mengenai ID, nama, usia, gaji, departemen, dan tanggal bergabung. Manajemen perusahaan ingin melakukan analisis terhadap data ini untuk memahami distribusi usia dan gaji karyawan, hubungan antara usia dan gaji, serta tren dan distribusi karyawan berdasarkan departemen dan tahun bergabung.

Tugas
1. Memuat Data:
    Muatlah data dari file CSV yang bernama your_data.csv
   
3. Memahami Struktur Data:
    Tampilkan 5 baris pertama dari data yang telah dimuat.
    Tampilkan tipe data dari setiap kolom dalam data.

4. Membersihkan Data:
    Periksa apakah ada nilai yang hilang di setiap kolom dalam data.
    Jika terdapat nilai yang hilang, isilah nilai yang hilang tersebut dengan median dari kolom yang bersangkutan.
   
5. Eksplorasi Data Awal:
    Hitung statistik deskriptif dari kolom numerik dalam data.
    Buat histogram untuk melihat distribusi dari kolom 'age' dan 'salary'.
    Buat scatter plot untuk melihat hubungan antara kolom 'age' dan 'salary'.
    Buat heatmap dari matriks korelasi antara kolom numerik dalam data.
   
6. Analisis Tambahan:
    Hitung rata-rata gaji per department.
    Hitung jumlah karyawan per department.
    Buat bar plot untuk visualisasi jumlah karyawan per department.
    Buat line plot untuk melihat trend jumlah karyawan yang bergabung per tahun.




Hasil :
Gambar 1 
![image](https://github.com/noelsagara/noelsagara_penkodean/assets/166829920/837fa489-3783-4e01-b4cd-6238b5c39eb4)
Interpretasi Grafik: Distribusi Kolom Numerik (Age dan Salary)
Grafik yang ditampilkan adalah histogram untuk kolom 'age' dan 'salary'. Berikut adalah interpretasi dari grafik tersebut:
Grafik Distribusi Age
•	Sumbu X (Horizontal): Menunjukkan rentang usia (age) dari 20 hingga 50 tahun.
•	Sumbu Y (Vertikal): Menunjukkan frekuensi atau jumlah kejadian untuk setiap rentang usia, dalam skala yang tampaknya normalisasi.
Pengamatan dari Grafik:
1.	Rentang Usia 25-30 Tahun:
o	Frekuensi: Bervariasi antara 1 hingga 2.
o	Pengamatan: Rentang usia ini menunjukkan adanya beberapa individu di setiap interval usia, dengan puncak yang jelas pada usia 30 tahun dengan frekuensi 2.
2.	Rentang Usia 30-35 Tahun:
o	Frekuensi: Puncak pada usia 30 tahun dengan frekuensi tertinggi (2).
o	Pengamatan: Usia 30 tahun memiliki jumlah kejadian tertinggi, sedangkan usia lain dalam rentang ini memiliki frekuensi yang lebih rendah dan lebih bervariasi.
3.	Rentang Usia 35-50 Tahun:
o	Frekuensi: Bervariasi antara 0 hingga 1.
o	Pengamatan: Rentang usia ini menunjukkan distribusi yang lebih tersebar dengan frekuensi yang lebih rendah dan lebih bervariasi, dengan tidak ada usia tertentu yang dominan.
Grafik Distribusi Salary
•	Sumbu X (Horizontal): Menunjukkan rentang gaji (salary) dari 40.000 hingga 90.000.
•	Sumbu Y (Vertikal): Menunjukkan frekuensi atau jumlah kejadian untuk setiap rentang gaji, dalam skala yang tampaknya normalisasi.
Pengamatan dari Grafik:
1.	Rentang Gaji 50.000-60.000:
o	Frekuensi: Bervariasi antara 1 hingga 2.
o	Pengamatan: Rentang gaji ini menunjukkan adanya beberapa individu di setiap interval gaji, dengan puncak pada gaji sekitar 60.000 dengan frekuensi 2.
2.	Rentang Gaji 60.000-90.000:
o	Frekuensi: Bervariasi antara 0 hingga 1.
o	Pengamatan: Rentang gaji ini menunjukkan distribusi yang lebih tersebar dengan frekuensi yang lebih rendah dan lebih bervariasi, dengan tidak ada gaji tertentu yang dominan.
Kesimpulan
•	Distribusi Usia: Distribusi usia menunjukkan bahwa sebagian besar individu berada di usia sekitar 30 tahun, dengan distribusi yang lebih tersebar pada usia yang lebih tinggi.
•	Distribusi Gaji: Distribusi gaji menunjukkan bahwa sebagian besar individu memiliki gaji sekitar 50.000 hingga 60.000, dengan distribusi yang lebih tersebar pada gaji yang lebih tinggi.
Secara keseluruhan, grafik ini memberikan gambaran bahwa distribusi usia dan gaji dalam dataset cenderung berkonsentrasi pada nilai-nilai tertentu dengan penyebaran yang lebih luas pada rentang yang lebih tinggi.

Gambar 2 
![image](https://github.com/noelsagara/noelsagara_penkodean/assets/166829920/8482fd0e-72d8-49ef-a08d-630ff1cff8eb)
Interpretasi Grafik: Scatter Plot antara Age dan Salary
Grafik yang ditampilkan adalah scatter plot yang menunjukkan hubungan antara usia (age) dan gaji (salary). Berikut adalah interpretasi dari grafik tersebut:
•	Sumbu X (Horizontal): Menunjukkan usia (age) dari 20 hingga 50 tahun.
•	Sumbu Y (Vertikal): Menunjukkan gaji (salary) dari 40.000 hingga 90.000.
Pengamatan dari Grafik:
1.	Pola Hubungan: Terlihat adanya hubungan positif antara usia dan gaji. Semakin tinggi usia, semakin tinggi gaji yang diterima.
2.	Rentang Usia 20-25 Tahun:
o	Gaji sekitar: 40.000 hingga 50.000.
o	Pengamatan: Individu yang berada pada rentang usia ini cenderung memiliki gaji yang lebih rendah.
3.	Rentang Usia 25-30 Tahun:
o	Gaji sekitar: 45.000 hingga 60.000.
o	Pengamatan: Terjadi kenaikan gaji yang signifikan seiring bertambahnya usia dalam rentang ini.
4.	Rentang Usia 30-35 Tahun:
o	Gaji sekitar: 55.000 hingga 70.000.
o	Pengamatan: Kenaikan gaji terus berlanjut dengan peningkatan yang konsisten.
5.	Rentang Usia 35-40 Tahun:
o	Gaji sekitar: 65.000 hingga 80.000.
o	Pengamatan: Peningkatan gaji lebih terlihat pada rentang usia ini.
6.	Rentang Usia 40-50 Tahun:
o	Gaji sekitar: 75.000 hingga 90.000.
o	Pengamatan: Individu dalam rentang usia ini cenderung memiliki gaji tertinggi.
Kesimpulan:
•	Hubungan Positif: Scatter plot menunjukkan adanya hubungan positif yang kuat antara usia dan gaji. Hal ini berarti seiring dengan bertambahnya usia, gaji cenderung meningkat.
•	Pola Distribusi: Titik-titik data tersebar membentuk pola linear naik, yang menunjukkan peningkatan gaji yang stabil seiring bertambahnya usia.
•	Variabilitas Gaji: Variabilitas atau penyebaran gaji lebih terlihat pada rentang usia yang lebih tinggi (40-50 tahun) dibandingkan rentang usia yang lebih muda.
Secara keseluruhan, grafik ini memberikan gambaran bahwa usia mempengaruhi gaji, di mana individu yang lebih tua cenderung memiliki gaji yang lebih tinggi dibandingkan dengan individu yang lebih muda.




   
