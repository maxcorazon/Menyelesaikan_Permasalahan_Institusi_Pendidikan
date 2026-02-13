# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi ini telah meluluskan banyak siswa berprestasi. Namun, terdapat permasalahan krusial berupa tingginya angka mahasiswa yang tidak menyelesaikan pendidikannya (dropout).

Tingginya angka dropout ini berdampak negatif pada reputasi institusi dan juga stabilitas finansial operasional kampus. Oleh karena itu, diperlukan solusi berbasis data untuk mendeteksi faktor penyebab dropout dan memprediksi siswa yang berisiko agar dapat diberikan bimbingan secepatnya.

### Permasalahan Bisnis

Permasalahan utama yang dihadapi adalah:

- Tingginya Dropout: Sekolah kesulitan menekan angka siswa yang berhenti di tengah jalan.

- Keterbatasan Deteksi Dini: Belum adanya sistem otomatis yang dapat memprediksi apakah seorang siswa berpotensi dropout atau lulus berdasarkan data historis mereka.

- Kurangnya Monitoring Visual: Institusi kesulitan memantau tren dan faktor penyebab dropout secara real-time karena belum adanya dashboard yang terintegrasi.

### Cakupan Proyek

- Exploratory Data Analysis (EDA): Menganalisis dataset untuk menemukan pola dan faktor dominan penyebab dropout (seperti faktor ekonomi, akademik, dan demografi).

- Business Dashboard: Membuat dashboard interaktif menggunakan Tableau untuk memvisualisasikan persebaran data dan performa siswa.

- Machine Learning Modeling: Membangun model prediksi menggunakan algoritma Logistic Regression untuk mengklasifikasikan status siswa (Graduate vs Dropout).

- Deployment Prototype: Mengembangkan aplikasi berbasis web menggunakan Streamlit agar model dapat digunakan dengan mudah oleh Manajemen Institut.

### Persiapan

Sumber data: Dataset yang digunakan adalah data historis siswa Jaya Jaya Institut (format .csv) yang mencakup informasi demografi, status sosial-ekonomi, dan performa akademik.

Setup environment:
Pastikan Python sudah terinstal, lalu jalankan perintah berikut di terminal untuk menginstal library yang dibutuhkan:

```
# Membuat virtual environment (Opsional)
python -m venv venv
source venv/bin/activate  # Untuk Mac/Linux
venv\Scripts\activate     # Untuk Windows

# Menginstall library yang dibutuhkan
pip install -r requirements.txt

```

## Business Dashboard

Saya telah membuat dashboard interaktif menggunakan Tableau Public untuk memonitor performa mahasiswa. Dashboard ini memberikan wawasan visual mengenai:

- Status Mahasiswa: Ringkasan jumlah siswa yang Lulus, Masih Aktif, dan Dropout.

- Faktor Ekonomi: Korelasi antara status pembayaran uang sekolah (Tuition Fees) dengan tingkat kelulusan.

- Faktor Akademik: Hubungan antara nilai semester 1 dengan risiko dropout.

- Distribusi Usia: Pola sebaran usia siswa saat mendaftar dan pengaruhnya terhadap keberhasilan studi.

Link : https://public.tableau.com/shared/2NGS3QC4G?:display_count=n&:origin=viz_share_link

## Menjalankan Sistem Machine Learning

Prototype sistem prediksi ini dibangun menggunakan Streamlit. Aplikasi digunakan untuk memasukkan data terbaru mahasiswa (seperti nilai, status pembayaran, dan usia) dan mendapatkan hasil prediksi probabilitas dropout secara real-time.
Cara menjalankan prototype secara lokal:

Pastikan seluruh library sudah terinstal.

Buka terminal dan arahkan ke direktori proyek.

Jalankan perintah berikut:

```
# Membuat virtual environment (Opsional)
python -m venv venv
source venv/bin/activate  # Untuk Mac/Linux
venv\Scripts\activate     # Untuk Windows

# Menginstall library yang dibutuhkan
pip install -r requirements.txt

# Menjalankan Sistem Machine Learning Lokakl
streamlit run dashboard.py
```

Prototype ini juga telah di deploy ke Streamlit Cloud sehingga dapat diakses secara daring tanpa instalasi lokal.

Link : https://menyelesaikanpermasalahaninstitusipendidikan.streamlit.app/

## Conclusion

**Faktor Utama Penyebab Dropout**
Dari hasil analisis, ditemukan tiga indikator utama yang paling mempengaruhi keputusan siswa untuk berhenti sekolah:

- Masalah Finansial : Siswa yang menunggak pembayaran uang sekolah (Tuition_fees_up_to_date = 0) memiliki kecenderungan sangat tinggi untuk dropout.

- Performa Akademik Awal : Nilai semester 1 (Curricular_units_1st_sem_grade) yang rendah menjadi sinyal peringatan yang kuat. Siswa dengan nilai rendah di awal semester lebih rentan gagal.

- Faktor Usia : Siswa yang mendaftar di usia matang (di atas 25 tahun) memiliki tingkat risiko dropout yang lebih tinggi dibandingkan siswa yang mendaftar pada usia muda.

### Rekomendasi Action Items

- Restrukturisasi Pembayaran & Beasiswa : Tawarkan opsi cicilan atau bantuan finansial khusus bagi siswa yang terdeteksi menunggak namun memiliki performa akademik yang baik.

- Program Mentoring : Wajibkan sesi bimbingan tambahan bagi siswa Semester 1 dengan nilai rendah untuk mencegah kegagalan studi sejak dini.

- Monitoring via Dashboard & Aplikasi : Gunakan dashboard dan aplikasi prediksi secara rutin untuk mendeteksi dan melakukan pendekatan personal kepada siswa berisiko tinggi (High Risk) sebelum terlambat.
