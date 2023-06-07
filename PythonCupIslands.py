import tkinter as tk
import random 

size = 50

numberofx = random.randrange(4,7)
numberofy = random.randint(3,10)
squares = []
choice = []
in_choice = []
win = tk.Tk()
text = []
bridges = []

color = "gray"



canvas = tk.Canvas(win,width = (numberofx+2)*size+10,height = numberofy*size+100,bg=color)
canvas.pack()

bridge_cost = 10
isle_cost = 50

def grid_creation():
    global wallet
    wallet = 0
    text.append(canvas.create_text(numberofx*size+size,10+size*2,font=("Arial",20),text=wallet))
    choice.append(canvas.create_rectangle((numberofx+1)*size,10,(numberofx+2)*size,10+size,fill="white",tag ="island"))
    in_choice.append(canvas.create_oval(canvas.coords(choice[0])[0]+10,10+10,canvas.coords(choice[0])[2]-10,10+size-10,fill="orange"))
    for y in range(numberofy):
        for x in range(numberofx):
            num = random.randrange(1,6)
            if num==2:
                col = "orange"
                tag = "isler"
            else:
                col = "white"
                tag = "normal"
            squares.append(canvas.create_rectangle(10+x*size,10+y*size,10+(x+1)*size,10+(y+1)*size,fill=col,width = 2,outline = color,tag=tag))

def click(e):
    global in_choice,wallet
    overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    coords = canvas.coords(overlap[0])

    if overlap[0] == choice[0]:
        if canvas.itemcget(overlap[0],"tag")=="island":
            canvas.delete(in_choice[0])
            in_choice = [ ]
            in_choice.append(canvas.create_rectangle(canvas.coords(choice[0])[0]+5,25,canvas.coords(choice[0])[2]-5,size+10-15,fill="aquamarine"))
            canvas.itemconfig(choice[0],tag="bridge")
        elif canvas.itemcget(overlap[0],"tag")=="bridge":
            canvas.delete(in_choice[0])
            in_choice = [ ]
            in_choice.append(canvas.create_oval(canvas.coords(choice[0])[0]+10,10+10,canvas.coords(choice[0])[2]-10,10+size-10,fill="orange"))
            canvas.itemconfig(choice[0],tag="island")

    elif overlap[0] in squares:
        bridges = [ ]
        bridges = list(canvas.find_overlapping(coords[0]+3,coords[1]+3,coords[2]-3,coords[3]-3))
        bridges.remove(bridges[0])
        if canvas.itemcget(overlap[0],"tag") != "isler current":
            if canvas.itemcget(choice[0],"tag") == "bridge":
                if canvas.itemcget(overlap[0],"tag") == "normal current" and len(bridges)==0 or canvas.itemcget(bridges[0],"tag")=="ver_bridge current":
                    if len(bridges) ==0:
                        bridges.append(canvas.create_rectangle(coords[0]+5,coords[1]+15,coords[2]-5,coords[3]-15,fill="aquamarine"))
                        wallet+=10
                        canvas.itemconfig(text[0],text=wallet)
                        canvas.itemconfig(overlap[0],tag="hor_bridge")
                      
                    else:
                        canvas.delete(bridges[0])
                        bridges.remove(bridges[0])
                        bridges.append(canvas.create_rectangle(coords[0]+5,coords[1]+15,coords[2]-5,coords[3]-15,fill="aquamarine",tag="hor_bridge"))
                        canvas.itemconfig(bridges[0],tag="hor_bridge")
                        canvas.itemconfig(overlap[0],tag="hor_bridge")
                    
                
                elif canvas.itemcget(bridges[0],"tag") == "hor_bridge current" or canvas.itemcget(bridges[0],"tag")=="current":
                    canvas.delete(bridges[0])
                    bridges.remove(bridges[0])
                    bridges.append(canvas.create_rectangle(coords[0]+15,coords[1]+5,coords[2]-15,coords[3]-5,fill="aquamarine",tag="ver_bridge"))
                    canvas.itemconfig(bridges[0],tag="ver_bridge")
                    canvas.itemconfig(overlap[0],tag="ver_bridge")
     
            
            elif canvas.itemcget(choice[0],"tag") == "island":
                if canvas.itemcget(overlap[0],"tag") != "ver_bridge" and canvas.itemcget(overlap[0],"tag")!="hor_bridge" and canvas.itemcget(overlap[0],"tag")!="hor_bridge current" and canvas.itemcget(overlap[0],"tag")!="ver_bridge current":
                    if canvas.itemcget(overlap[0],"tag")!="isler" and canvas.itemcget(overlap[0],"tag")!="isler current" :
                        wallet+=50
                    canvas.itemconfig(overlap[0],fill="orange")
                    canvas.itemconfig(overlap[0],tag="isler")
                    canvas.itemconfig(text[0],text=wallet)

    return 






canvas.bind("<Button-1>",click)
grid_creation()

win.mainloop()