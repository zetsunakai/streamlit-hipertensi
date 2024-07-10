import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('penyakit_hipertensi.sav','rb'))

#header
st.title('Prediksi Penyakit Hipertensi')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Umur')
    sex = st.text_input('Jenis Kelamin')
    cp = st.text_input('Jenis nyeri dada')
    trestbps = st.text_input('Tekanan darah')
with col2:
    chol = st.text_input('Kolesterol')
    fbs = st.text_input('Gula darah')
    restecg = st.text_input('Hasil Elektrokardiography')
    thalach = st.text_input('Detak Jantung Max')
with col3:
    exang = st.text_input('Induksi Angina')
    oldpeak = st.text_input('ST Depresi')
    slope = st.text_input('Slope')
    ca = st.text_input('Nilai CA')
    thal = st.text_input('Nilai Thal')

#button prediksi
heart_diagnosis = ''

if st.button('Prediksi'):
    try:
        age = float(age)
        sex = float(sex)
        cp = float(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = float(fbs)
        restecg = float(restecg)
        thalach = float(thalach)
        exang = float(exang)
        oldpeak = float(oldpeak)
        slope = float(slope)
        ca = float(ca)
        thal = float(thal)
    
        heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0]==1):
            heart_diagnosis = 'Pasien Terkena Penyakit Hipertensi'
        else :
            heart_diagnosis = 'Pasien Tidak Terkena Penyakit Hipertensi'

    except ValueError:
        st.error("Pastikan semua input sudah terisi dengan benar dan dalam format numerik.")
st.success(heart_diagnosis)
