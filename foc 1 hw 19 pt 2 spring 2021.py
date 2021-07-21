#Torian Dawkins
#homework problem 4
#celcius fahrenheit
#foc 1 hw 19 pt 2 spring 2021

#import tkinter and messagebox
import tkinter as tk
import tkinter.messagebox

#def the class
class MYgui:

    #initials the self
    def __init__(self):

        #create the main window
        self.mainwindow = tk.Tk()

        #window title
        self.mainwindow.title("celcius to fahrenheit")

        #create the frames
        self.frame1 = tk.Frame(self.mainwindow)
        self.frame2 = tk.Frame(self.mainwindow)
        self.frame3 = tk.Frame(self.mainwindow)
        self.frame4 = tk.Frame(self.mainwindow)

        #pack frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        #create a title on the main window with th label1 and pack
        self.label1 = tk.Label(self.frame1,text="celcius to fahrenheit:",
                               font=("arial",35),bg="purple",fg="white")
        self.label1.pack()

        #create label 2 and entrybox and pack
        self.label2 = tk.Label(self.frame2,text="enter the temperature: ",
                               font=("arial",20),bg="white",fg="black")
        self.entrybox = tk.Entry(self.frame2,width=30)

        self.label2.pack(side="left")
        self.entrybox.pack(side="left")

        #create button
        self.button1 = tk.Button(self.frame3,text="calculate", font=("arial",22),
                                 bg="blue",fg="black", command=self.calculate)
        self.button1.pack(side="left")

        self.button2 = tk.Button(self.frame3,text="exit",font=("arial",22),
                                 bg="red",fg="black",command=self.mainwindow.destroy)
        self.button2.pack(side="left")

        #mainloop
        tkinter.mainloop()

        #calculate function
    def calculate(self):

        #get user input from entry box
        celcius = float(self.entrybox.get())

        fahrenheit = 9 / 5 * celcius + 32

        #display
        tk.messagebox.showinfo("results of temperature: ", str(fahrenheit) + "fahrenheit")

#final gui
MYgui = MYgui()
        
        
        

        
        
        

        
