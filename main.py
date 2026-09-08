import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

book = askopenfilename()
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages)
engine = pyttsx3.init()

for page in reader.pages:
    text = page.extract_text()
    engine.say(text)
    engine.runAndWait()
