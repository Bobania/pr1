from tkinter import *
window = Tk()
window.title("Записная книжка")
window.geometry("600x400")

d = {}





lbl = Label(window, text="1.",font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
lbl = Label(window, text="2.",font=("Arial Bold", 20))
lbl.grid(column=0, row=1)
lbl = Label(window, text="3.",font=("Arial Bold", 20))
lbl.grid(column=0, row=2)
lbl = Label(window, text="4.",font=("Arial Bold", 20))
lbl.grid(column=0, row=4)
lbl = Label(window, text="5.",font=("Arial Bold", 20))
lbl.grid(column=0, row=5)
lbl = Label(window, text="6.",font=("Arial Bold", 20))
lbl.grid(column=0, row=6)
lbl = Label(window, text="7.",font=("Arial Bold", 20))
lbl.grid(column=0, row=7)
lbl = Label(window, text="8.",font=("Arial Bold", 20))
lbl.grid(column=0, row=8)
lbl = Label(window, text="9.",font=("Arial Bold", 20))
lbl.grid(column=0, row=9)
lbl = Label(window, text="10.",font=("Arial Bold", 20))
lbl.grid(column=0, row=10)

entry1 = Entry(window)
entry1.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.02)
entry2 = Entry(window)
entry2.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.11)
entry3 = Entry(window)
entry3.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.21)
entry4 = Entry(window)
entry4.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.31)
entry5 = Entry(window)
entry5.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.4)
entry6 = Entry(window)
entry6.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.49)
entry7 = Entry(window)
entry7.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.59)
entry8 = Entry(window)
entry8.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.68)
entry9 = Entry(window)
entry9.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.78)
entry10 = Entry(window)
entry10.place(relheight=0.06, relwidth=0.3, relx=0.08, rely=0.87)






window.mainloop()
