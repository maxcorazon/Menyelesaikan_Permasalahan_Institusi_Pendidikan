import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Jaya Jaya Institut Prediction",
    page_icon="🎓",
    layout="wide"
)

# Load Model, Scaler, dan Data
@st.cache_resource
def load_files():
    try:
        # Load Model & Scaler yang sudah disimpan dari Notebook
        model = joblib.load('model_dropout.joblib')
        scaler = joblib.load('scaler_dropout.joblib')
        
        # Load Data Asli
        df_ref = pd.read_csv('data.csv', delimiter=';') 
        return model, scaler, df_ref
    except Exception as e:
        st.error(f"Error loading files: {e}")
        st.error("Pastikan file 'model_dropout.joblib', 'scaler_dropout.joblib', dan 'data.csv' ada di folder yang sama.")
        return None, None, None

model, scaler, df_ref = load_files()

if model is None:
    st.stop() # Program berhenti jika file tidak ditemukan

# Sidebar Menu
st.sidebar.title("Jaya Jaya Institut")
st.sidebar.write("Sistem Prediksi & Monitoring Siswa")
menu = st.sidebar.radio("Pilih Menu:", ["Beranda", "Prediksi Dropout"])

# Halaman Beranda
if menu == "Beranda":
    st.title("Selamat Datang di Dashboard Jaya Jaya Institut")
    st.markdown("""
    Aplikasi ini adalah Prototype Machine Learning untuk mendeteksi risiko **Dropout** siswa.
    
    **Cara Menggunakan:**
    1. Pilih menu **Prediksi Dropout** di sebelah kiri.
    2. Masukkan data siswa (Nilai, Status Keuangan, dll).
    3. Klik tombol **Prediksi**.
    4. Program akan menampilkan hasil analisis risiko dropout siswa tersebut.
    """)
    
    st.info("Proyek ini dibuat untuk memenuhi submission 'Menyelesaikan Permasalahan Institusi Pendidikan'.")
    
    # Menampilkan data sampel
    st.subheader("Sampel Data Mahasiswa")
    st.dataframe(df_ref.head(5))

# Halaman Prediksi Dropout
elif menu == "Prediksi Dropout":
    st.title("Prediksi Risiko Dropout")
    st.markdown("Masukkan data terbaru siswa untuk melihat probabilitas kelulusan.")
    
    # Buat Form agar rapi
    with st.form("prediction_form"):
        st.subheader("1. Data Akademik")
        col1, col2 = st.columns(2)
        
        # Input Nilai (Rentang 0 - 20 sesuai dataset asli)
        grade_sem1 = col1.number_input("Nilai Semester 1 (Skala 0-20)", min_value=0.0, max_value=20.0, value=12.0)
        grade_sem2 = col2.number_input("Nilai Semester 2 (Skala 0-20)", min_value=0.0, max_value=20.0, value=12.0)
        
        st.subheader("2. Data Keuangan")
        col3, col4 = st.columns(2)
        
        # 1=Lancar, 0=Nunggak
        tuition_fees = col3.selectbox("Status Uang Kuliah", [1, 0], format_func=lambda x: "Lancar" if x == 1 else "Nunggak")
        # 1=Ada Hutang, 0=Tidak
        debtor = col4.selectbox("Memiliki Hutang?", [0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
        scholarship = st.selectbox("Penerima Beasiswa?", [0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
        
        st.subheader("3. Data Pribadi")
        col5, col6 = st.columns(2)
        
        age = col5.number_input("Usia saat Mendaftar", min_value=17, max_value=70, value=20)
        gender = col6.selectbox("Gender", [1, 0], format_func=lambda x: "Laki-laki" if x == 1 else "Perempuan")
        
        # Tombol Submit
        submit_btn = st.form_submit_button("Lakukan Prediksi")

    # Proses Prediksi
    if submit_btn:
        # Tahap 1: Siapkan Data Default
        # Ambil rata-rata dari seluruh data sebagai nilai default untuk kolom yang tidak diinput user
        input_data = df_ref.drop(columns=['Status']).mean().to_dict()
        
        # Tahap 2: Timpa dengan Input User
        # Pastikan nama key-nya sama persis dengan nama kolom di CSV
        # Cari nama kolom yang mengandung 'grade' dan '1st_sem'
        col_grade1 = [c for c in df_ref.columns if '1st_sem' in c and 'grade' in c][0]
        col_grade2 = [c for c in df_ref.columns if '2nd_sem' in c and 'grade' in c][0]
        
        input_data[col_grade1] = grade_sem1
        input_data[col_grade2] = grade_sem2
        input_data['Tuition_fees_up_to_date'] = tuition_fees
        input_data['Debtor'] = debtor
        input_data['Scholarship_holder'] = scholarship
        input_data['Age_at_enrollment'] = age
        input_data['Gender'] = gender
        
        # Tahap 3: Buat DataFrame dari input tadi
        input_df = pd.DataFrame([input_data])
        
        # Tahap 4: Scaling Data
        input_scaled = scaler.transform(input_df)
        
        # Tahap 5: Prediksi
        prediksi = model.predict(input_scaled)[0]     # 0 = Graduate, 1 = Dropout
        peluang = model.predict_proba(input_scaled)   # Probabilitas
        peluang_dropout = peluang[0][1]
        
        # Tahap 6: Tampilkan Hasil
        st.markdown("---")
        st.subheader("Hasil Analisis Sistem:")
        
        if prediksi == 1: # Dropout
            st.error(f"**Beresiko Tinggi (High Risk)**")
            st.write(f"Probabilitas Dropout: **{peluang_dropout:.1%}**")
            st.warning("Rekomendasi: Segera hubungi siswa ini untuk diberikan bimbingan khusus.")
            
            # Bar chart probabilitas
            st.progress(int(peluang_dropout * 100))
            
        else: # Graduate
            st.success(f"**Aman (Low Risk)**")
            st.write(f"Probabilitas Dropout: **{peluang_dropout:.1%}** (Kemungkinan Lulus Tinggi)")
            st.info("Pertahankan performa ini.")
            st.progress(int(peluang_dropout * 100))