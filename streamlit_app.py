import streamlit as st

st.title("Kalkulori")
def hitung_bmr(gender, berat, tinggi, usia):
    if gender == "Laki-laki":
        bmr = 88.36 + (13.4 * berat) + (4.8 * tinggi) - (5.7 * usia)
    else:
        bmr = 447.6 + (9.2 * berat) + (3.1 * tinggi) - (4.3 * usia)
    return bmr

def hitung_kalori(bmr, aktivitas):
    faktor_aktivitas = {
        "Sangat kurang aktif": 1.2,
        "Kurang aktif": 1.375,
        "Cukup aktif": 1.55,
        "Aktif": 1.725,
        "Sangat aktif": 1.9
    }
    return bmr * faktor_aktivitas[aktivitas]

st.title("Kalkulator Kebutuhan Kalori Harian")

gender = st.radio("Pilih Gender:", ["Laki-laki", "Perempuan"])
usia = st.number_input("Usia (tahun):", min_value=1, max_value=120, value=25)
berat = st.number_input("Berat Badan (kg):", min_value=10.0, max_value=300.0, value=70.0, step=0.1)
tinggi = st.number_input("Tinggi Badan (cm):", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
aktivitas = st.selectbox("Tingkat Aktivitas:", ["Sangat kurang aktif", "Kurang aktif", "Cukup aktif", "Aktif", "Sangat aktif"])

if st.button("Hitung Kalori"):
    bmr = hitung_bmr(gender, berat, tinggi, usia)
    kebutuhan_kalori = hitung_kalori(bmr, aktivitas)
    st.success(f"Kebutuhan kalori harian Anda: {kebutuhan_kalori:.2f} kkal")
