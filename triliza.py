#a simple triliza

import Tkinter
import tkMessageBox

parentWindow = Tkinter.Tk()
parentWindow.title("TRILIZA")

def drawTamplo():
    koumpi = Tkinter.Button(parentWindow, text ="1", width=10, height=5)
    koumpi.grid(row=0,column=0)
    koumpi.bind('<Button-1>',clickHandler)
    koumpi = Tkinter.Button(parentWindow, text ="2", width=10, height=5)
    koumpi.grid(row=0,column=1)
    koumpi.bind('<Button-1>',clickHandler)
    koumpi = Tkinter.Button(parentWindow, text ="3", width=10, height=5)
    koumpi.grid(row=0,column=2)
    koumpi.bind('<Button-1>',clickHandler)
    koumpi = Tkinter.Button(parentWindow, text ="4", width=10, height=5)
    koumpi.grid(row=1,column=0)
    koumpi.bind('<Button-1>',clickHandler)
    koumpi = Tkinter.Button(parentWindow, text ="5", width=10, height=5)
    koumpi.grid(row=1,column=1)
    koumpi.bind('<Button-1>',clickHandler)
    koumpi = Tkinter.Button(parentWindow, text ="6", width=10, height=5)
    koumpi.grid(row=1,column=2)
    koumpi.bind('<Button-1>',clickHandler)
    koumpi = Tkinter.Button(parentWindow, text ="7", width=10, height=5)
    koumpi.grid(row=2,column=0)
    koumpi.bind('<Button-1>',clickHandler)
    koumpi = Tkinter.Button(parentWindow, text ="8", width=10, height=5)
    koumpi.grid(row=2,column=1)
    koumpi.bind('<Button-1>',clickHandler)
    koumpi = Tkinter.Button(parentWindow, text ="9", width=10, height=5)
    koumpi.grid(row=2,column=2)
    koumpi.bind('<Button-1>',clickHandler)

def clickHandler(event):
    global table
    global player
    button = event.widget
    text=button.cget('text')
    l=['1','2','3','4','5','6','7','8','9']
    if ((text in l) and player==1):
        refreshTable(text,player)
        button.config(text="X")
        if (nikhse()):
            tkMessageBox.showinfo("You won!!!")
        player=2
    elif ((text in l) and player==2):
        refreshTable(text,player)
        button.config(text="O")
        if (nikhse()):
            tkMessageBox.showinfo("You won!!!")
        player=1

def refreshTable(text,player):
    #gemizo to pinaka table me assoys gia ton paikth 1 kai dyaria gia ton 2
    if player==1:
        if text=='1':
            table[0][0]=1
        elif text=='2':
            table[0][1]=1
        elif text=='3':
            table[0][2]=1
        elif text=='4':
            table[1][0]=1
        elif text=='5':
            table[1][1]=1
        elif text=='6':
            table[1][2]=1
        elif text=='7':
            table[2][0]=1
        elif text=='8':
            table[2][1]=1    
        elif text=='9':
            table[2][2]=1
    else:
        if text=='1':
            table[0][0]=2
        elif text=='2':
            table[0][1]=2
        elif text=='3':
            table[0][2]=2
        elif text=='4':
            table[1][0]=2
        elif text=='5':
            table[1][1]=2
        elif text=='6':
            table[1][2]=2
        elif text=='7':
            table[2][0]=2
        elif text=='8':
            table[2][1]=2    
        elif text=='9':
            table[2][2]=2

def nikhse():
    if ( (table[0][0]==table[0][1] and table[0][1]==table[0][2]) ) :
        return True
    elif ( (table[1][0]==table[1][1] and table[1][1]==table[1][2]) ):
        return True
    elif ( (table[2][0]==table[2][1] and table[2][1]==table[2][2]) ):
        return True
    elif ( (table[0][0]==table[1][0] and table[1][0]==table[2][0]) ) :
        return True
    elif ( (table[0][1]==table[1][1] and table[1][1]==table[2][1]) ):
        return True
    elif ( (table[0][2]==table[1][2] and table[1][2]==table[2][2]) ):
        return True
    elif ( (table[0][0]==table[1][1] and table[1][1]==table[2][2]) ):
        return True
    elif ( (table[0][2]==table[1][1] and table[1][1]==table[2][0]) ):
        return True
    
        
table=[[10,11,12],[13,14,15],[16,17,18]] #model thn pista...useful at background logic
player=1 #ginetai 1 otan paizei o 1os paikths kai 2 otan...

drawTamplo()
parentWindow.mainloop()
