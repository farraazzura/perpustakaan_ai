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
                f"Hey! Mari kita cari tahu tentang {self.topic} di SMKN 9 Malang🔍 "
                f"Kita akan fokus mencari info terkini dan akurat dari {url}. "
                "Pastikan sumber informasinya valid ya! 📚"
            ),
            expected_output=(
                f"""
                 ✨ Berikan laporan ringkas dalam bahasa {self.language} yang:
                
                📝 Maksimal 3 baris per paragraf
                🗣️ Menggunakan bahasa {self.language} yang gaul & kekinian yang sopan
                🎯 Fokus menjawab tentang {self.topic}
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