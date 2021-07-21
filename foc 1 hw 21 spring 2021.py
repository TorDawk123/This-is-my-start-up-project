#Torian Dawkins
#hw 20
#gui with radio buttona

#import tkinter as tk
#import message boz
import tkinter as tk
import tkinter.messagebox

#def class mygui
class MYgui:

    #create initial the self
    def __init__(self):

    #create the mainwinow
        self.mainwindow = tk.Tk()

        #window title
        self.mainwindow.title("Long distance calls")

        #create frames
        self.frame1 = tk.Frame(self.mainwindow)
        self.frame2 = tk.Frame(self.mainwindow)
        self.frame3 = tk.Frame(self.mainwindow)
        self.frame4 = tk.Frame(self.mainwindow)
        self.frame5 = tk.Frame(self.mainwindow)

        #pack frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        #create the first label
        self.label1 = tk.Label(self.frame1,text="select a long distance call price:",font=("arial",35),bg="blue",
                               fg="pink")
        self.label1.pack()

        #create the radio buttons intvar
        self.radioVar = tk.IntVar()

        #radio button initial value
        self.radioVar.set(1)

        #the acutal radio buttons and pack
        self.radio1 = tk.Radiobutton(self.frame2,bg="green",fg="blue",font=("arial",20),text="Day time $0.07"
                                     ,variable=self.radioVar,value=1)
        self.radio1.pack()

        self.radio2 = tk.Radiobutton(self.frame2, bg="sky blue", fg="gold",font=("arial",20),text="Evening time $0.12",
                                     variable=self.radioVar,value=2)
        self.radio2.pack()

        self.radio3 = tk.Radiobutton(self.frame2, bg="dark grey", fg="purple",font=("arial",20),text="Off peak $0.05",
                                     variable=self.radioVar,value=3)
        self.radio3.pack()

        #create entry button
        self.entry1 = tk.Entry(self.frame3,width=15)
        self.entry1.pack(side="left")

        #create the button and pack

        self.button1 = tk.Button(self.frame4,font=("arial", 35),width=10,text="calculate", command=self.calculate)
        self.button1.pack(side="left")

        self.button2 = tk.Button(self.frame4,font=("arial",35),width=10,text="Exit",command=self.mainwindow.destroy)
        self.button2.pack(side="right")

        #enter the main loop
        tk.mainloop()

    #define the call back function for button one
    def calculate(self):

        pick = int(self.radioVar.get())

        minutes = float(self.entry1.get())

        #message initialize
        message = "you selected: \n"
        price = 0

        #compare if elif else
        if(pick==1):
            message+="Day time $0.07"
            price = 0.07
        elif(pick==2):
            message+="Evening time $0.12"
            price = 0.12
        else:
            message+="Off peak $0.05"
            price = 0.05

        #compute
        total = price * minutes

        message +="\n\total amount with time of day and minutes: " + str(total)

        #display
        tk.messagebox.showinfo("the total is:",total)
        

#call back the gui
MYgui = MYgui()
