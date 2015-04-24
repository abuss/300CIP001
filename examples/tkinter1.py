__author__ = 'abuss'

import tkinter
import time

#print(dir(tkinter))

master = tkinter.Tk()

w = tkinter.Canvas(master, width=200, height=100)
w.pack()
w.update()

i=w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

j = w.create_rectangle(50, 25, 150, 75, fill="blue")
w.update()

input()
w.coords(i, 10,10, 150,50) # change coordinates
w.update()

input()
w.itemconfig(i, fill="yellow") # change color
w.update()

for x in range(50):
    w.coords(j,50+x,25,150-x,75)
    w.update()
    time.sleep(0.1)

tkinter.mainloop()
