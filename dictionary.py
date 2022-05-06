from os import linesep
from tkinter import *
import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def dictionary():
    if word.get() in data  :
        t1.delete('1.0', END)
        for result in data[word.get()]: 
            t1.insert(END, result, '%s', ( linesep),'%s', (linesep ))
        
    
    elif word.get().lower() in data:
        t1.delete('1.0', END)
        for result in data[word.get().lower()]:  
            t1.insert(END,result, '%s', ( linesep),'%s', (linesep ))
    
    elif word.get().title() in data:
        t1.delete('1.0', END)
        for result in data[word.get().title()]:  
            t1.insert(END, result, '%s', ( linesep),'%s', (linesep ))

    elif word.get().upper() in data:
        t1.delete('1.0', END)
        for result in data[word.get().upper()]:  
            t1.insert(END, result, '%s', ( linesep),'%s', (linesep ))
    
    elif len(get_close_matches(word.get(), data.keys())) > 0:
        t1.delete('1.0', END)
        t1.insert(END,"Did you mean \"%s\"" %get_close_matches(word.get(), data.keys()) [0])

    else:
        t1.delete('1.0', END)
        t1.insert(END, "Try another word !")

window = Tk(className='Python Examples - Window Color')
window.configure(bg='#E0EEE0')



l1 = Label(window, text='English Dictionary', font='Helvetica 28 bold italic', pady=20, padx=100,bg='#36648B', fg='#FFFFFF')
l1.grid(row=0, column=0)
l2 = Label(window, text='Type the word in following Search bar: ', font='Helvetica 12 bold', fg='#2F4F4F' )
l2.grid(row=1, column=0)

t1 = Text(window, height=20, width=50, font='Helvetica 20 bold')
t1.grid(row=2, column=0, rowspan=2, pady=20, padx=100)

word = StringVar()
e1 = Entry(window, textvariable=word, font='Helvetica 40 bold')
e1.grid(row=2, column=3, pady=20, padx=100)

b1 = Button(window, text='Translate', command=dictionary, font='Helvetica 20 bold', bg='#76EEC6', fg='#2F4F4F', width=30, height=2)
b1.grid(row=3, column=3, columnspan=2)

window.mainloop()


