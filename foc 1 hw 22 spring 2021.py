#torian dawkins
#hw 22
#check buttons hw
#hw 655 problem 6

#import function
import tkinter as tk
import tkinter.messagebox

#class
class MYgui:

    #initialize
    def __init__(self):

        #create a mainwindow
        self.mainwindow = tk.Tk()

        #create the mainwinodw title
        self.mainwindow.title("automotive services")

        #cretae frames
        self.frame1 = tk.Frame(self.mainwindow)
        self.frame2 = tk.Frame(self.mainwindow)
        self.frame3 = tk.Frame(self.mainwindow)
        self.frame4 = tk.Frame(self.mainwindow)
        

        #pack windows
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        

        #create the first label and pack it
        self.label1 = tk.Label(self.frame1, text="automotive services:",font=("arial",35),
                               bg="orange",fg="black")
        self.label1.pack()

        #create the 7 IntVar objects, one for each checkbutton,set to 0 meaning unchecked
        self.cb1 = tk.IntVar()
        self.cb1.set(0)
        
        self.cb2 = tk.IntVar()
        self.cb2.set(0)
        
        self.cb3 = tk.IntVar()
        self.cb3.set(0)
        
        self.cb4 = tk.IntVar()
        self.cb4.set(0)
        
        self.cb5 = tk.IntVar()
        self.cb5.set(0)
        
        self.cb6 = tk.IntVar()
        self.cb6.set(0)

        self.cb7 = tk.IntVar()
        self.cb7.set(0)

        #create the checkbuttons and pack them
        self.check1 = tk.Checkbutton(self.frame2,text="oil change $30.00",font=("arial",30),bg="blue",
                                     fg="yellow",variable=self.cb1)
        self.check1.pack()

        self.check2 = tk.Checkbutton(self.frame2,text="Lube job $20.00",font=("arial",30),
                                     bg="green",fg="purple",variable=self.cb2)
        self.check2.pack()

        self.check3 = tk.Checkbutton(self.frame2,text="Radiator Flush $40.00",font=("arial",30),
                                     bg="white",fg="green",variable=self.cb3)
        self.check3.pack()

        self.check4 = tk.Checkbutton(self.frame2,text="Transmission Flush $100.00",font=("arial",30),
                                     bg="gray",fg="red",variable=self.cb4)
        self.check4.pack()

        self.check5 = tk.Checkbutton(self.frame2,text="Inspection $35.00",font=("arial",30),
                                     bg="gray",fg="yellow",variable=self.cb5)
        self.check5.pack()

        self.check6 = tk.Checkbutton(self.frame2,text="Muffler Replacement $200.00",font=("arial",30),
                                     bg="pink",fg="light green",variable=self.cb6)
        self.check6.pack()

        self.check7 = tk.Checkbutton(self.frame2,text="Tire Rotation $20.00",font=("arial",30),bg="green",
                                     fg="pink",variable=self.cb7)
        self.check7.pack()

        #create a stringvar() object in frame3 and associate it with label
        self.value = tk.StringVar()
        self.label2 = tk.Label(self.frame3,textvariable=self.value,font=("arial",20),bg="blue")

        self.label2.pack()

        #create the buttons
        self.button1 = tk.Button(self.frame4,text="Total services",width=15,bg="white",fg="black",
                                 command=self.calculate)
        self.button1.pack(side="left")

        self.button2 = tk.Button(self.frame4,text="quit", width=15,bg="white",fg="black",
                                 command=self.mainwindow.destroy)
        self.button2.pack(side="right")

        #enter the mainloop
        tk.mainloop()

    #create the compute function
    def calculate(self):

        #initalize two variables
        amount = 0
        message = "your services are as followed: "

        #compare if elif else with checks its always if no elif or else
        if(self.cb1.get() == 1):
            amount += 30.00
            message += "oil change"
        if(self.cb2.get() == 2):
            amount += 20.00
            message += "Lube job"
        if(self.cb3.get() == 3):
            amount += 40.00
            message += "Radiator flush"
        if(self.cb4.get() == 4):
            amount += 100.00
            message += "Transmission flush"
        if(self.cb5.get() == 5):
            amount += 35.00
            message += "Inspection"
        if(self.cb6.get() == 6):
            amount += 200.00
            message += "Muffler replacement"
        if(self.cb7.get() == 7):
            amount += 20.00
            message += "Tire rotation"

        #compute tax and total
        tax = amount * 0.0875
        total = amount + tax

        #message box
        tk.messagebox.showinfo("services amount:",total)

#call the function
MYgui = MYgui()

            
            
        
                                     
































        
