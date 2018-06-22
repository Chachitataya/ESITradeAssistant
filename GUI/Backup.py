#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kieltal
#
# Created:     19/06/2018
# Copyright:   (c) Kieltal 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter.ttk import *

class OverallGui:
    def __init__(self,master):
        self.master = master
        regionsIn = ['Amarr','Jita','Hek','Rens','Dodixie']
        itemsIn = ['Tritanium']

        master.title("Consultant")

        #self.label = Label(master, text="This is our first GUI!")
        #self.label.grid(row=1)
        self.labelHeader1 = Label(master, text="").grid(row=0, column=0)
        self.labelHeader2 = Label(master, text="").grid(row=0, column=2)
        self.labelHeader2 = Label(master, text="").grid(row=0, column=4)


        #self.greet_button = Button(master, text="greet", command=self.greet).grid(row=1, column=0)
        #self.greet_button.grid(row=2)
        self.close_button = Button(master, text="close", command=root.destroy).grid(row=8, column = 1)
        #self.close_button.grid(row=3)

        self.Spacer1 = Label(master, text="").grid(row=0, column=1, padx=50)
        #self.Spacer2 = Label(master, text="").grid(row=0, column=3, padx=50)
        #self.Spacer3 = Label(master, text="").grid(row=0, column=5, padx=50)

        #self.listbox1 = Listbox(master)
        #self.listbox1.config(border=2,relief=SUNKEN)
        #self.listbox1.grid(row=6, column=0)


        notebookpage = Notebook(master)
        notebookpage.grid(row=0,column=0,columnspan=50,rowspan=49,sticky='NESW')
        page1 = Frame(notebookpage)
        notebookpage.add(page1, text="FirstThing")

        page2 = Frame(notebookpage)
        notebookpage.add(page2, text="SecondThing")



        self.itempick = Combobox(master)
        #self.itempick.grid(row=5, column=0)
        self.itempick['values']=itemsIn
        self.itempick.grid(row=2,column=1)
        self.itempick.bind("<<ComboboxSelected>>",self.selectMethod)


        self.combobox1 = Combobox(master)
        self.combobox1.grid(row=5, column=0)
        self.combobox1['values']=regionsIn
        self.combobox1.bind("<<ComboboxSelected>>",self.selectMethod)

        self.combobox2 = Combobox(master)
        self.combobox2.grid(row=5, column=2)
        self.combobox2['values']=regionsIn
        self.combobox2.bind("<<ComboboxSelected>>",self.selectMethod)



        self.newtreebuy = Treeview(master)
        self.newtreebuy["columns"]=("one","two","three")
        self.newtreebuy.grid(row=7, column = 0)
        self.newtreebuy.column("one")
        self.newtreebuy.heading("one", text="Station")
        self.newtreebuy.column("two")
        self.newtreebuy.heading("two", text="Price")
        self.newtreebuy.column("three")
        self.newtreebuy.heading("three", text="Volume")
        self.newtreebuy['show'] = 'headings'

        self.newtreesell = Treeview(master)
        self.newtreesell["columns"]=("one","two","three")
        self.newtreesell.grid(row=7, column = 2)
        self.newtreesell.column("one")
        self.newtreesell.heading("one", text="Station")
        self.newtreesell.column("two")
        self.newtreesell.heading("two", text="Price")
        self.newtreesell.column("three")
        self.newtreesell.heading("three", text="Volume")
        self.newtreesell['show'] = 'headings'

    def selectMethod(self, picked):
        print("Done ")
        print(self.combobox1.get())






    def greet(self):
            print("Greetings!")


root = Tk()
my_gui = OverallGui(root)
root.mainloop()

