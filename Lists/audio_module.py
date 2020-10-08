
import pyttsx3
import PyPDF2
import keyboard
engine=pyttsx3.init()

def onWord(name,location,length):
    print('word',name,location,length)
    if keyboard.is_pressed("d"):
        engine.stop()
engine.connect('started-word',onWord)
#get the voice using voices property
voices=engine.getProperty('voices')
#set the voice of the male with voices[0] and female with voice[1]
engine.setProperty('voice',voices[1].id)
#get the rate of the 

rate=engine.getProperty('rate')
engine.setProperty('rate',125)
pdf = open('C:/Users/dhuli/OneDrive/Desktop/python_tutorial.pdf','rb')
pdfobj=PyPDF2.PdfFileReader(pdf)
k=pdfobj.getNumPages()
for i in range(0,k):
    l=pdfobj.getPage(i)
    engine.say(l.extractText())
    engine.runAndWait()
engine.stop()
pdf.close()