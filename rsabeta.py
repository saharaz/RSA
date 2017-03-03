from Tkinter import * 
import tkMessageBox


root = Tk()
root.title("Encrypt/Decrypt")

button1 = Button(root, text = "Encrypt")
button1.grid(row=3, column=0)

button2 = Button(root, text = "Decrypt")
button2.grid(row=3, column=5)

label1 = Label(root, text = "Encrypt", bg="yellow", anchor=W )
label1.grid(row=0, column=0, sticky=EW, columnspan=5)

label2 = Label(root, text = "Decrypt", bg="red", anchor=W )
label2.grid(row=0, column=5, sticky=EW, columnspan=2)

label3 = Label(root, text = "                 ")
label3.grid(row=0, column=2, sticky=EW, columnspan=3)

label4 = Label(root, text = "n = " )
label4.grid(row=1, column=0, sticky=EW, columnspan=2)

label5 = Label(root, text = "e = ")
label5.grid(row=2, column=0, sticky=EW, columnspan=2)

label6 = Label(root, text = "Public Key =     ")
label6.grid(row=1, column=5, sticky=EW, columnspan=2)

entry1 = Entry(root, width = 1)
entry1.grid(row=1, column=1)

entry2 = Entry(root, width = 1)
entry2.grid(row=2, column=1)

entry3 = Entry(root, width = 1)
entry3.grid(row=1, column=6)

mainloop() 