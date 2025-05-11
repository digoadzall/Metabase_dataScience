Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
Business Understanding
Jaya Jaya Institut adalah sebuah perusahaan edutech yang berfokus pada layanan pendidikan online. Mereka menghadapi tantangan serius terkait banyaknya siswa yang tidak menyelesaikan studi alias dropout. Untuk membantu pengambilan keputusan dan peningkatan kualitas layanan, perusahaan ingin menggunakan pendekatan data science untuk:

Menganalisis data performa siswa secara menyeluruh.

Mengidentifikasi faktor-faktor utama penyebab dropout.

Membangun sistem prediktif untuk mengetahui risiko dropout siswa sejak dini.

Permasalahan Bisnis
Jumlah siswa yang dropout masih tinggi dan belum diketahui faktor utamanya.

Tidak ada alat bantu visualisasi data yang dapat memberikan insight cepat ke tim manajemen.

Tidak ada sistem yang mampu memprediksi potensi dropout sebelum terjadi.

Belum ada integrasi analisis berbasis data untuk pengambilan keputusan operasional.

Cakupan Proyek
Melakukan eksplorasi dan analisis terhadap data performa siswa.

Membangun visualisasi dalam bentuk dashboard untuk memantau performa siswa.

Membuat model prediktif menggunakan algoritma machine learning.

Menyusun dokumentasi lengkap untuk mendukung implementasi solusi berbasis data science.

Persiapan
Sumber Data: Dataset Students Performance dari Dicoding (turunan dari UCI Machine Learning Repository).
Dataset ini mencakup berbagai atribut seperti umur saat masuk, status pembayaran, nilai semester, jenis kelamin, dan beasiswa.

Setup Environment:

Pastikan Python dan pustaka berikut telah diinstal:

bash
Copy
Edit
pip install pandas matplotlib seaborn scikit-learn joblib
Business Dashboard
Dashboard telah dibuat menggunakan Metabase, yang berisi:

Distribusi siswa berdasarkan status (Dropout, Enrolled, Graduate)

Analisis dropout berdasarkan gender

Distribusi umur siswa saat mendaftar

Korelasi antara nilai semester dan status siswa

Hubungan antara status pembayaran/beasiswa dengan dropout

Akses Dashboard Lokal:
Dashboard dijalankan di lokal melalui http://localhost:3000.

Email: root@mail.com

Password: root123

Anda dapat menyalin database Metabase dengan perintah:

bash
Copy
Edit
docker cp metabase:/metabase.db/metabase.db.mv.db ./
Jika ingin berbagi ke reviewer, dashboard dapat diekspor ke Tableau Public atau Looker Studio.

Menjalankan Sistem Machine Learning
Model prediktif dibangun menggunakan Random Forest Classifier dari scikit-learn untuk memprediksi status siswa.

Langkah Menjalankan Model:
Jalankan skrip Python model_training.py untuk melakukan pelatihan model.

Model disimpan dalam format .pkl menggunakan joblib:

python
Copy
Edit
joblib.dump(model, 'random_forest_model.pkl')
File model dapat digunakan untuk prediksi pada data baru dengan memuat kembali model:

python
Copy
Edit
model = joblib.load('random_forest_model.pkl')
Fitur Penting:
Tuition_fees_up_to_date

Scholarship_holder

Curricular_units_1st_sem_grade

Age_at_enrollment

Gender

dll.

Conclusion
Berdasarkan eksplorasi data dan hasil model:

Sebagian besar siswa yang dropout memiliki nilai akademik rendah di semester awal dan memiliki status pembayaran tertunda.

Umur saat mendaftar dan status beasiswa juga memengaruhi kemungkinan dropout.

Model prediksi (Random Forest) menunjukkan performa baik dalam mengklasifikasikan status siswa dan dapat digunakan sebagai dasar sistem peringatan dini.

Dashboard memberikan wawasan penting secara visual bagi manajemen untuk mengambil tindakan tepat waktu.

Rekomendasi Action Items
Action Item 1:
Buat program pendampingan belajar bagi siswa yang memiliki nilai rendah di semester awal.

Action Item 2:
Sediakan skema bantuan pembayaran atau cicilan bagi siswa dengan status pembayaran tertunda agar tidak dropout karena alasan finansial.

Action Item 3:
Gunakan dashboard secara rutin oleh manajemen untuk mengidentifikasi siswa dengan risiko tinggi berdasarkan data terbaru.

Action Item 4:
Kembangkan sistem peringatan berbasis model prediktif internal agar tindakan preventif dapat diambil sebelum siswa keluar.

