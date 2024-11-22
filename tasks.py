from crewai import Task
from urlbase import url
from agents import Agents
from tools import webSearch
class Tasks:
    def __init__(self, topic, language):
        self.topic = topic
        self.language = language
        
    def research_task(self):
        return Task(
            description=(
                f"Hey! Mari kita cari tahu buku sesuai {self.buku} di SMKN 9 Malang🔍 "
            ),
            expected_output=(
                f"""
                 ✨ Berikan ringkasan dalam bahasa {self.language} yang:
                
                🗣️ Menggunakan bahasa {self.language} yang gaul & kekinian yang sopan
                🎯 Fokus memberikan rekomendasi sesuai {self.buku}
                ❌ Katakan Maaf jika tidak ada info valid
                
                Format jawaban:
                
                💡 [Judul yang Catchy]
                
                [Paragraf 1 - max 3 baris]
                [Paragraf 2 - max 3 baris] (opsional)
                
                🔍 Sumber: [link valid]
                """
            ),
            agent=Agents(self.topic).research_agent(),
            tools=[webSearch],
        )