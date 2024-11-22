import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()


class Static():
    def llm():
        return ChatOpenAI(
            model=os.getenv("OPENAI_MODEL_NAME"),
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.2,
        )
    
    def pageConfig():
        return st.set_page_config(
            page_title="SKAGRI GPT",
            page_icon="🎓",
            layout="centered",
        )

    def logo():
        return st.image('logo.png')
    
    def pageTitle():
        return st.markdown("""
            <div class="header-container" style="margin-top: 1%;">
                <h1 class="header-title">SKAGRI GPT</h1>
                <p class="header-subtitle">Dikembangkan oleh</p>
                <p class="header-team">SMK PGRI SOOKO Developer Team ✨</p>
            </div>
        """, unsafe_allow_html=True)
            
    def pageCss():
        return st.markdown("""
            <style>
                /* Main Container */
                .main {
                    padding: 2rem;
                }
                
                /* Header Styling */
                .header-container {
                    background: linear-gradient(135deg, #155799 0%, #159957 100%);
                    padding: 2rem;
                    border-radius: 0 0 2rem 2rem;
                    margin: -6rem -4rem 2rem -4rem;
                    color: white;
                    text-align: center;
                }
                
                .header-title {
                    font-size: 3.5rem;
                    font-weight: 700;
                    margin-bottom: 0.5rem;
                    background: linear-gradient(120deg, #ffffff, #f0f0f0);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                }
                
                .header-subtitle {
                    font-size: 1.2rem;
                    opacity: 0.9;
                    margin-bottom: 0.5rem;
                }
                
                .header-team {
                    font-size: 1.4rem;
                    font-weight: 600;
                    opacity: 0.95;
                }
                
                /* Search Container */
                .search-container {
                    padding: 2rem;
                    border-radius: 1rem;
                    box-shadow: 0 8px 30px rgba(0,0,0,0.1);
                    margin: 2rem 0;
                }
                
                /* Input Field */
                .stTextInput input {
                    border: 2px solid #e0e0e0;
                    border-radius: 1rem;
                    padding: 1rem;
                    font-size: 1.1rem;
                    width: 100%;
                    transition: all 0.3s ease;
                }
                
                .stTextInput input:focus {
                    border-color: #155799;
                    box-shadow: 0 0 15px rgba(21,87,153,0.2);
                }
                
                /* Button */
                .stButton button {
                    background: linear-gradient(135deg, #155799, #159957);
                    color: white;
                    padding: 0.8rem 2rem;
                    border-radius: 2rem;
                    font-size: 1.1rem;
                    font-weight: 600;
                    width: auto;
                    min-width: 200px;
                    border: none;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                    transition: all 0.3s ease;
                    margin-top: 1rem;
                }
                
                .stButton button:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
                }
                
                /* Result Container */
                .result-container {
                    background: white;
                    padding: 2rem;
                    border-radius: 1rem;
                    box-shadow: 0 8px 30px rgba(0,0,0,0.1);
                    margin: 2rem 0;
                    transition: all 0.3s ease;
                }
                
                /* Loading Spinner */
                .stSpinner {
                    text-align: center;
                    padding: 2rem;
                }
                
                /* Error Message */
                .stAlert {
                    border-radius: 1rem;
                    border: none;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                }
                
                /* Emoji Styling */
                .emoji {
                    font-size: 1.5rem;
                    margin: 0 0.5rem;
                }
                
                /* Responsive Design */
                @media (max-width: 768px) {
                    .header-container {
                        margin: -2rem -1rem 2rem -1rem;
                        padding: 1.5rem;
                    }
                    
                    .header-title {
                        font-size: 2.5rem;
                    }
                    
                    .search-container, .result-container {
                        padding: 1.5rem;
                    }
                }
            </style>
        """, unsafe_allow_html=True)






