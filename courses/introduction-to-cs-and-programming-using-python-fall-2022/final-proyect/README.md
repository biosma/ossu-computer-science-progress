# 🧠 Mini Search Engine in Python

A simple search engine written in Python that indexes `.txt`, `.pdf`, and `.epub` files, allowing you to search for words, show results by frequency, and visualize the top 10 most frequent words per file.

---

## 🚀 Features

* Support for `.txt`, `.pdf`, and `.epub` files
* Spanish stopwords filtering using `nltk`
* Frequency and percentage calculation per file
* Index persistence using `index.json`
* Automatic detection of modified files (by modification date)
* Bar chart of top 10 most frequent words per file
* Interactive menu with:

  * Word search
  * Graphical top 10 view

---

## 📦 Requirements

* Python 3.8+
* `matplotlib`
* `ebooklib`
* `beautifulsoup4`
* `PyMuPDF` (imported as `fitz`)
* `nltk`

Install everything with:

```bash
pip install matplotlib ebooklib beautifulsoup4 PyMuPDF nltk
```

And make sure to download NLTK stopwords:

```python
import nltk
nltk.download('stopwords')
```

---

## 📁 Expected Structure

```
search_engine/
├── docs/              # Your .txt, .pdf, .epub files
├── main.py            # Main script
└── index.json         # Automatically generated
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Menu options:

* Search for a word
* View top 10 most used words in a file (with bar chart)

The index is saved automatically and only updates if files change.

---

## 📊 Example Output

```
🔎 Browse by word: gato
Word 'gato' appears in the following files:
documento1.txt: 4 times (0.75%)
cuentos.pdf: 2 times (0.30%)
```

Then:

```
2. Top 10 words by file
Choose file: cuentos.pdf
[Bar chart showing top words and frequencies]
```

---

## 🧠 Author

Project built by Gonzalo as part of his self-taught journey through the [OSSU CS Path](https://github.com/ossu/computer-science).

---

## 📘 License

This project is licensed under the MIT License. You are free to use, modify, and share it.
