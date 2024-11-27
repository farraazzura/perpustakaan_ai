from crewai.tools import BaseTool
from langchain.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

load_dotenv()
from langchain_community.tools import TavilySearchResults
os.environ["TAVILY_API_KEY"]=os.getenv("tavilyapi_key")
SearchTool = TavilySearchResults(k=5)

CHROMA_PATH = r"./db"

class RAGTool(BaseTool):
    name: str = "RAGTool"
    description: str = "Search the vector db for related information "

    def _run(self,query:str) -> str:
        """
        Search related information from queries
        """
        embedding_function = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"], allowed_special={'<|endoftext|>'})
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
        try:
            return db.similarity_search_with_relevance_scores(query, k=4)
        except Exception as e:
            return "Tools error"