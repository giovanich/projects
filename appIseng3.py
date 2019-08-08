from tkinter import *
from tkinter import messagebox

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Insert a word to replace")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.a=Label(top,text="Insert a word to be the replacement")
        self.a.pack()
        self.c=Entry(top)
        self.c.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class mainWindow(object):
    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled"
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"

    def process(self):
        self.input = self.t.get(1.0,END)
        self.check = self.t2.get(1.0,END)
        self.lenInput = len(self.input)
        self.lenCheck = len(self.check)
        print(self.lenCheck, self.lenInput)
        if self.lenCheck <= 1:
            if self.lenInput <= 1:
                self.t.insert(END,"Please insert a text")
            else:
                for i in replaceThings:
                    self.inputFin= self.input.replace(""+str(i)+"",'')
                    self.input=self.inputFin
                self.t2.insert(END,self.inputFin)
                print(self.inputFin)

    def reset(self):
        self.t.delete(1.0,END)
        self.t2.delete(1.0,END)

    def __init__(self, master):
        self.master=master
        self.menubar = Menu(master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Add MySQL Library", command = self.popup)
        self.filemenu.add_command(label="Add VB Library",)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=master.quit)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)

        self.topFrame = Frame(master)
        self.topFrame.pack()
        self.bottomFrame = Frame(master)
        self.bottomFrame.pack(side=BOTTOM)
        self.Label0 = Label(self.topFrame, text= "Converter",font="Arial 20",)
        self.Label0.grid(row=1,column=5)
        self.Label1 = Label(self.topFrame, text="MS SQL QUERY", font="Arial 16",)
        self.Label1.grid(row=2,column=1)
        self.Label2 = Label(self.topFrame, text="MySQL QUERY", font="Arial 16",)
        self.Label2.grid(row=2,column=6)

        self.t = Text(self.topFrame, height=20, width=40)
        self.t.grid(row=3,column=1)
        self.t2 = Text(self.topFrame, height=20, width=40)
        self.t2.grid(row=3,column=6)

        self.Button1 = Button(self.topFrame, text="OK",command=self.process).grid(row=4, column=1)
        self.Button1 = Button(self.topFrame, text="RESET",command=self.reset).grid(row=4, column=6)

        master.config(menu=self.menubar)
        master.mainloop()

if __name__ == "__main__":
    root=Tk()
    root.title("Converter")
    replaceThings =['a','c']
    m=mainWindow(root)
    root.mainloop()
