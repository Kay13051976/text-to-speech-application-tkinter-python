from tkinter import *
from gtts import gTTs


def convertToMP3():
    word=text_entry.get()
    language='th'
    output=gTTs(text=word,lang=language,slow=False)
    output.save("sound.mp3")

root=Tk()
root.title("Text To Speech(Thai to English)")
canvas=Canvas(root,width=400,height=300)
canvas.pack()

app_label=Label(text="Text To Speech",font=('Arial',20,'bold'))
canvas.create_window(200,100,window=app_label)

text_entry=Entry(root)
canvas.create_window(200,180,window=text_entry)

button=Button(text="Speech",command=convertToMP3)
canvas.create_window(200,230,window=button)


root.mainloop()