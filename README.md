# Text Summarizer

This project summarizes long texts into a specified number of concise paragraphs using a transformer model (`facebook/bart-large-cnn`) from Hugging Face. It optionally uses NLTK for sentence tokenization and can be run both locally and on Google Colab.

---

## Features

- Summarizes long texts into 1–n paragraphs
- Powered by Hugging Face Transformers (BART model)
- Optional NLTK-based sentence splitting
- Automatically handles large text inputs by chunking
- Works on CPU (no GPU required)

---

## Setup

### Requirements

Install dependencies using pip:

```bash
pip install transformers torch nltk
