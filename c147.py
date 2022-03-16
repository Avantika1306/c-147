from tkinter import*
root=Tk()
root.title("word to acsii code")
root.geometry("600x600")
root.configure(background="blue")
input1=Entry(root)
input1.place(relx=0.5,rely=0.3,anchor=CENTER)

def change_to_ascii_code():
    storedword=input1.get()
    for letter in storedword:
        label1["text"]+=str(ord(letter))+" "
        ascii=int(ord(letter))
        encrypted=ascii+2
        label2["text"]+=str(chr(encrypted))+" "

button1= Button(root,text="Change To Code", bg ="red",fg="white", command=change_to_ascii_code)
button1.place(relx=0.5,rely=0.4,anchor=CENTER)
label1=Label(root, text="name in ASCII", bg="yellow",fg="black")
label1.place(relx=0.5,rely=0.5,anchor=CENTER)
label2=Label(root, text="encrypted name", bg="yellow",fg="black")
label2.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()