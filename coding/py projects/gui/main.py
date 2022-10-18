# from tkinter import *
# from tkinter.ttk import Combobox
#
# window = Tk()
# window.title('First Window')
# window.geometry('800x300')
# lbl = Label( window,text='Sinjar Academy', font=('Alkalami', 40 ) )
# lbl.grid(row=0,column=0)
# lbl1 = Label( window,text='Python Course', font=('Alkalami', 40 ) )
# lbl1.grid(row=1,column=0)
#
# def click_me():
#     res  = 'welcome ' + ent.get()
#     lbl1.configure(text=res)
#
# btn = Button(window ,command=click_me, text='Click Here', bg = 'red' , fg='yellow' , width='30',height='10')
# btn.grid(row=2,column=0 )
#
#
# ent = Entry(window , width= 20,state='disabled')
# ent.focus()
# ent.grid(row=0,column=1 )
#
# como = Combobox(window )
# como['values']= ('saman','shaker','saad','nazi', 'imad')
# como.current(0)
# como.grid(row=0,column=3)
# def select():
#     name = como.get()
#     lbl1.configure(text=name)
# btn1 = Button(window , text='Select coco',command=select )
# btn1.grid(row=1,column=2)
# window.mainloop()


# from tkinter import *
#
# from tkinter.ttk import *
#
# window = Tk()
#
# window.title("Welcome to app")
#
# window.geometry('350x200')
#
# chk_state = BooleanVar()
#
# chk_state.set(False) #set check state
#
# chk = Checkbutton(window, text='Choose', var=chk_state)
#
# chk.grid(column=0, row=0)
#
# select = IntVar()
# r1 = Radiobutton(window , text='Radio one' , value=1 , variable=select)
# r2 = Radiobutton(window , text='Radio Two',value=2 , variable=select)
# r3 = Radiobutton(window , text='Radio Three' , value=3 , variable=select)
# r1.grid(row=1,column=0)
# r2.grid(row=2,column=0)
# r3.grid(row=3,column=0)
# def radio():
#     print(select.get())
# btn =Button(window , text='Click ' , command=radio)
# btn.grid(row=4 , column=0)
# window.mainloop


#
# from tkinter import *
# from tkinter import messagebox
# from tkinter import scrolledtext
#
# window = Tk()
# window.title("Welcome to LikeGeeks app")
#
# window.geometry('450x200')
#
# txt = scrolledtext.ScrolledText(window,width=20, height=10)
# txt.insert(INSERT,'You text goes here')
# txt.delete(1.0,END)
# txt.grid(column=0,row=0)
# def show():
#     res= messagebox.askokcancel(title='Title of message' , message='Content of message')
#     print(res)
# btn = Button(window , text='Show Dialog' , command=show)
# btn.grid(row=0,column=1)
# num = IntVar()
# num.set(5)
# spin = Spinbox(window , from_=0 , to=1000000 , width=25 ,textvariable=num)
# spin.grid(row=0 , column=3)
# window.mainloop()


#
# from  tkinter import *
# window  = Tk()
# window.title('My Title')
# window.geometry('600x300')
# lbl = Label(window , text='Sinjar Academy',font=('Oswald', 30))
# lbl.grid(row=0,column=0)
# def click():
#     res = 'Welcome ' + ent.get()
#     lbl.configure(text=res)
#     print('You click Button')
# btn =Button(window , text='Click Me',command=click,height=2, width=20,bg='red' , fg='yellow')
# btn.grid(row=0 , column=1 )
#
# ent = Entry(window ,width=10 , )
# ent.focus()
# ent.grid(row=1,column=0)
# window.mainloop()


# from  tkinter import *
# from tkinter.ttk import Combobox
#
# window  = Tk()
# window.title('My Title')
# window.geometry('600x300')
# lbl = Label(window,text='Not Selected' ,font=('Oswald', 30) )
# lbl.grid(row=0,column=0)
# def clicK():
#     res = com.get()
#     lbl.configure(text=res)
# btn = Button(window , text='Click To change' ,command=clicK, bg='green')
# btn.grid(row=2,column=0)
# com = Combobox(window)
# com['values'] = ('saman' , 'lava' , 'marwan' , 'bahzani')
# com.current(1)
# com.grid(row=1,column=0)
# window.mainloop()


# from tkinter import *
#
# window = Tk()
# window.title('Check box')
# window.geometry('600x300')
# ch_state = BooleanVar()
# ch_state.set(True)
# ch = Checkbutton(window, text='Checked', variable=ch_state)
# ch.grid(row=0, column=0)
# selected = IntVar()
# rad1 = Radiobutton(window, text='Radio one', value=1 , variable=selected)
# rad2 = Radiobutton(window, text='Radio Two', value=2,variable=selected)
# rad3 = Radiobutton(window, text='Radio Three', value=3,variable=selected)
# rad1.grid(row=1, column=0)
# rad2.grid(row=2, column=0)
# rad3.grid(row=3, column=0)
#
#
# def clicked():
#
#    print(selected.get())
#
# btn = Button(window, text="Click Me", command=clicked)
#
# btn.grid(column=0, row=4)
# window.mainloop()

#
# from tkinter import *
# from tkinter import scrolledtext
# window = Tk()
# window.title("Welcome to LikeGeeks app")
# window.geometry('350x200')
#
# txt = scrolledtext.ScrolledText(window,width=20, height=10)
# txt.insert(INSERT,'Saman Scrolle text ')
# txt.grid(column=0,row=0)
# def clear():
#     txt.delete(1.0 , END)
# btn = Button(window , text='Clear' , command=clear)
# btn.grid(row=0,column=1)
# window.mainloop()





from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
window = Tk()
window.title('Message')
window.geometry('500x250')
def click():
    res=messagebox.askquestion(title='Title of message' ,message= 'Message Contet')
    print(res)
btn = Button(window,text='Show Dialog ',command=click, bg='green',fg='white')
btn.pack()
sp = Spinbox(window , from_=0 , to=10 ,width=10)
sp.pack()
spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.pack()

bar = Progressbar(window , length = 200)
bar['value'] =(70)
bar.pack()
window.mainloop()
