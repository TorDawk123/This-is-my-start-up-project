#torian dawkins
#gui miles per gallon calculator
#calculator for tire rpm

#imports 
import tkinter as tk
import tkinter.messagebox

#define the class
class MYgui:

    #the function initializer
    def __init__(self):

        #create the mainwindow
        self.mainwindow = tk.Tk()

        #create the title of the main window
        self.mainwindow.title("miles per gallon")

        #create the mainloop
        tk.mainloop

        #creating frames and packing them 
        self.frame1 = tk.Frame(self.mainwindow)
        self.frame2 = tk.Frame(self.mainwindow)
        self.frame3 = tk.Frame(self.mainwindow)
        self.frame4 = tk.Frame(self.mainwindow)
        self.frame5 = tk.Frame(self.mainwindow)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        #labels and pack for miles
        self.label1 = tk.Label(self.frame1,bg="blue",fg="white",text="enter your miles")
        self.label1.pack(side="left")

        self.entry1 = tk.Entry(self.frame1,width=30)
        self.entry1.pack(side="left")

        #labels and pack for gallons
        self.label2 = tk.Label(self.frame2,bg="red",fg="black",text="enter the gallons")
        self.label2.pack(side="left")

        self.entry2 = tk.Entry(self.frame2,width=30)
        self.entry2.pack(side="left")

        #labels and entry packs for revolutions
        self.label3 = tk.Label(self.frame3,bg="green",fg="yellow",text="enter your revolutions:")
        self.label3.pack(side="left")

        self.entry3 = tk.Entry(self.frame3,width=30)
        self.entry3.pack(side="left")

        #labels and entry packs for mins
        self.label4 = tk.Label(self.frame4,text="enter the mins:",fg="white",bg="black")
        self.label4.pack(side="left")

        self.entry4 = tk.Entry(self.frame4,width=30)
        self.entry4.pack(side="left")
        

        #buttons and quit labels + pack
        self.button1 = tk.Button(self.frame5,text="Calculate", command=self.convert)
        self.button1.pack(side="left")

        self.button3 = tk.Button(self.frame5,text="Quit",command=self.mainwindow.destroy)
        self.button3.pack(side="left")

    #functions
    def convert(self):
        
        #getting the entries from the gui to the function
        miles = float(self.entry1.get())
        gallons = float(self.entry2.get())
        revs = float(self.entry3.get())
        mins = float(self.entry4.get())

        #calculate the mpg
        mpg = miles / gallons

        #calculcate the rpms of the car
        rpms = revs / mins

        if(mpg > 30):
            tk.messagebox.showinfo(mpg,"Your car has good miles per gallon!!")
        else:
            tk.messagebox.showinfo("your miles per gallon is :",mpg)

        tk.messagebox.showinfo("your cars rpms is:",rpms)
MYgui()


            
        

    

        

    

