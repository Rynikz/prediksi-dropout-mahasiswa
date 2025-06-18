import streamlit as st
import pandas as pd
import pickle
import numpy as np

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Memuat Model dan Scaler ---
# Menggunakan cache agar model tidak perlu di-load ulang setiap kali ada interaksi
@st.cache_data
def load_assets():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    return model, scaler

model, scaler = load_assets()

# --- Fungsi untuk Prediksi ---
def predict_status(data, model, scaler):
    # Buat DataFrame dari input
    # Urutan kolom HARUS SAMA dengan saat training
    # Di sini kita asumsikan urutan kolom sesuai daftar di bawah
    # Jika model Anda menggunakan semua 36 fitur, Anda harus memasukkan semuanya
    # Untuk prototipe, kita fokus pada fitur-fitur paling penting
    
    # Dapatkan semua nama fitur dari scaler
    feature_names = scaler.get_feature_names_out()
    
    # Buat DataFrame dengan semua fitur dan isi dengan nilai default (misal, 0)
    input_df = pd.DataFrame([data], columns=feature_names)
    
    # Scaling data
    input_scaled = scaler.transform(input_df)
    
    # Prediksi
    prediction = model.predict(input_scaled)
    prediction_proba = model.predict_proba(input_scaled)
    
    return prediction[0], prediction_proba

# --- Antarmuka (UI) Streamlit ---

# Header Utama
st.title("🎓 Prediksi Status Dropout Mahasiswa")
st.write(
    "Aplikasi ini memprediksi status kelulusan seorang mahasiswa (Lulus, Terdaftar, atau Dropout) "
    "berdasarkan data akademik dan demografis. Masukkan data di sidebar kiri."
)

# Sidebar untuk Input Pengguna
st.sidebar.header("Input Data Mahasiswa")

# --- Input Fields ---
# Kita akan gunakan beberapa fitur paling penting yang ditemukan dari analisis sebelumnya
# Anda bisa menambahkan lebih banyak input sesuai dengan semua fitur model Anda

# Akademik
curricular_units_1st_approved = st.sidebar.number_input(
    'SKS Lulus (Semester 1)', min_value=0, max_value=30, value=10,
    help="Jumlah mata kuliah yang disetujui di semester pertama."
)
curricular_units_2nd_approved = st.sidebar.number_input(
    'SKS Lulus (Semester 2)', min_value=0, max_value=30, value=9,
    help="Jumlah mata kuliah yang disetujui di semester kedua."
)
admission_grade = st.sidebar.slider(
    'Nilai Masuk', min_value=0, max_value=200, value=120,
    help="Nilai saat penerimaan mahasiswa baru."
)

# Finansial
tuition_fees_up_to_date = st.sidebar.selectbox(
    'Pembayaran UKT Lancar?', (1, 0), format_func=lambda x: 'Ya' if x == 1 else 'Tidak',
    help="Apakah pembayaran biaya kuliah lancar?"
)
debtor = st.sidebar.selectbox(
    'Memiliki Utang?', (0, 1), format_func=lambda x: 'Ya' if x == 1 else 'Tidak',
    help="Apakah mahasiswa teridentifikasi memiliki utang?"
)
scholarship_holder = st.sidebar.selectbox(
    'Penerima Beasiswa?', (1, 0), format_func=lambda x: 'Ya' if x == 1 else 'Tidak',
    help="Apakah mahasiswa adalah penerima beasiswa?"
)

# Demografi
age_at_enrollment = st.sidebar.slider('Umur Saat Pendaftaran', 17, 70, 20)
gender = st.sidebar.selectbox('Gender', (1, 0), format_func=lambda x: 'Laki-laki' if x == 1 else 'Perempuan')

# --- Tombol Prediksi ---
if st.sidebar.button("Prediksi Status", use_container_width=True):
    # Kumpulkan semua data input ke dalam satu dictionary
    # Nama key HARUS SAMA PERSIS dengan nama kolom saat training
    # Untuk fitur yang tidak ada inputnya, kita isi dengan nilai rata-rata atau median dari data training
    # (Di sini kita sederhanakan dengan mengisi 0, namun praktik terbaik adalah menggunakan mean/median)
    user_input = {
        'Marital status': 1, 'Application mode': 1, 'Application order': 1, 'Course': 9147,
        'Daytime/evening attendance': 1, 'Previous qualification': 1, 'Previous qualification (grade)': 130,
        'Nacionality': 1, "Mother's qualification": 1, "Father's qualification": 1,
        "Mother's occupation": 5, "Father's occupation": 5, 'Admission grade': admission_grade,
        'Displaced': 0, 'Educational special needs': 0, 'Debtor': debtor,
        'Tuition fees up to date': tuition_fees_up_to_date, 'Gender': gender, 'Scholarship holder': scholarship_holder,
        'Age at enrollment': age_at_enrollment, 'International': 0, 'Curricular units 1st sem (credited)': 0,
        'Curricular units 1st sem (enrolled)': 6, 'Curricular units 1st sem (evaluations)': 6,
        'Curricular units 1st sem (approved)': curricular_units_1st_approved,
        'Curricular units 1st sem (grade)': 12, 'Curricular units 1st sem (without evaluations)': 0,
        'Curricular units 2nd sem (credited)': 0, 'Curricular units 2nd sem (enrolled)': 6,
        'Curricular units 2nd sem (evaluations)': 6,
        'Curricular units 2nd sem (approved)': curricular_units_2nd_approved,
        'Curricular units 2nd sem (grade)': 12, 'Curricular units 2nd sem (without evaluations)': 0,
        'Unemployment rate': 12, 'Inflation rate': 1, 'GDP': 0
    }

    # Lakukan prediksi
    prediction, prediction_proba = predict_status(user_input, model, scaler)
    
    # Mapping hasil prediksi ke label yang mudah dibaca
    status_map = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduate'}
    result = status_map[prediction]

    # Tampilkan Hasil
    st.subheader("Hasil Prediksi")
    
    if result == 'Dropout':
        st.error(f"**Status Prediksi: {result}**", icon="🚨")
        st.write("Mahasiswa ini memiliki kemungkinan besar untuk **Dropout**. Perlu perhatian dan bimbingan khusus segera.")
    elif result == 'Enrolled':
        st.warning(f"**Status Prediksi: {result}**", icon="⏳")
        st.write("Mahasiswa ini diprediksi masih **Terdaftar** dan dalam progres. Tetap pantau kinerjanya.")
    else: # Graduate
        st.success(f"**Status Prediksi: {result}**", icon="✅")
        st.write("Mahasiswa ini memiliki kemungkinan besar untuk **Lulus** dengan baik.")

    # Tampilkan Probabilitas
    with st.expander("Lihat Detail Probabilitas"):
        prob_df = pd.DataFrame(prediction_proba, columns=['Dropout', 'Enrolled', 'Graduate'])
        prob_df_renamed = prob_df.rename(index={0: 'Probabilitas'})
        st.dataframe(prob_df_renamed.style.format("{:.2%}"))
        st.bar_chart(prob_df.T)