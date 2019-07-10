from tkinter import *
# import tkinter
# import tkMessageBox
def process():
    input=Entry.get(Entry1)
    check = Entry.get(Entry2)
    replaceThings =['a','c']
    if check == "":
        if input =="":
            Entry.insert(Entry2,0,"Please insert a text")
        else:
            for i in replaceThings:
                inputFin= input.replace(""+str(i)+"",'')
                input=inputFin
            Entry.insert(Entry2,0,inputFin)
            print(inputFin)
def reset():
    Entry1.delete(0,'end')
    Entry2.delete(0,'end')


top = Tk()
top.geometry("400x500")
Label0 = Label(top, text= "Converter",).grid(row=0,column=1)
Label1 = Label(top, text="MS SQL QUERY").grid(row=1,column=0)
Entry1 = Entry(top , bd=2)
Entry1.grid(row=1, column=1)
Label2 = Label(top, text="MySQL QUERY").grid(row=2,column=0)
Entry2 = Entry(top , bd=2)
Entry2.grid(row=2, column=1)
Button1 = Button(top, text="OK",command= process).grid(row=3, column=1)
Button1 = Button(top, text="RESET",command= reset).grid(row=3, column=0)



top.mainloop()
