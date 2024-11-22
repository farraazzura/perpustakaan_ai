import streamlit as st
from crewai import Crew, Process
from static import Static
from agents import Agents
from tasks import Tasks
from database import saveSurvey

Static.pageConfig()
Static.pageCss()
Static.logo()
Static.pageTitle()

with st.container():
    name = st.text_input(
        "Nama Lengkap : ",
        placeholder="Masukkan Nama Lengkap..."
    )
    if not name:
        st.info("❕ Tolong isi Nama Lengkap")
    
    phone = st.text_input(
        "Nomor Telepon : ",
        placeholder="Masukkan Nomor Telepon..."
    )
    if not phone:
        st.info("❕ Tolong isi Nomor Telepon")
    
    category = st.selectbox(
        "Pilihan Kategori Identitas : ",
        ("Pilih Kategori Identitas...", "Guru", "Siswa/Siswi", "Orang Tua/Wali", "Masyarakat Umum")
    )
    if category == "Pilih Kategori Identitas...":
        st.info("❕ Tolong isi Kategori Identitas")

if not (name and phone and category != "Pilih Kategori Identitas..."):
    st.error("❌ Tolong isi Data Pengguna dengan lengkap")
else:
    with st.container():
        topic = st.text_input(
            "Masukkan topik yang ingin kamu cari:",
            placeholder="Contoh: Apa jurusan yang ada?",
            help="Ketik topik yang ingin kamu cari informasinya"
        )
        
        language = st.selectbox(
            "Pilihan menu bahasa : ",
            ("Pilih Bahasa...", "Bahasa Indonesia", "Bahasa Jawa", "Bahasa Inggris")
        )
        
        search_button = st.button("🔍 Mulai Penelitian")

    if search_button:
        if not topic:
            st.error("❌ Tolong masukkan topik penelitian.")
        elif language == "Pilih Bahasa...":
            st.error("❌ Tolong pilih bahasa.")
        else:
            
            crew = Crew(
                agents=[Agents(topic).research_agent()],
                tasks=[Tasks(topic, language).research_task()],
                verbose=True,
                process=Process.sequential
            )

            with st.spinner("🔄 Sedang mencari informasi..."):
                result = crew.kickoff()
                answer = result
                saveSurvey(name, phone, category, topic, language)
                
            st.markdown(result)
