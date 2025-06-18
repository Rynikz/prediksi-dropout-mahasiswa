# Proyek Analisis Prediktif: Mengatasi Masalah Dropout Mahasiswa di Jaya Jaya Institut

- **Nama:** [Isi Nama Lengkap Anda]
- **Email:** [Isi Email Anda]
- **ID Dicoding:** [Isi ID Dicoding Anda]

## Business Understanding

### Latar Belakang Bisnis
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi dengan reputasi yang sangat baik dan telah berdiri sejak tahun 2000. Meskipun telah mencetak banyak lulusan berkualitas, institusi ini menghadapi tantangan signifikan terkait tingginya angka mahasiswa yang tidak menyelesaikan pendidikan (dropout). Tingkat dropout yang tinggi tidak hanya berdampak pada reputasi institusi, tetapi juga pada stabilitas finansial dan moral akademik secara keseluruhan. Oleh karena itu, pihak manajemen ingin mengatasi masalah ini secara proaktif dengan memanfaatkan pendekatan berbasis data.

### Permasalahan Bisnis
Berdasarkan latar belakang tersebut, permasalahan utama yang ingin diselesaikan adalah:
1.  Bagaimana cara mengidentifikasi mahasiswa yang memiliki risiko tinggi untuk dropout sedini mungkin?
2.  Apa saja faktor-faktor kunci (baik akademik, demografis, maupun finansial) yang paling signifikan dalam memengaruhi keputusan seorang mahasiswa untuk dropout?
3.  Bagaimana menyediakan alat bantu yang mudah digunakan bagi manajemen dan staf akademik untuk memonitor tren dropout dan melakukan prediksi secara mandiri?

### Cakupan Proyek
Untuk menjawab permasalahan di atas, proyek ini akan mencakup beberapa hal berikut:
- **Analisis Data Eksploratif (EDA):** Menganalisis dataset performa mahasiswa untuk menemukan pola dan wawasan terkait faktor-faktor yang berkorelasi dengan status dropout.
- **Pengembangan Model Machine Learning:** Membangun dan mengevaluasi model klasifikasi yang dapat memprediksi status mahasiswa (Lulus, Terdaftar, atau Dropout) dengan akurasi dan metrik performa yang baik.
- **Pembuatan Business Dashboard:** Merancang dan membuat dashboard interaktif menggunakan Looker Studio untuk visualisasi data dan monitoring tren performa mahasiswa secara keseluruhan.
- **Pengembangan Prototipe Aplikasi Web:** Membuat prototipe sistem machine learning dalam bentuk aplikasi web menggunakan Streamlit yang memungkinkan pengguna (staf akademik) untuk melakukan prediksi status seorang mahasiswa secara real-time.

---

## Persiapan

### Sumber Data
Dataset yang digunakan dalam proyek ini adalah **"Predict students' dropout and academic success"** yang tersedia di [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success). Dataset ini berisi informasi demografis, sosio-ekonomi, dan performa akademik dari 4.424 mahasiswa.

### Setup Environment
Proyek ini dikerjakan menggunakan bahasa Python. Library utama yang digunakan untuk analisis dan pengembangan adalah sebagai berikut:

streamlit
pandas
scikit-learn
numpy

Versi spesifik dari library ini terdokumentasi dalam file `requirements.txt` yang disertakan dalam proyek.

---

## Business Dashboard
Sebuah dashboard interaktif telah dibuat menggunakan **Looker Studio** untuk membantu manajemen Jaya Jaya Institut dalam memonitor data dan performa mahasiswa secara visual. Dashboard ini dirancang dengan tema gelap yang profesional untuk kenyamanan penggunaan dan fokus pada data.

**Tujuan Dashboard:**
Dashboard ini dirancang untuk memberikan gambaran tingkat tinggi mengenai situasi dropout, mengidentifikasi program studi dengan tingkat dropout tertinggi, dan memahami hubungan antara berbagai faktor dengan status kelulusan.

**Fitur Utama Dashboard:**
- **KPI Utama:** Menampilkan metrik kunci seperti Total Mahasiswa, Tingkat Dropout Aktual, Tingkat Deteksi Model (Recall), dan Presisi Prediksi Model.
- **Filter Interaktif:** Pengguna dapat memfilter data secara dinamis berdasarkan Program Studi, Status Beasiswa, dan Gender.
- **Visualisasi Informatif:** Termasuk grafik distribusi status mahasiswa, tingkat dropout per program studi, dan analisis faktor finansial.
- **Tabel Aksi:** Menyajikan daftar mahasiswa yang diprediksi berisiko tinggi untuk dropout, lengkap dengan data pendukungnya untuk keperluan intervensi.

**Link untuk Mengakses Dashboard:**
[https://lookerstudio.google.com/reporting/c9b1041a-811a-4ca4-a6ce-532817c955dc]

---

## Menjalankan Sistem Machine Learning
Sebagai solusi praktis, sebuah prototipe aplikasi web telah dikembangkan menggunakan Streamlit. Aplikasi ini memungkinkan staf akademik atau dosen wali untuk memasukkan data seorang mahasiswa dan mendapatkan prediksi statusnya secara instan.

**Cara Menjalankan Prototipe:**

1.  **Melalui Link Cloud (Direkomendasikan):**
    Aplikasi ini telah di-deploy ke Streamlit Community Cloud dan dapat diakses oleh siapa saja melalui link berikut tanpa perlu instalasi:
    
    **Link Aplikasi:** [https://prediksi-dropout-mahasiswa-rynikz.streamlit.app/]

2.  **Menjalankan Secara Lokal:**
    Jika ingin menjalankan di komputer lokal, pastikan Anda sudah melakukan setup environment sesuai file `requirements.txt`. Buka terminal di dalam folder proyek dan jalankan perintah berikut:
    ```bash
    streamlit run app.py
    ```

---

## Conclusion
Proyek ini berhasil menunjukkan bahwa pendekatan berbasis data dapat memberikan solusi konkret untuk masalah dropout mahasiswa di Jaya Jaya Institut.

1.  **Faktor Prediktor Utama:** Analisis data secara konsisten menunjukkan bahwa dua faktor memiliki pengaruh paling signifikan terhadap status dropout:
    * **Kinerja Akademik Semester Awal:** Jumlah SKS yang disetujui di semester 1 dan 2 adalah prediktor terkuat. Mahasiswa dengan jumlah SKS lulus yang sangat rendah di awal masa studi memiliki probabilitas dropout yang sangat tinggi.
    * **Status Finansial:** Mahasiswa yang memiliki tunggakan pembayaran UKT (`Tuition fees up to date = 0`) dan berstatus sebagai penunggak utang (`Debtor = 1`) hampir dapat dipastikan akan dropout.

2.  **Performa Model:** Model klasifikasi **Logistic Regression** terpilih sebagai model akhir karena performanya yang baik dan interpretasinya yang mudah. Model ini berhasil di-deploy ke dalam aplikasi web yang fungsional.

### Rekomendasi Action Items
Berdasarkan hasil analisis dan model yang dikembangkan, berikut adalah beberapa rekomendasi tindakan yang dapat diambil oleh Jaya Jaya Institut:

1.  **Implementasikan Sistem Peringatan Dini (Early Warning System) Otomatis:**
    Gunakan dashboard dan model yang ada untuk membuat sistem yang secara otomatis menandai mahasiswa di akhir semester pertama jika mereka memenuhi kriteria risiko tinggi (misalnya: **Jumlah SKS lulus < 6 DAN Pembayaran UKT tidak lancar**). Daftar ini harus langsung diteruskan ke tim bimbingan akademik.

2.  **Adakan Sesi Konseling Wajib untuk Mahasiswa Berisiko:**
    Mahasiswa yang telah ditandai oleh sistem peringatan dini wajib mengikuti sesi konseling dengan dosen wali atau konselor. Tujuannya adalah untuk mengidentifikasi masalah (akademik, finansial, atau pribadi) dan mencari solusi sebelum keputusan dropout diambil.

3.  **Tawarkan Program Bantuan Finansial Secara Proaktif:**
    Gunakan data status pembayaran untuk secara proaktif menawarkan solusi kepada mahasiswa yang kesulitan, seperti program cicilan UKT atau informasi beasiswa. Jangan menunggu mahasiswa mengajukan permohonan saat kondisi sudah terlambat.

4.  **Lakukan Evaluasi Kurikulum pada Program Studi dengan Tingkat Dropout Tertinggi:**
    Gunakan dashboard yang telah dibuat untuk memonitor program studi mana yang secara konsisten memiliki tingkat dropout tertinggi. Lakukan evaluasi mendalam terhadap kurikulum, metode pengajaran, atau beban SKS pada program studi tersebut untuk menemukan akar masalahnya.
