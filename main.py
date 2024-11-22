import streamlit as st
from crewai import Crew, Process
from static import Static
from agents import Agents
from tasks import Tasks
from database import saveSurvey

# Konfigurasi Halaman
Static.pageConfig()
Static.pageCss()
Static.logo()
Static.pageTitle()

# Input Data Pengguna
with st.container():
    st.header("Informasi Pengguna")
    name = st.text_input("Nama Lengkap :", placeholder="Masukkan Nama Lengkap...")
    phone = st.text_input("Nomor Telepon :", placeholder="Masukkan Nomor Telepon...")
    category = st.selectbox(
        "Kategori Identitas :",
        ["Pilih Kategori Identitas...", "Guru", "Siswa/Siswi", "Orang Tua/Wali", "Masyarakat Umum"]
    )

# Validasi Input Pengguna
if not name or not phone or category == "Pilih Kategori Identitas...":
    st.warning("❕ Pastikan semua data pengguna telah diisi dengan benar.")
else:
    st.success("✅ Data pengguna lengkap.")

    # Input untuk Pencarian Informasi
    with st.container():
        st.header("Pencarian Informasi")
        topic = st.text_input(
            "Topik Pencarian:",
            placeholder="Contoh: Apa jurusan yang ada?",
            help="Ketik topik yang ingin Anda cari informasinya."
        )
        language = st.selectbox("Bahasa:", ["Pilih Bahasa...", "Bahasa Indonesia", "Bahasa Jawa", "Bahasa Inggris"])
        search_button = st.button("🔍 Mulai Penelitian")

        if search_button:
            if not topic:
                st.error("❌ Tolong masukkan topik pencarian.")
            elif language == "Pilih Bahasa...":
                st.error("❌ Tolong pilih bahasa.")
            else:
                # Proses Pencarian
                try:
                    crew = Crew(
                        agents=[Agents(topic).search_book()],
                        tasks=[Tasks(topic, language).research_task()],
                        verbose=True,
                        process=Process.sequential
                    )
                    with st.spinner("🔄 Sedang mencari informasi..."):
                        result = crew.kickoff()
                        saveSurvey(name, phone, category, topic, language)

                    # Tampilkan Hasil
                    st.subheader("Hasil Pencarian:")
                    st.markdown(result)

                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")
