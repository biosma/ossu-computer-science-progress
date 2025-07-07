import nltk
import os
from indexing import index_documents, should_update, save_index, load_index
from search import word_browser
from plotting import show_top_words
from file_utils import extract_text_pdf, extract_text_epub, clean_word

def menu():
    print("📚 Menu:")
    print("1. Browse by word")
    print("2. 10 top words by file")
    print("3. Quit")

if __name__ == "__main__":

    if os.path.exists('index.json'):
        index, word_count, mod_times = load_index()
        if should_update(mod_times):
            print("🔄 Updating index...")
            stop_words = nltk.corpus.stopwords.words('spanish')
            index, word_count, mod_times = index_documents("docs", stop_words)
            save_index(index, word_count, mod_times)
    else:
        stop_words = nltk.corpus.stopwords.words('spanish')
        index, word_count, mod_times = index_documents("docs", stop_words)
        save_index(index, word_count, mod_times)

    while True:
        menu()
        option = input("Choose an option: ").strip()
        if option == "1":
            word = input("🔎 Browse by word: ").strip()
            word_browser(word, index, word_count)

        elif option == "2":
            show_top_words(index)
        elif option == "3":
            print("👋 See you soon.")
            break
        else:
            print("⚠️ Invalid Option.")