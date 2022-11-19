import tkinter
from tkinter import *
from datetime import datetime

global now
global current_time

    
class Win(tkinter.Tk):

    def __init__(self,master=None):
        tkinter.Tk.__init__(self,master)
        self.overrideredirect(True)

        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',self.clickwin)
        self.bind('<B1-Motion>',self.dragwin)

    



    def dragwin(self,event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(self,event):
        self._offsetx = event.x
        self._offsety = event.y
    def refresh(self):
        self.destroy()
        self.__init__()



win = Win()
def nuke():
    win.destroy()
    
    
def nowyczas():

    canvas.create_oval(3, 3, 297, 297, fill='green', outline='green')   
    now = datetime.now()
    tsekundy = now.strftime("%S")
    tminuty = now.strftime("%M")
    tgodziny = now.strftime("%H")
    sekundy = int(tsekundy)
    minuty = int(tminuty)
    godziny = int(tgodziny)
    if godziny>=12:
        godziny = godziny - 12
    if godziny <0:
        godziny = godziny * -1
    if minuty == 0:
        minuty = 0.3
    if godziny ==0:
        godziny=0.2
    if sekundy == 0:
        sekundy = 0.3

    canvas.create_arc(3+45, 3+45, 297-45, 297-45, start=90, extent=-6*sekundy,  outline='cyan', width=20, style=tkinter.ARC)
    #canvas.create_arc(3, 3, 297, 297, start=90, extent=-6*sekundy+1,  outline='green', width=20, style=tkinter.ARC)
    canvas.create_arc(3+30+45, 3+30+45, 297-30-45, 297-30-45, start=90, extent=-6*minuty,  outline='red', width=20, style=tkinter.ARC)
    canvas.create_arc(3+60+45, 3+60+45, 297-45-60, 297-45-60, start=90, extent=-30*godziny,  outline='black', width=20, style=tkinter.ARC)
    canvas.create_text(150, 17, text="12", fill='cyan')
    canvas.create_text(150, 300-19, text="6", fill='cyan')
    canvas.create_text(19, 150, text="9", fill='cyan')
    canvas.create_text(300-19, 150, text="3", fill='cyan')
    
    canvas.after(1000, nowyczas)
    
now = datetime.now()


canvas = Canvas(win)
canvas.pack()

canvas.create_oval(3, 3, 297, 297, fill='green', outline='green')
btn=Button(win, text="X", bg='red', command=nuke)

btn.place(x=260, y=0)
win.geometry("300x300")

canvas.after(1000, nowyczas)
win.mainloop()
    



