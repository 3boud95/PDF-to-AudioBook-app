# 📖 PDF Text-to-Speech Reader

A simple Python application that allows you to **select a PDF file and listen to its text being read aloud** using text-to-speech.

The program uses `PyPDF2` to extract text from each page and `pyttsx3` to convert the extracted text into speech.

## ✨ Features

* 📂 Select a PDF file using a file dialog
* 📄 Extract text from every page of the PDF
* 🔊 Read the extracted text aloud
* 🖥️ Works locally without requiring an internet connection
* 🐍 Built entirely with Python

## 🛠️ Technologies Used

* **Python**
* **PyPDF2** - Extracts text from PDF documents
* **pyttsx3** - Converts text into speech
* **Tkinter** - Provides the file selection dialog

## 📋 Requirements

Make sure Python is installed on your computer.

Install the required packages with:

```bash
pip install pyttsx3 PyPDF2
```

> **Note:** `tkinter` is usually included with standard Python installations on Windows and macOS.

## 🚀 How to Run

1. Clone or download this repository.

2. Open a terminal in the project directory.

3. Install the dependencies:

```bash
pip install pyttsx3 PyPDF2
```

4. Run the Python script:

```bash
python main.py
```

5. A file-selection window will appear.

6. Select the PDF you want to listen to.

7. The program will extract the text page by page and read it aloud.

## 🔍 How It Works

The program follows a simple process:

```text
Start
  │
  ▼
Open PDF File Dialog
  │
  ▼
Select PDF
  │
  ▼
Read PDF using PyPDF2
  │
  ▼
Extract text from each page
  │
  ▼
Send text to pyttsx3
  │
  ▼
Read text aloud
  │
  ▼
Next page
  │
  ▼
Finish
```
## ⚠️ Limitations

This is a basic implementation and has some limitations:

* It only works well with PDFs containing selectable/extractable text.
* Scanned PDFs may not work because they contain images rather than actual text.
* There are no controls for pausing, skipping, or stopping playback.
* The voice and speech rate are not currently configurable.
* Formatting from the original PDF may not be preserved.
* PDFs with complex layouts may produce poorly ordered extracted text.

## 🔮 Possible Improvements

Some useful features that could be added later:

* 🎚️ Adjust speech speed
* 🗣️ Select different voices
* ⏸️ Add pause/resume controls
* ⏭️ Skip to a specific page
* 📊 Display the current page number
* 🖥️ Create a graphical user interface
* 📚 Support multiple document formats
* 🔎 Add OCR support for scanned PDFs
* 💾 Remember the user's preferred voice and speed
* 📝 Display the extracted text while it is being read

## 📁 Project Structure

A simple version of the project can look like this:

```text
PDF-Text-to-Speech/
│
├── main.py
└── README.md
```
