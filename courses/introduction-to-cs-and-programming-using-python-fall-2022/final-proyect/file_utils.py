from ebooklib import epub
from bs4 import BeautifulSoup
import fitz  # PyMuPDF

def extract_text_epub(file_path):
    book = epub.read_epub(file_path)
    text = ""

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_content()
            soup = BeautifulSoup(content, 'html.parser')
            text += soup.get_text() + "\n"

    return text

def extract_text_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text

def clean_word(word):
    return word.strip(string.punctuation).lower()