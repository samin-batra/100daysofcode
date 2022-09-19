from gtts import *
import PyPDF2

# creating a pdf file object
pdfFileObj = open('Pride-and-Prejudice.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(5)

pdf = str(pageObj.extractText())

myobj = gTTS(text=pdf, lang='en', slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

print(pdf)


