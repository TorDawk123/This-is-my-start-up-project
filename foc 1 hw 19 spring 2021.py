#Torian Dawkins
#homework problems
#miles per gallons calculator
#gui program

#import tkinter as tk
#tkinter messagebox

import tkinter as tk
import tkinter.messagebox

#def the class
class MYgui:

    #def initial self
    def __init__(self):

        #create the main window
        self.mainwindow = tk.Tk()

        #title mainwindow
        self.mainwindow.title("miles per gallon")

        #create frames
        self.frame1 = tk.Frame(self.mainwindow)
        self.frame2 = tk.Frame(self.mainwindow)
        self.frame3 = tk.Frame(self.mainwindow)
        self.frame4 = tk.Frame(self.mainwindow)

        #pack frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        #create title label1 and pack
        self.label1 = tk.Label(self.frame1,text="miles per gallon calculator")
        self.label1.pack()

        #label 2, entrybox, and pack to enter gallons
        self.label2 = tk.Label(self.frame2,text="enter the gallons: ",
                               font=("arial",30),bg="blue",fg="yellow")
        self.label2.pack(side="left")

        self.entrybox = tk.Entry(self.frame2,width=20)
        self.entrybox.pack(side="left")

        #label 3 and entrybox 2 and pack to enter miles
        self.label3 = tk.Label(self.frame3,text="enter the miles: ",
                               font=("arial",30),bg="grey",fg="white")
        self.label3.pack(side="left")

        self.entrybox2 = tk.Entry(self.frame3,width=30)
        self.entrybox2.pack(side="left")

        #buttons and pack for converstion
        self.button1 = tk.Button(self.frame4, text="convert", font=("arial",20),
                                 bg="white",fg="black",command=self.convert)
        self.button1.pack(side="left")

        self.button2 = tk.Button(self.frame4, text="Exit", font=("arial",15),
                                bg="white",fg="black",command=self.mainwindow.destroy)
        self.button2.pack(side="left")

        #mainloop
        tkinter.mainloop()

    def convert(self):

        #get user input from the entry box
        gallons = float(self.entrybox.get())

        miles = float(self.entrybox2.get())

        mpg = miles / gallons

        #display results in message box
        tk.messagebox.showinfo("results=", str(mpg) + "miles per gallon")

MYgui = MYgui()
        

        
        

        

        
        
