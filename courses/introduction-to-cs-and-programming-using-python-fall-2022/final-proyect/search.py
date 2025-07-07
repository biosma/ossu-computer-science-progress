def word_browser(word, index, word_count):
    cleaned_word = clean_word(word)
    if cleaned_word not in index:
        print(f"Word '{word}' not found in index")
        return

    apareances = index[cleaned_word]
    results = sorted(apareances.items(), key=lambda x: x[1], reverse=True)
    print(f"Word '{word}' appears in the following files:")
    for file, count in results:
        total = word_count[file]
        percentage = count / total * 100 if total > 0 else 0
        print(f"{file}: {count} times ({percentage:.2f}%)")
