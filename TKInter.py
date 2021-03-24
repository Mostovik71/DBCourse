from tkinter import *
from tkinter.scrolledtext import ScrolledText

from DBConnection import cur,con
from PIL import Image, ImageTk

def slipknotmembers():#Функция которая выдает всех участников Slipknot
 cur.execute("SELECT * from slipknotmembers")
 rows = cur.fetchall()
 for i in rows:
  text.insert(END, str(i)+'\n')
  #print(i)


 #text.configure(state='normal')  # enable insert
 text.yview(END)  # autoscroll
 #text.configure(state='enabled')
 con.commit()
def slipknotalbum1():# Функция которая выдает все треки альбома Vol .3: The Subliminal Verses
 cur.execute("SELECT * from thesubliminalverses")
 rows = cur.fetchall()
 for i in rows:
  text1.insert(END, str(i) + '\n')
  #print(i)

 text1.yview(END)  # autoscroll

 con.commit()
def slipknotalbum2():  # Функция которая выдает все треки альбома We Are Not Your Kind
  cur.execute("SELECT * from wearenotyourkind")
  rows = cur.fetchall()
  for i in rows:
      text1.insert(END, str(i) + '\n')
      #print(i)

  text1.yview(END)  # autoscroll

  con.commit()
def slipknotinfo():
 cur.execute("SELECT group_info from slipknotinfo")
 rows = cur.fetchall()

 con.commit()

 text.insert(END, rows)
 text.yview(END)  # autoscroll



def bfmvmembers():#Функция которая выдает всех участников Bullet for My Valentine
 cur.execute("SELECT * from bfmvmembers")
 rows = cur.fetchall()
 for i in rows:
     textbfmv.insert(END, str(i) + '\n')
     #print(i)

  # enable insert
 textbfmv.yview(END)  # autoscroll


 con.commit()
def bfmvalbum1():# Функция которая выдает все треки альбома The Poison
 cur.execute("SELECT * from thepoison")
 rows = cur.fetchall()
 for i in rows:
     textbfmv1.insert(END, str(i) + '\n')
     #print(i)


 textbfmv1.yview(END)  # autoscroll


 con.commit()
def bfmvalbum2():  # Функция которая выдает все треки альбома Scream Aim Fire
  cur.execute("SELECT * from screamaimfire")
  rows = cur.fetchall()
  for i in rows:
      textbfmv1.insert(END, str(i) + '\n')
      #print(i)


  textbfmv1.yview(END)  # autoscroll


  con.commit()
def bfmvinfo():
 cur.execute("SELECT group_info from bfmvinfo")
 rows = cur.fetchall()
 textbfmv.insert(END, rows)
 textbfmv.yview(END)  # autoscroll
 con.commit()







class Main(Tk):
 def __init__(self):
  super().__init__()
  self.title("Группы")  # Заголовок окна
  self.geometry('500x500')
  self.img = ImageTk.PhotoImage(Image.open("C:/Users/Vlad/Desktop/QVsnSq.jpg"))
  self.panel = Label(self, image=self.img)
  self.panel.pack(side="bottom", fill="both", expand="no")
  lbl = Label(self, text="Выберите интересующую вас группу",bg="red",fg="white", font=("Arial Black", 12))
  lbl.place(x=80,y=300,width=350,height=30)
  btn1 = Button(self, text="Slipknot",bg="red", fg="black",command=slipknotmain)
  btn2 = Button(self, text="Bullet for My Valentine",bg="red", fg="black",command=bfmvmain)
  btn1.place(x=100,y=100)
  btn2.place(x=300,y=100)


 def started_create(self):
  self.top_level = slipknotmain()
 def started_create1(self):
  self.top_level = bfmvmain()


class slipknotmain(Toplevel):
 def __init__(self):
  super().__init__()
  self.geometry('500x500')
  self.img = ImageTk.PhotoImage(Image.open("C:/Users/Vlad/Desktop/slipknot.jpg"))
  self.panel = Label(self, image=self.img)
  self.panel.pack(side="bottom", fill="both", expand="no")

  global text
  text = ScrolledText(self, width=50, height=5)
  text.place(x=40, y=400)

  but1 = Button(self, text="Получить краткую информацию о группе",bg="black", fg="red",command=slipknotinfo)
  but2 = Button(self, text="Получить список участников группы",bg="black", fg="red",command=slipknotmembers)
  but3 = Button(self, text="Получить список альбомов",bg="black", fg="red",command = slipknotalbums)
  but4 = Button(self, text="Очистить", bg="black", fg="red", command=lambda: text.delete(1.0,END))
  but1.place(x=0, y=0)
  but2.place(x=150, y=50)
  but3.place(x=335, y=0)
  but4.place(x=0, y=200)





  self.title("Страница группы Slipknot")
 def started_create(self):
  self.top_level = slipknotalbums()

def clear():
 text.update()




class slipknotalbums(Toplevel):
 def __init__(self):

   super().__init__()
   self.geometry('500x500')
   self.img = ImageTk.PhotoImage(Image.open("C:/Users/Vlad/Desktop/slipknotalbums.jpg"))
   self.panel = Label(self, image=self.img)
   self.panel.pack(side="bottom", fill="both", expand="no")
   but1 = Button(self, text="Vol. 3: The Subliminal Verses", bg="black", fg="red", command=slipknotalbum1)
   but2 = Button(self, text="We Are Not Your Kind", bg="black", fg="red", command=slipknotalbum2)
   but4 = Button(self, text="Очистить", bg="black", fg="red", command=lambda: text1.delete(1.0, END))
   but4.place(x=0, y=200)
   but1.place(x=300, y=50)
   but2.place(x=80, y=50)
   self.geometry('500x500')  # Размеры окна
   self.title("Наиболее популярные альбомы группы Slipknot")
   global text1
   text1 = ScrolledText(self, width=50, height=5)
   text1.place(x=40, y=400)


class bfmvmain(Toplevel):
 def __init__(self):
  super().__init__()
  self.geometry('500x500')
  self.img = ImageTk.PhotoImage(Image.open("C:/Users/Vlad/Desktop/Bullet-for-My-Valentine.jpg"))
  self.panel = Label(self, image=self.img)
  self.panel.pack(side="bottom", fill="both", expand="no")

  but1 = Button(self, text="Получить краткую информацию о группе",bg="black", fg="red",command=bfmvinfo)
  but2 = Button(self, text="Получить список участников группы",bg="black", fg="red",command=bfmvmembers)
  but3 = Button(self, text="Получить список альбомов",bg="black", fg="red",command = bfmvalbums)
  but4 = Button(self, text="Очистить", bg="black", fg="red", command=lambda: textbfmv.delete(1.0, END))
  but4.place(x=0, y=200)
  but1.place(x=0, y=0)
  but2.place(x=150, y=50)
  but3.place(x=335, y=0)

  global textbfmv
  textbfmv = ScrolledText(self, width=50, height=5)
  textbfmv.place(x=40, y=400)


  self.title("Страница группы Bullet for My Valentine")
 def started_create(self):
  self.top_level = bfmvalbums()


class bfmvalbums(Toplevel):
 def __init__(self):

   super().__init__()
   self.geometry('500x500')
   self.img = ImageTk.PhotoImage(Image.open("C:/Users/Vlad/Desktop/bfmvalbums.jpg"))
   self.panel = Label(self, image=self.img)
   self.panel.pack(side="bottom", fill="both", expand="no")
   but1 = Button(self, text="The Poison", bg="black", fg="red", command=bfmvalbum1)
   but2 = Button(self, text="Scream Aim Fire", bg="black", fg="red", command=bfmvalbum2)
   but4 = Button(self, text="Очистить", bg="black", fg="red", command=lambda: textbfmv1.delete(1.0, END))
   but4.place(x=0, y=200)
   but1.place(x=80, y=50)
   but2.place(x=330, y=50)
   self.geometry('500x500')  # Размеры окна
   self.title("Наиболее популярные альбомы группы Bullet for My Valentine")
   global textbfmv1
   textbfmv1 = ScrolledText(self, width=50, height=5)
   textbfmv1.place(x=40, y=400)



if __name__ == "__main__":
    main = Main()
    main.mainloop()