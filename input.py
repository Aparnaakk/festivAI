from tkinter import *
import pandas as pd
def input():
    master = Tk()
    Label(master, text="Enter path of image").grid(row=0)
    Label(master, text="Enter festival").grid(row=1)
    
    e1 = Entry(master)
    e2 = Entry(master)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    
    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    #Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    
    mainloop( )
    image=e1.get()
    video=e2.get()
    return image,video
