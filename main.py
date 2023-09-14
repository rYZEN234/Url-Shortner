import pyshorteners
from tkinter import *

win=Tk()
# to resize window size we use geometry function
win.geometry("400x270")  #height and width
win.configure(bg="pink") #this is this syntax for the background color.
#label for link which is given by the user.
#function for button.
def short():
    url=entry.get()
    s=pyshorteners.Shortener().tinyurl.short(url)
    
    #for copy
    entry1.insert(END,s)
Label(win,text="Enter your Url link",font="impact 17 bold",bg="black",fg="white").pack(fill="x")
#fg =foegroewn color of the font.
#entry box.
entry=Entry(win,font="10",bd=3,width=40)
entry.pack(pady=30)
#bd=border,pad using for gap
#button
Button(win,text="click Me",font="impact 12 bold",bg="blue",fg="white",width="15",command=short).pack()
#entry for short link
entry1=Entry(win,font="impack 16 bold",bg="pink",width=24,bd=0)
entry1.pack(pady=30)

mainloop()