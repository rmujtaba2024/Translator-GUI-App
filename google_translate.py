from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English",dest="Hindi"):
    text1=text
    sec1=src
    des1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=sec1,dest=des1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text = masg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget)


root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="light blue")

lab_txt = Label(root, text="Translator", font=("Times New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=70,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Times New Roman",20,"bold"))
lab_txt.place(x=100,y=130,height=30,width=300)


Sor_txt = Text(frame,font=("Times New Roman",20),wrap=WORD)
Sor_txt.place(x=10,y=170,height=150,width=480)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=90,y=330,height=30,width=100)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=200,y=330,height=30,width=100)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=310,y=330,height=30,width=100)
comb_dest.set("english")

dest_txt = Text(frame,font=("Times New Roman",20),wrap=WORD)
dest_txt.place(x=10,y=370,height=150,width=480)


root.mainloop()
