from tkinter import *
from time import *

d = Tk()
hua = Canvas(d,width=400,height=400)
# oval = hua.create_line(0,0,100,100)
# oval1 = hua.create_line(0,100,100,100)
hua.pack()
san  = hua.create_polygon(10,10,50,10,10,50)
def aaa(e):
    if e.char=="a":
      hua.move(1,-5,0)
    if e.char == "s":
      hua.move(1, 0, 5)
    if e.char == "d":
      hua.move(1, 5, 0)
    if e.char == "w":
      hua.move(1, 0, -5)
hua.bind_all("<KeyPress-a>",aaa)
hua.bind_all("<KeyPress-s>",aaa)
hua.bind_all("<KeyPress-d>",aaa)
hua.bind_all("<KeyPress-w>",aaa)
# for i in range(1,100):
#   hua.move(1,15,0)
#   sleep(1)
#   hua.update()
# tex = hua.create_text(100,50,text="132")
# coord = 10, 50, 240, 240
# arc = hua.create_arc(coord,fill="red")
# oavl = hua.create_oval(0,0,100,100,fill="red")

d.mainloop()