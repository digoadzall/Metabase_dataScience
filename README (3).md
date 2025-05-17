# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah sebuah perusahaan edutech yang berfokus pada layanan pendidikan online. Mereka menghadapi tantangan serius terkait banyaknya siswa yang tidak menyelesaikan studi alias dropout. Untuk membantu pengambilan keputusan dan peningkatan kualitas layanan, perusahaan ingin menggunakan pendekatan data science untuk:

Menganalisis data performa siswa secara menyeluruh.

Mengidentifikasi faktor-faktor utama penyebab dropout.

Membangun sistem prediktif untuk mengetahui risiko dropout siswa sejak dini.

### Permasalahan Bisnis
1. Jumlah siswa yang dropout masih tinggi dan belum diketahui faktor utamanya.
2. Tidak ada alat bantu visualisasi data yang dapat memberikan insight cepat ke tim manajemen.
3. Tidak ada sistem yang mampu memprediksi potensi dropout sebelum terjadi.
4. Belum ada integrasi analisis berbasis data untuk pengambilan keputusan operasional.

### Cakupan Proyek
- Melakukan eksplorasi dan analisis terhadap data performa siswa.
- Membangun visualisasi dalam bentuk dashboard untuk memantau performa siswa.
- Membuat model prediktif menggunakan algoritma machine learning.
- Menyusun dokumentasi lengkap untuk mendukung implementasi solusi berbasis data science.

### Persiapan

Sumber Data
Dataset yang digunakan adalah Students Performance dari Dicoding, yang mencakup atribut seperti:

Umur saat masuk kuliah

Status pembayaran

Nilai semester 1 dan 2

Jenis kelamin

Status beasiswa

Sumber data dapat diakses melalui link berikut:
🔗https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```
1. Persiapkan lingkungan Python
Di Google Colab, kitak tidak usah perlu khawatir tentang mengaktifkan virtual environment. Colab sudah menggunakan Python versi 3.x secara default. kita bisa mengecek versi Python yang sedang digunakan dengan menjalankan perintah ini di Colab:

!python --version

setelah melihat versi 3.7 mari kita lanjutkan ke selanjutnya

Namun, jika perlu, bisa diinstal ulang dengan:

python
Salin
Edit
!pip install pandas scikit-learn joblib seaborn matplotlib

Opsi 2: Local Machine (Anaconda)
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

2. Install dependensi
Jalankan perintah berikut di terminal:

pip install pandas scikit-learn joblib seaborn matplotlib
Jika menggunakan Google Colab, tidak perlu install manual karena library tersebut sudah tersedia.

3. Menjalankan Notebook
Jalankan notebook Jupyter berikut untuk melakukan analisis dan modeling:

📄 ds_submission2.ipynb

Pastikan file data.csv ada di direktori yang sama sebelum menjalankan notebook.

4. Menjalankan Dashboard di Metabase
Metabase digunakan untuk membuat dashboard berbasis visualisasi dari data yang sama.

Langkah-langkah:

Pastikan Metabase telah terinstal dan berjalan secara lokal atau di server.

Upload dataset data.csv ke Metabase dan sambungkan sebagai database (bisa menggunakan koneksi file CSV via SQLite atau Postgres).

Buat dashboard dan tambahkan visualisasi-visualisasi berikut:

- Distribusi siswa berdasarkan status (Dropout, Enrolled, Graduate)
- Dropout berdasarkan gender
- Distribusi usia saat mendaftar
- Korelasi nilai akademik semester dengan status siswa
- Hubungan antara status pembayaran dan beasiswa terhadap dropout
- Gunakan akun berikut untuk login ke Metabase (opsional jika ingin standardisasi akses):

Username: root@mail.com
Password: root123
Dashboard dapat diakses dan digunakan untuk memantau performa siswa serta mengidentifikasi potensi risiko dropout sejak dini.
```

## Business Dashboard
Dashboard telah dibuat menggunakan Metabase untuk membantu Jaya Jaya Institut dalam memantau performa dan status siswa. Dashboard ini mencakup beberapa visualisasi penting, yaitu:
1. Distribusi Siswa Berdasarkan Status
Menampilkan jumlah siswa dalam kategori Dropout, Enrolled, dan Graduate. Visualisasi ini membantu dalam melihat proporsi dropout terhadap total populasi siswa.

2. Analisis Dropout Berdasarkan Gender
Memperlihatkan distribusi gender siswa yang mengalami dropout. Tujuannya untuk mengidentifikasi apakah ada kecenderungan tertentu pada gender tertentu.

3. Distribusi Usia Siswa Saat Mendaftar
Menunjukkan sebaran umur siswa yang dropout. Ini membantu perusahaan memahami apakah usia berperan terhadap risiko putus kuliah.

4. Korelasi Nilai Akademik dan Status Siswa
Visualisasi boxplot nilai semester 1 dan 2 terhadap status dropout menunjukkan bahwa nilai akademik rendah berkorelasi dengan risiko dropout.

5. Pengaruh Pembayaran dan Beasiswa terhadap Dropout
Menampilkan perbandingan status pembayaran (debt) dan kepemilikan beasiswa pada siswa yang dropout. Visualisasi ini penting untuk melihat apakah masalah finansial berkontribusi terhadap putus sekolah.

6. Hubungan antara Status Pembayaran/Beasiswa dengan Dropout
Visualisasi ini membandingkan jumlah siswa dropout berdasarkan status pembayaran (lunas atau memiliki utang) serta status penerima beasiswa. Tujuannya untuk mengetahui apakah kondisi finansial siswa berkorelasi dengan tingkat dropout.


## Menjalankan Sistem Machine Learning
Model prediktif dibangun menggunakan Random Forest Classifier dari scikit-learn untuk memprediksi status siswa.

Langkah Menjalankan Model:
1. Jalankan skrip Python model_training.py untuk melakukan pelatihan model.
2. Model disimpan dalam format .pkl menggunakan joblib:
joblib.dump(model, 'random_forest_model.pkl')

3. File model dapat digunakan untuk prediksi pada data baru dengan memuat kembali model:
model = joblib.load('random_forest_model.pkl')

## Meng-Akses Prototype
Prototype sistem ini telah dibangun menggunakan Streamlit, sebuah framework Python untuk membuat aplikasi berbasis web interaktif.

Cara Menjalankan Prototype (Secara Lokal)
Jika ingin menjalankan prototipe di lokal:

Pastikan streamlit telah terinstal:
pip install streamlit

Jalankan aplikasi:
streamlit run app_siswa.py
link :
https://metabasedatascience-ttblodrtssre4yfqkbdlux.streamlit.app/

## Conclusion
Berdasarkan eksplorasi data dan hasil model:
- Sebagian besar siswa yang dropout memiliki nilai akademik rendah di semester awal dan memiliki status pembayaran tertunda.
- Umur saat mendaftar dan status beasiswa juga memengaruhi kemungkinan dropout.
- Model prediksi (Random Forest) menunjukkan performa baik dalam mengklasifikasikan status siswa dan dapat digunakan sebagai dasar sistem peringatan dini.
- Dashboard memberikan wawasan penting secara visual bagi manajemen untuk mengambil tindakan tepat waktu.

### Rekomendasi Action Items
Action Item 1:
Buat program pendampingan belajar bagi siswa yang memiliki nilai rendah di semester awal.

Action Item 2:
Sediakan skema bantuan pembayaran atau cicilan bagi siswa dengan status pembayaran tertunda agar tidak dropout karena alasan finansial.

Action Item 3:
Gunakan dashboard secara rutin oleh manajemen untuk mengidentifikasi siswa dengan risiko tinggi berdasarkan data terbaru.

Action Item 4:
Kembangkan sistem peringatan berbasis model prediktif internal agar tindakan preventif dapat diambil sebelum siswa keluar.
