#refactoring of code is proces of modifying the code after it was written and is working
import tkinter as tk
import random as rnd
root=tk.Tk()
root.title('I and B')
width=300
height=450
p_w=50
p_h=50
c_w=rnd.randrange(4,7)
c_h=rnd.randrange(3,10)
canvas = tk.Canvas(root,width=width+100,height=height,bg='grey')
canvas.pack()
water=[]
islands=[]
switcher = []
text = []
wallet = 0
bckg=tk.PhotoImage(file='Images/ostrov3.png')
bckg2=tk.PhotoImage(file='Images/ostrov0.png')
img1=tk.PhotoImage(file='Images/ostrov1.png')
img2=tk.PhotoImage(file='Images/ostrov2.png')
img3 = tk.PhotoImage(file="Images/ostrov_kruh0.png")
img4 = tk.PhotoImage(file="Images/ostrov_kruh1.png")

def setup():
    global water, islands
    for y in range(c_h):
        for x in range(c_w):
            chance = rnd.random()
            if chance >= 0.2:
                water.append(canvas.create_image(p_w*x,p_h*y, image = bckg, anchor = tk.NW))
            else:
                islands.append(canvas.create_image(p_w*x,p_h*y, image = bckg2, anchor = tk.NW))
    switcher.append(canvas.create_image(c_w*p_w+50,0,anchor="nw", image=img3,tag="switcheroo"))
    text.append(canvas.create_text(c_w*p_w+50,80,text=wallet))

def switch(e):
    global water,wallet
    list1=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if canvas.itemcget(switcher[0],"image")=="pyimage5":
        if len(list1)!=0 and list1[0] in water:
            n_x=(e.x//p_w)*p_w
            n_y=(e.y//p_h)*p_h
            temp=list1[0]
            canvas.delete(temp)
            water.remove(temp)
            canvas.create_image(n_x,n_y,image = img1, anchor = tk.NW, tag='bridge')
            wallet+=10
            canvas.itemconfig(text[0],text=wallet)
    if canvas.itemcget(switcher[0],"image")=="pyimage6":
        if len(list1)!=0 and list1[0] in water:
            n_x=(e.x//p_w)*p_w
            n_y=(e.y//p_h)*p_h
            temp=list1[0]
            canvas.delete(temp)
            water.remove(temp)
            canvas.create_image(n_x,n_y,image = bckg2, anchor = tk.NW, tag='island')
            wallet+=50
            canvas.itemconfig(text[0],text=wallet)


def spinner(e):
    list1=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if canvas.itemcget(list1[0],"image") =="pyimage3":
        canvas.itemconfig(list1[0],image=img2)
    else:
        canvas.itemconfig(list1[0],image=img1)

def spinner_switch(e):
    overl = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if canvas.itemcget(overl[0],"image")=="pyimage5":
        canvas.itemconfig(overl[0],image=img4)
    else:
        canvas.itemconfig(overl[0],image=img3)


canvas.bind('<Button-1>', switch)
canvas.tag_bind('bridge','<Button-1>',spinner)
canvas.tag_bind('switcheroo','<Button-1>',spinner_switch)

setup()
root.mainloop()
