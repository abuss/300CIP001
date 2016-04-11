from tkinter import *

def quit(event):
    print("Done")
    import sys; sys.exit()


def derecha(e):
    print(jumper)
    x,y = c.coords(jumper['obj'])
    print(nivel[jumper['y']])
    if x < nivel[jumper['y']]['x'][0][1]:
        c.move(jumper['obj'],5,0)
        # c.itemconfigure(chef,image=imgr)

def izquierda(e):
    x,y = c.coords(jumper['obj'])
    if x > nivel[jumper['y']]['x'][0][0]:
    # if x>15:
        c.move(jumper['obj'],-5,0)
        # c.itemconfigure(chef,image=imgr)

def arriba(e):
    x,y = c.coords(jumper['obj'])
    escalera = escaleras[jumper['y']-1]['x'][0]
    if escalera[0] < x < escalera[1]:
        c.coords(jumper['obj'],x,y-5)
    if (y-6)< (jumper['y'])*dY:
        print('cambio de piso')
        jumper['y']-=1

def abajo(e):
    x,y = c.coords(jumper['obj'])
    escalera = escaleras[jumper['y']]['x'][0]
    if escalera[0] < x < escalera[1]:
        c.coords(jumper['obj'],x,y+5)
    if (y+dY+1)> (jumper['y'])*dY:
        print('cambio de piso')
        jumper['y']+=1

nivel = [{'y':0,'x':[(10,400)],'obj':[]},
         {'y':1,'x':[(10,400)],'obj':[]},
         {'y':2,'x':[(10,400)],'obj':[]},
         {'y':3,'x':[(10,400)],'obj':[]},
         {'y':4,'x':[(10,400)],'obj':[]},
         {'y':5,'x':[(10,400)],'obj':[]} ]

escaleras = [{'y':0,'x':[(350,380)],'obj':[]},
             {'y':1,'x':[(30,60)],'obj':[]},
             {'y':2,'x':[(350,380)],'obj':[]},
             {'y':3,'x':[(50,80)],'obj':[]},
             {'y':4,'x':[(350,380)],'obj':[]},]
master = Tk()
c = Canvas(master,width=440,height=340)
c.pack()

i = 1
dY = 50
for d in nivel:
    pisos = d['x']
    for p in pisos:
        print(p)
        d['obj'].append(c.create_rectangle(p[0],i*dY,p[1],i*dY+10,fill="red"))
    i += 1

i = 1
for d in escaleras:
    posx = d['x']
    for p in posx:
        print(p)
        d['obj'].append(c.create_rectangle(p[0],i*dY,p[1],i*dY+dY,fill="blue"))
    i += 1

imgr = PhotoImage(file="chef.gif")
imgl = PhotoImage(file="chefl.gif")
jumper = {'y':len(nivel)-1,'x':50}
jumper['obj'] = c.create_image(jumper['x'],(jumper['y']+1)*dY,image=imgr)

c.bind('<Double-1>', quit)

master.bind('a', izquierda)
master.bind('s', derecha)
master.bind('<Right>', derecha)
master.bind('<Left>', izquierda)
master.bind('<Up>', arriba)
master.bind('<Down>', abajo)

mainloop()
