from tkinter import *
import random


class PWGenerator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Password Generator")
        self.WIDTH = 650
        self.HEIGHT = 500
        self.images()
        self.window_size()
        self.frames()
        self.entrys()
        self.checkbuttons()
        self.labels()
        self.spinbox_()
        self.buttons()
        self.scrollbar()
        self.listbox()
        self.mainloop()

    def checkbuttons(self):
        self.letter1 = StringVar()
        self.letters1 = Checkbutton(self.frame1, text="English Uppercase [A - Z]", bg="white", onvalue="ABCDEFGHIJKLMNOPQRSTUVWXYZ", offvalue="", variable= self.letter1)
        self.letters1.place(relx=0.05, rely=0.1)
        self.letter2 = StringVar()
        self.letters2 = Checkbutton(self.frame1, text="English Lowercase [a - z]", bg="white", onvalue="abcdefghijklmnopqrstuvwxyz", offvalue="", variable= self.letter2)
        self.letters2.place(relx=0.05, rely=0.15)
        self.special_ = StringVar()
        self.special = Checkbutton(self.frame1, text="Special Symbols [@,!,#,$,...]", bg="white", onvalue="@!#$%&/()=?§", offvalue="", variable= self.special_)
        self.special.place(relx=0.05, rely=0.45)
        self.your_symbol = StringVar()
        self.your_symbols = Checkbutton(self.frame1, text="Other (your symbols):", bg="white", onvalue=self.entry_symbols.get(), offvalue="", variable= self.your_symbol)
        self.your_symbols.place(relx=0.05, rely=0.5)
        self.number = StringVar()
        self.numbers = Checkbutton(self.frame1, text="Numbers [0 - 10]", bg="white", onvalue="123456789", offvalue="", variable= self.number)
        self.numbers.place(relx=0.05, rely=0.2)

    def images(self):
        self.title = PhotoImage(file="pwtitle.png")

    def spinbox_(self):
        self.spinbox = Spinbox(self.frame1, from_=0, to=30)
        self.spinbox.place(relx=0.6, rely=0.27, relwidth=0.25)

    def entrys(self):
        self.entry_symbols = Entry(self.frame1, bd=2)
        self.entry_symbols.place(relx=0.1, rely=0.56)
        self.pw_list_info = Entry(self.frame2, bd=2)
        self.pw_list_info.insert(0, "Password Location")
        self.pw_list_info.place(relx=0.65, rely=0.08, relwidth=0.33, relheight=0.8)

    def labels(self):
        self.password_length = Label(self.frame1, text="Password Length:", bg="white", fg="black")
        self.password_length.place(relx=0.05, rely=0.27)
        self.general = Label(self.frame1, text="General", bg="White", fg="black", font="Arial 10 bold")
        self.general.place(relx=0.1)
        self.advanced = Label(self.frame1, text="Advanced", bg="White", fg="black", font="Arial 10 bold")
        self.advanced.place(relx=0.1, rely=0.35)

    def listbox(self):
        self.listpw = Listbox(self.root, bg="lightgrey", yscrollcommand=self.scroll.set)
        self.listpw.place(relx=0.3, rely=0.2, relheight=0.8, relwidth=0.66)

    def scrollbar(self):
        self.scroll = Scrollbar(self.root)
        self.scroll.place(relx=0.96, rely=0.2, relheight=0.8, relwidth=0.038)

    def buttons(self):
        self.generate = Button(self.frame1, text="Generate", font="Arial 8 ", bg="lightgrey", relief="ridge", command= lambda: self.password_generate())
        self.generate.place(relx=0.09, rely=0.8, relwidth=0.8, relheight=0.07)
        self.copy = Button(self.frame2, text="Copy", font="Arial 8", bg="lightgrey", relief="ridge", command=None)
        self.copy.place(relx=0.01, rely=0.1, relheight=0.8, relwidth=0.15)
        self.save = Button(self.frame2, text="Save", font="Arial 8", bg="lightgrey", relief="ridge", command= lambda: self.save_pw())
        self.save.place(relx=0.17, rely=0.1, relheight=0.8, relwidth=0.15)
        self.clear = Button(self.frame2, text="Clear", font="Arial 8", bg="lightgrey", relief="ridge", command= lambda: self.delete_list())
        self.clear.place(relx=0.33, rely=0.1, relheight=0.8, relwidth=0.15)
        self.about = Button(self.frame2, text="About", font="Arial 8", bg="lightgrey", relief="ridge")
        self.about.place(relx=0.49, rely=0.1, relheight=0.8, relwidth=0.15)

    def frames(self):
        self.frame1 = Frame(self.root, bd=3, relief = "ridge", bg="white")
        self.frame1.place(rely=0.1, relheight=0.9, relwidth=0.3)
        self.frame2 = Frame(self.root, bd=3, relief ="ridge", bg="grey")
        self.frame2.place(relx=0.3, rely=0.1, relheight=0.1, relwidth=0.7)

    def window_size(self):
        self.canvas = Canvas(self.root, width=self.WIDTH, height=self.HEIGHT, bg="white")
        self.canvas.create_image(310,25, image=self.title)
        self.canvas.pack()

    def password_generate(self):
        self.uppercase = self.letter1.get()
        self.lowercase = self.letter2.get()
        self.symbols = self.special_.get()
        self.numbers = self.number.get()
        self.yoursymbols = self.entry_symbols.get()
        self.pwlength = int(self.spinbox.get())
        self.pw = []

        for i in range(self.pwlength):
            try:
                self.pw.append(random.choice(self.uppercase + self.lowercase + self.numbers + self.symbols + self.yoursymbols))
            except:
                self.listpw.insert(END, "Couldnt create your Password")

        pwlist = "".join(self.pw)
        self.listpw.insert(END, pwlist)
        print(pwlist)

    def delete_list(self):
        self.listpw.delete(ACTIVE, last=None)

    def save_pw(self):
        with open("pwlist.txt", 'a') as f:
            f.write(self.pw_list_info.get() + ":" + self.listpw.get(ACTIVE, last=None))
            f.write('\n')
            f.close()

    def copy_list(self):
        self.listpw.get(ACTIVE, last=None)

    def mainloop(self):
        self.root.mainloop()

PWGenerator()
