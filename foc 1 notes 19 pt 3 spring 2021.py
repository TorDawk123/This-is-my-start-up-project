#Torian Dawkins
#hw problems for tonight
#end of chapter 8 #2,3,5
#pages 434-435 in physical book
#notes today 19 pt 3
#program 66
#gui program

#convert feet to inches
#we will use labels, entry box, and buttons
#output results to a messagesbox

import tkinter
import tkinter.messagebox

#def the class
class MYgui:

    #initials the self
    def __init__(self):

        #create the mainwindow
        self.mainwindow = tkinter.Tk()

        #create 3 frames
        self.frame1 = tkinter.Frame(self.mainwindow)
        self.frame2 = tkinter.Frame(self.mainwindow)
        self.frame3 = tkinter.Frame(self.mainwindow)

        #create the title in frame1
        self.label1 = tkinter.Label(self.frame1,text="feet to inches converter",
                                    font=("arial",35),bg="black",fg="white")
        #pack
        self.label1.pack()

        #create a label and an entry box in frame2
        self.label2 = tkinter.Label(self.frame2, text="enter the value in feet: ",
                                    font=("arial",20),bg="black",fg="white")
        self.entrybox = tkinter.Entry(self.frame2,width=10)

        self.label2.pack(side="left")
        self.entrybox.pack(side="left")

        #frame 3 create 2 buttons in frame 3
        self.button1 = tkinter.Button(self.frame3, text="convert",font=("arial",15),
                                      bg="blue",fg="white",command=self.convert)
        self.button2 = tkinter.Button(self.frame3, text="quit",font=("arial",15),
                                      bg="red", fg="black",command=self.mainwindow.destroy)
        #pack button
        self.button1.pack(side="left")
        self.button2.pack(side="left")

        #pack the frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        #title of the main window
        self.mainwindow.title("Feet to inches code.")

        #background color
        self.mainwindow.configure(bg="light blue")

        #main loop
        tkinter.mainloop()

        #def callback function - this is the function that runs when button is clicked
    def convert(self):

            #get user input from entry box
        feet = float(self.entrybox.get())

            #convert feet to inches
        inches = feet * 12

            #display result in message box
        tkinter.messagebox.showinfo("results",str(feet)+"feet = " + str(inches) + "inches.")


#create an instance of the class mygui
MYgui = MYgui()

#gui hw page 655 3 and 4

        
