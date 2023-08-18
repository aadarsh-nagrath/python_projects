import pyttsx3
import PyPDF2

# pyttsx3 is a text to speech converting library
pdfreader = PyPDF2.PdfReader(open('e:/github/python_projects/Pdf_2_Audio_Converter/021.pdf', 'rb'))
speaker = pyttsx3.init()

full_text = ""

for page in pdfreader.pages:
    text = page.extract_text()
    ctext = text.strip().replace('\n', '')
    full_text += ctext

print(full_text)

speaker.save_to_file(full_text, 'new_audio.mp3')
speaker.runAndWait()
speaker.stop()
