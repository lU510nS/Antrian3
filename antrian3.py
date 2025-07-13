import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Judul Aplikasi
st.set_page_config(page_title="Simulasi Antrian M/M/1", layout="centered")
st.title("📊 Simulasi Model Antrian M/M/1")
st.markdown("Simulasi dan visualisasi sistem antrian dengan 1 server (loket) berdasarkan parameter λ (kedatangan) dan μ (pelayanan).")

# Input pengguna
λ = st.number_input("🔢 Masukkan rata-rata kedatangan (λ) (pelanggan per jam):", min_value=0.0, value=15.0, step=1.0)
μ = st.number_input("🔧 Masukkan rata-rata pelayanan (μ) (pelanggan per jam):", min_value=0.01, value=20.0, step=1.0)

# Validasi
if λ >= μ:
    st.error("⚠️ Rata-rata kedatangan (λ) harus lebih kecil dari rata-rata pelayanan (μ) agar sistem stabil!")
else:
    # Hitungan metrik antrian
    ρ = λ / μ
    L = λ / (μ - λ)
    W = 1 / (μ - λ)
    Wq = λ / (μ * (μ - λ))
    Lq = λ**2 / (μ * (μ - λ))

    # Menampilkan hasil
    st.subheader("📈 Hasil Perhitungan:")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Tingkat Utilisasi (ρ)", f"{ρ:.2f}")
        st.metric("Jumlah Rata-rata Dalam Sistem (L)", f"{L:.2f}")
        st.metric("Jumlah Rata-rata Dalam Antrean (Lq)", f"{Lq:.2f}")
    with col2:
        st.metric("Waktu Rata-rata Dalam Sistem (W)", f"{W:.2f} jam")
        st.metric("Waktu Rata-rata Dalam Antrean (Wq)", f"{Wq:.2f} jam")

    # Visualisasi Diagram Bar
    st.subheader("📊 Visualisasi Jumlah Pelanggan")
    fig1, ax1 = plt.subplots(figsize=(6,4))
    sns.barplot(x=['Dalam Sistem (L)', 'Dalam Antrean (Lq)'], y=[L, Lq], palette='coolwarm', ax=ax1)
    ax1.set_ylabel('Jumlah Pelanggan')
    ax1.set_title('Perbandingan Pelanggan: Sistem vs Antrean')
    for i, v in enumerate([L, Lq]):
        ax1.text(i, v + 0.1, f"{v:.2f}", ha='center', va='bottom', fontweight='bold')
    st.pyplot(fig1)

    # Visualisasi Waktu Tunggu
    st.subheader("⏱️ Visualisasi Waktu Tunggu")
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.barplot(x=['Dalam Sistem (W)', 'Dalam Antrean (Wq)'], y=[W, Wq], palette='mako', ax=ax2)
    ax2.set_ylabel('Waktu (Jam)')
    ax2.set_title('Perbandingan Waktu: Sistem vs Antrean')
    for i, v in enumerate([W, Wq]):
        ax2.text(i, v + 0.01, f"{v:.2f}", ha='center', va='bottom', fontweight='bold')
    st.pyplot(fig2)

    # Diagram Ilustrasi Teori Antrian
    st.subheader("📥 Ilustrasi Model Antrian M/M/1")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Queueing_theory_diagram.svg/800px-Queueing_theory_diagram.svg.png",
             caption="Model Antrian Sederhana: M/M/1", use_container_width=True)
