import matplotlib.pyplot as plt
import os
from collections import Counter

def show_top_words(index, folder="docs", top_n=10):
    counter = Counter()
    print("📚 Choose a file by number:", os.listdir(folder))
    for idx, file in enumerate(os.listdir(folder)):
        print(f"{idx} - {file}") 
    
    try:
        election = int(input("File number: ").strip())
        files = os.listdir(folder)
        if election < 0 or election >= len(files):
            print("❌ Invalid number.")
            return
        file = files[election]
    except (ValueError, IndexError):
        print("❌ Please enter a valid number.")
        return
    for word, count in index.items():
        if file in count:
            counter[word] += count[file]

    if not counter:
        print("📭 Words not found in index")
        return

    top_words = counter.most_common(top_n)
    word, frequency = zip(*top_words)

    plt.figure(figsize=(10, 5))
    plt.bar(word, frequency)
    plt.title(f"Top {top_n} words in {file}")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
  