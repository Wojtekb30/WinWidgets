import tkinter
from tkinter import *
from datetime import datetime
from datetime import date
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
    now = datetime.now()
    rok = now.year
    
    miesiac = now.month
    matmiesiac=0
    dzien = now.day

    w=10
    h=10
    #kwadraty
    canvas.create_rectangle(w, h, w+100, h+100, width=5, fill='lightgrey')
    canvas.create_rectangle(w+100, h, w+200, h+100, width=5, fill='lightgrey')
    canvas.create_rectangle(w+200, h, w+300, h+100, width=5, fill='lightgrey')
    canvas.create_rectangle(w+300, h, w+400, h+100, width=5, fill='lightgrey')
    canvas.create_rectangle(w+400, h, w+500, h+100, width=5, fill='lightgrey')
    canvas.create_rectangle(w+500, h, w+600, h+100, width=5, fill='lightgrey')
    canvas.create_rectangle(w+600, h, w+700, h+100, width=5, fill='lightgrey')
    
    canvas.create_rectangle(w, h+100, w+100, h+200, width=5, fill='lightgrey')
    canvas.create_rectangle(w+100, h+100, w+200, h+200, width=5, fill='lightgrey')
    canvas.create_rectangle(w+200, h+100, w+300, h+200, width=5, fill='lightgrey')
    canvas.create_rectangle(w+300, h+100, w+400, h+200, width=5, fill='lightgrey')
    canvas.create_rectangle(w+400, h+100, w+500, h+200, width=5, fill='lightgrey')
    canvas.create_rectangle(w+500, h+100, w+600, h+200, width=5, fill='lightgrey')
    canvas.create_rectangle(w+600, h+100, w+700, h+200, width=5, fill='lightgrey')
    
    canvas.create_rectangle(w, h+200, w+100, h+300, width=5, fill='lightgrey')
    canvas.create_rectangle(w+100, h+200, w+200, h+300, width=5, fill='lightgrey')
    canvas.create_rectangle(w+200, h+200, w+300, h+300, width=5, fill='lightgrey')
    canvas.create_rectangle(w+300, h+200, w+400, h+300, width=5, fill='lightgrey')
    canvas.create_rectangle(w+400, h+200, w+500, h+300, width=5, fill='lightgrey')
    canvas.create_rectangle(w+500, h+200, w+600, h+300, width=5, fill='lightgrey')
    canvas.create_rectangle(w+600, h+200, w+700, h+300, width=5, fill='lightgrey')
    
    canvas.create_rectangle(w, h+300, w+100, h+400, width=5, fill='lightgrey')
    canvas.create_rectangle(w+100, h+300, w+200, h+400, width=5, fill='lightgrey')
    canvas.create_rectangle(w+200, h+300, w+300, h+400, width=5, fill='lightgrey')
    canvas.create_rectangle(w+300, h+300, w+400, h+400, width=5, fill='lightgrey')
    canvas.create_rectangle(w+400, h+300, w+500, h+400, width=5, fill='lightgrey')
    canvas.create_rectangle(w+500, h+300, w+600, h+400, width=5, fill='lightgrey')
    canvas.create_rectangle(w+600, h+300, w+700, h+400, width=5, fill='lightgrey')
    
    
    if miesiac!=2:
        canvas.create_rectangle(w, h+400, w+100, h+500, width=5, fill='lightgrey')
    if miesiac==2 and rok%4==0 and rok%100!=0:
        canvas.create_rectangle(w, h+400, w+100, h+500, width=5, fill='lightgrey')
    if miesiac==2 and rok%4==0 and rok%400==0:
        canvas.create_rectangle(w, h+400, w+100, h+500, width=5, fill='lightgrey')
    
    
    
    
    
    
    
    
    
    
    if miesiac>7:
        matmiesiac=miesiac+1
    else:
        matmiesiac=miesiac
    if (miesiac!=2):
        canvas.create_rectangle(w+100, h+400, w+200, h+500, width=5, fill='lightgrey')
        if matmiesiac%2==1:
            canvas.create_rectangle(w+200, h+400, w+300, h+500, width=5, fill='lightgrey')
        
        
    #renderfix
    canvas.create_rectangle(w+300, h+400, w+705, h+510, width=5, fill='white')
    
    #dzienkwadrat
    nh = 0
    nw = 0

    if dzien==2:
        nw = 100
    if dzien==3:
        nw = 200
    if dzien==4:
        nw = 300
    if dzien==5:
        nw = 400
    if dzien==6:
        nw = 500
    if dzien==7:
        nw = 600
        
    if dzien==8:
        nw = 0
        nh=100
    if dzien==9:
        nw = 100
        nh=100
    if dzien==10:
        nw = 200
        nh=100
    if dzien==11:
        nw = 300
        nh=100
    if dzien==12:
        nw = 400
        nh=100
    if dzien==13:
        nw = 500
        nh=100
    if dzien==14:
        nw = 600
        nh=100
        
        
        
    if dzien==15:
        nw = 0
        nh=200
    if dzien==16:
        nw = 100
        nh=200
    if dzien==17:
        nw = 200
        nh=200
    if dzien==18:
        nw = 300
        nh=200
    if dzien==19:
        nw = 400
        nh=200
    if dzien==20:
        nw = 500
        nh=200
    if dzien==21:
        nw = 600
        nh=200

    if dzien==22:
        nw = 0
        nh=300
    if dzien==23:
        nw = 100
        nh=300
    if dzien==24:
        nw = 200
        nh=300
    if dzien==25:
        nw = 300
        nh=300
    if dzien==26:
        nw = 400
        nh=300
    if dzien==27:
        nw = 500
        nh=300
    if dzien==28:
        nw = 600
        nh=300

    if dzien==29:
        nw = 0
        nh=400
    if dzien==30:
        nw = 100
        nh=400
    if dzien==31:
        nw = 200
        nh=400

    canvas.create_rectangle(w+nw, h+nh, w+nw+100, h+nh+100, width=7, outline='red')
    
#cyfrydnimiesiaca
    p=30
    canvas.create_text(w+p, h+p, text="01")
    canvas.create_text(w+100+p, h+p, text="02")
    canvas.create_text(w+200+p, h+p, text="03")
    canvas.create_text(w+300+p, h+p, text="04")
    canvas.create_text(w+400+p, h+p, text="05")
    canvas.create_text(w+500+p, h+p, text="06")
    canvas.create_text(w+600+p, h+p, text="07")
    
    canvas.create_text(w+p, h+100+p, text="08")
    canvas.create_text(w+100+p, h+100+p, text="09")
    canvas.create_text(w+200+p, h+100+p, text="10")
    canvas.create_text(w+300+p, h+100+p, text="11")
    canvas.create_text(w+400+p, h+100+p, text="12")
    canvas.create_text(w+500+p, h+100+p, text="13")
    canvas.create_text(w+600+p, h+100+p, text="14")
    
    canvas.create_text(w+p, h+200+p, text="15")
    canvas.create_text(w+100+p, h+200+p, text="16")
    canvas.create_text(w+200+p, h+200+p, text="17")
    canvas.create_text(w+300+p, h+200+p, text="18")
    canvas.create_text(w+400+p, h+200+p, text="19")
    canvas.create_text(w+500+p, h+200+p, text="20")
    canvas.create_text(w+600+p, h+200+p, text="21")
    
    canvas.create_text(w+p, h+300+p, text="22")
    canvas.create_text(w+100+p, h+300+p, text="23")
    canvas.create_text(w+200+p, h+300+p, text="24")
    canvas.create_text(w+300+p, h+300+p, text="25")
    canvas.create_text(w+400+p, h+300+p, text="26")
    canvas.create_text(w+500+p, h+300+p, text="27")
    canvas.create_text(w+600+p, h+300+p, text="28")
    
    if miesiac!=2:
        canvas.create_text(w+p, h+400+p, text="29")
    if miesiac==2 and rok%4==0 and rok%100!=0:
        canvas.create_text(w+p, h+400+p, text="29")
    if miesiac==2 and rok%4==0 and rok%400==0:
        canvas.create_text(w+p, h+400+p, text="29")
    
    if miesiac>7:
        matmiesiac=miesiac+1
    else:
        matmiesiac=miesiac
    if (miesiac!=2):
        canvas.create_text(w+100+p, h+400+p, text="30")
        if matmiesiac%2==1:
            canvas.create_text(w+200+p, h+400+p, text="31")
        

#final   
    
    tyg = (datetime.today().weekday())
    tyg = tyg + 1
    dtyg = "ERROR"
    texmiesiac="ERROR"
    if tyg==1:
        dtyg = "Poniedziałek, "
    if tyg==2:
        dtyg = "Wtorek, "
    if tyg==3:
        dtyg = "Środa, "
    if tyg==4:
        dtyg = "Czwartek, "
    if tyg==5:
        dtyg = "Piątek, "
    if tyg==6:
        dtyg = "Sobota, "
    if tyg==7:
        dtyg = "Niedziela, "
    if miesiac <10:
        texmiesiac = "0"+str(miesiac)
    if miesiac >=10:
        texmiesiac = str(miesiac)
    canvas.create_text(500, 470, text=dtyg+str(texmiesiac)+"."+str(rok), font=("Helvetica", 10))
    
    canvas.after(60000, nowyczas)
    
now = datetime.now()


canvas = Canvas(win)
canvas.pack()


btn=Button(win, text="X", bg='red', command=nuke)

btn.place(x=671, y=448)
win.geometry("720x525")

canvas.after(1000, nowyczas)
win.mainloop()
    



