from utils.create_summ import create_summary
from utils.create_todo import create_todolist
from utils.process_data import extract_text_from_txt

from core import API_KEY

from langchain_openai import ChatOpenAI
import os


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=API_KEY
)