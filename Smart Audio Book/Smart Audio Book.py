import pyttsx3    #pyttsx3 -> python text to speech version 3
import PyPDF2
book = open('CN.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)                #print the number of pages in the pdf
friend = pyttsx3.init()
for num in range(33, pages):
    page = pdfReader.getPage(num) #read the page no (num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()