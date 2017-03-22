from Tkinter import * 
import tkMessageBox
import tkFileDialog


root = Tk()
root.title("Encrypt/Decrypt")


#e = 13
#n = 56291
#d = 12877

def something(): 
    print entry1.get()




LUT_encryption = dict() 
LUT_decryption = dict() 
    
def encrypt_message():
    e = int(entry2.get())
    n = int(entry1.get())
    message = textbox1.get(1.0, END)
    encrypted_msg = ""
    for i in message:
        if i in LUT_encryption:
            encrypted_msg += LUT_encryption[i]
        else:
            numerize = int(ord(i))
            encrypt = pow(numerize, e, n)
            LUT_encryption[i] = unichr(encrypt) 
            encrypted_msg += unichr(encrypt)
    
    clear_entry1()
    textbox1.insert(END, encrypted_msg)
    tkMessageBox.showinfo("Encrypted Message", "Your message has been encrypted!!")

def decrypt_message(): 
    n = int(56291) 
    d = int(12877) 
    message = textbox2.get(1.0, END) 
    decrypted_msg = ""
    for i in message:
        if i in LUT_decryption:
            decrypted_msg += LUT_decryption[i]
        else:
            numerize = ord(i)
            decrypt = pow(numerize, d, n)
            LUT_decryption[i] = unichr(decrypt) 
            decrypted_msg += unichr(decrypt)
    clear_entry2() 
    textbox2.insert(END, decrypted_msg) 
    tkMessageBox.showinfo("Decrypted Message", "Your message has been decrypted!!")
    
def clear_entry2():
    textbox2.delete(1.0, END) 
    
def clear_entry1(): 
    textbox1.delete(1.0, END) 
    
def file_save():
    f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: 
        return
    text2save = str(text.get(1.0, END)) 
    f.write(text2save)
    f.close() 
    
def open_fileQ():
    tj=open("decrypt.txt.", 'r')
    textbox1.insert(END,tj.read())
    tj.close()
    
def openfileR():
    print "success"
    f= open("decrypt.txt.", 'w')
    inputs = textbox1.get(1.0, END)
    f.write(inputs)
    f.close()
    
    
def help(): 
    tkMessageBox.showinfo("Instructions", "Put your messsage into the box below, along with your public key. Press encrypt to encrypt your message. In order to decrypt your message, paste the message in the box on the left and click decrypt.")
def close():
    root.destroy()



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

entry1 = Entry(root, width = 5)
entry1.grid(row=1, column=1)

entry2 = Entry(root, width = 5)
entry2.grid(row=2, column=1)

entry3 = Entry(root, width = 5)
entry3.grid(row=1, column=6)

entry4 = Entry(root)
entry4.grid(row = 4, column = 0) 

#entry5 = Entry(root, height = 2, width = 2)
#entry5.grid(row = 4, column= 5)

textbox1 = Text(root, height=10, width=20)
textbox1.grid(row = 4, column = 0)

textbox2 = Text(root, height=10, width=20)
textbox2.grid(row = 4, column = 5)


button1 = Button(root, text = "Encrypt", command = encrypt_message)
button1.grid(row=3, column=0)

button2 = Button(root, text = "Decrypt", command = decrypt_message)
button2.grid(row=3, column=5)




menubar = Menu(root)
filemenu =Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_fileQ)
filemenu.add_command(label="Save", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Close", command=close)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=help)
menubar.add_cascade(label="Help", menu=helpmenu)


editmenu=Menu(menubar,tearoff=0)


root.config(menu=menubar)

mainloop() 