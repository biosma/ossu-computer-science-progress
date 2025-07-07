import os
import string
from collections import defaultdict
import json

def index_documents(folder, stop_words=[]):
    index = defaultdict(lambda: defaultdict(int))
    word_count = defaultdict(int)
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        elif file.endswith(".epub"):
            text = extract_text_epub(path)
        elif file.endswith(".pdf"):
            text = extract_text_pdf(path)
        else:
            continue  # ignores uknown file types
        for word in text.split():
            cleaned_word = clean_word(word)
            if cleaned_word and cleaned_word not in stop_words:
                index[cleaned_word][file] += 1
                word_count[file] += 1
    mod_times = {
        file: os.path.getmtime(os.path.join(folder, file))
        for file in os.listdir(folder)
        if file.endswith((".txt", ".pdf", ".epub"))
    }    
    return index, word_count, mod_times

def save_index(index, word_count, mod_times,file_path='index.json'):
    """ Saves the index and word_count to a json file """
    index_dict = {k: dict(v) for k, v in index.items()}
    data = {'index': index_dict, 'word_count': word_count, "mod_times": mod_times}
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_index(file_path='index.json'):
    """ Loads the index and word_count from a json file """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    index = defaultdict(lambda: defaultdict(int))
    for k, v in data['index'].items():
        for k2, v2 in v.items():
            index[k][k2] = v2
    word_count = data['word_count']
    return index, word_count, data.get("mod_times", {})


def should_update(saved_mod_time, folder='docs'):
    """ Checks if the index should be updated """
    mod_times = {
        file: os.path.getmtime(os.path.join(folder, file))
        for file in os.listdir(folder)
        if file.endswith((".txt", ".pdf", ".epub"))
    }

    if set(saved_mod_time.keys()) != set(mod_times.keys()):
        return True
    for file, mod_time in mod_times.items():
        if saved_mod_time.get(file, 0) < mod_time:
            return True
    return False
