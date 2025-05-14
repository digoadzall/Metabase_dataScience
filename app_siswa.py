import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('random_forest_model.pkl')

st.title("Prediksi Status Mahasiswa (Dropout / Enrolled / Graduate)")

st.markdown("### Masukkan data berikut:")

admission_grade = st.slider("Admission Grade", 0.0, 200.0, 120.0)
first_sem_enrolled = st.number_input("Jumlah Mata Kuliah Semester 1", min_value=0, step=1)
second_sem_enrolled = st.number_input("Jumlah Mata Kuliah Semester 2", min_value=0, step=1)

if st.button("Prediksi"):
    input_data = np.array([[admission_grade, first_sem_enrolled, second_sem_enrolled]])
    prediction = model.predict(input_data)[0]
    
    status_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    st.success(f"Prediksi Status Mahasiswa: **{status_map[prediction]}**")
