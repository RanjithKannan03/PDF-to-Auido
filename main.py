from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from gtts import gTTS
import PyPDF2
from pydub import AudioSegment
from pydub.playback import play
import io


fp=io.BytesIO()





def openFile():
    file_directory.delete(0,END)
    try:
        directory = filedialog.askopenfile(initialdir="/", title="Select the PDF", filetypes=[("PDF directory", "*.pdf")], mode="r")
    except AttributeError:
        messagebox.showwarning(title="File Error",message="Unable to open directory")
    else:
        file_directory.insert(0, directory.name)


def read():
    directory=file_directory.get()
    reader=PyPDF2.PdfReader(directory)
    text=""
    for page in reader.pages:
        text+="\n"+page.extract_text()
    print(text)
    tts=gTTS(text,lang="en-us",tld="us")
    tts.save("audio.mp3")






PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"



window=Tk()
window.title="PDF to AudioBook"
window.config(padx=100,pady=100,bg=YELLOW)

canvas=Canvas(width=700,height=400,bg=YELLOW,highlightthickness=0)
canvas.create_text(350,200,text="Convert PDF to Audio",font=(FONT_NAME,40,"bold"),fill=GREEN)

canvas.grid(row=0,column=1)

open_button=Button(text="Open",command=openFile,highlightthickness=0)
open_button.grid(row=1,column=0)


file_directory=Entry(width=40)
file_directory.grid(row=1,column=1)


read_button=Button(text="Read",command=read,highlightthickness=0)
read_button.grid(row=1,column=2)






window.mainloop()