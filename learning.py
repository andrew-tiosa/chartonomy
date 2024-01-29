import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

""" 
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(r"D:\Machine Data\20230313-BOCI-New-credits.pdf")
pages = loader.load()
len(pages)
print(pages[0].page_content[200:1000])
"""
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter

chunk_size =26
chunk_overlap = 4

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)
c_splitter = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

text1 = 'abcdefghijklmnopqrstuvwxyzvwxyzvwxyzvwxyzvwxyzvwxyzvwxyz'
r_splitter.split_text(text1)
text2 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
c_splitter.split_text(text2)
print(r_splitter.split(text1), r_splitter.split(text2))

def