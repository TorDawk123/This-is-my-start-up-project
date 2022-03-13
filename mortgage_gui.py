#mortgage calculator

#project
#gui

#import tkinter as tk
#import message

#define the class for gui
import tkinter as tk
import tkinter.messagebox

#define the class for gui
class MYgui:

    #create the initial self
    def __init__(self):

        #create the main window and its features
        self.mainwindow = tk.Tk()

        #create a window title
        self.mainwindow.title("mortgage calculator")

        #main loop
        tk.mainloop

        #this creates the frames and pack
        self.frame1 = tk.Frame(self.mainwindow)
        self.frame2 = tk.Frame(self.mainwindow)
        self.frame3 = tk.Frame(self.mainwindow)
        self.frame4 = tk.Frame(self.mainwindow)
        self.frame5 = tk.Frame(self.mainwindow)
        self.frame6 = tk.Frame(self.mainwindow)

        #pack these frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()

        #labels and pack for salary
        self.label1 = tk.Label(self.frame1, text="enter your salary", bg="blue", fg="pink")
        self.label1.pack(side="left")

        self.entry1 = tk.Entry(self.frame1,width=20)
        self.entry1.pack(side="left")

        #labels and pack for debt
        self.label2 = tk.Label(self.frame2, text="enter your debt", bg="black", fg="yellow")
        self.label2.pack(side="left")

        self.entry2 = tk.Entry(self.frame2,width=20)
        self.entry2.pack(side="left")

        #labels and pack for down payment for house
        self.label3 = tk.Label(self.frame3, text="enter your down payment", bg="red", fg="green")
        self.label3.pack(side="left")

        self.entry3 = tk.Entry(self.frame3,width=20)
        self.entry3.pack(side="left")

        #labels and pack for 
        self.label4 = tk.Label(self.frame4, text="enter your price of house", bg="green", fg="light yellow")
        self.label4.pack(side="left")

        self.entry4 = tk.Entry(self.frame4,width=20)
        self.entry4.pack(side="left")

        #labels and pack for 
        self.label5 = tk.Label(self.frame5, text="enter your loan years", bg="gray", fg="pink")
        self.label5.pack(side="left")

        self.entry5 = tk.Entry(self.frame5,width=20)
        self.entry5.pack(side="left")

        #the buttons
        self.button1 = tk.Button(self.frame6, text="determine",command=self.convert)
        self.button1.pack(side="left")

        self.button2 = tk.Button(self.frame6, text="quit", command=self.mainwindow.destroy)
        self.button2.pack(side="left")

    #functions
    def convert(self):
         first_entry = float(self.entry1.get())
         second_entry = float(self.entry2.get())
         third_entry = float(self.entry3.get())
         fourth_entry = float(self.entry4.get())
         fifth_entry = float(self.entry5.get())
         

         determine = second_entry / first_entry
         
         monthly_payment_base = fourth_entry - third_entry / fifth_entry

         mortgage = monthly_payment_base / 12

         tk.messagebox.showinfo("Your mortgage monthly base payment is:",mortgage)
MYgui()

        
        
        
