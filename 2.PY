#Instant PDF to Audio Converter
import pyttsx3
import PyPDF2

def speak_pdf(file_path):
    reader = PyPDF2.PdfReader(file_path)
    engine = pyttsx3.init()
    
    for page in reader.pages:
        text = page.extract_text()
        engine.say(text)
        engine.runAndWait()

# speak_pdf('document.pdf')