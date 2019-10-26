# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:46:21 2019

@author: stud9
"""
from tkinter import *
#name = StringVar()
dep = ["Neonatal intensive care unit", "Burn center", "Coronary care unit", "Emergency department", "Intensive care unit", "Operating room", "Physical therapy"]
staff = Tk()
staff.title("Staff Page")
staff.geometry("550x450")

var = StringVar()
var.set(dep[0])

Label(staff, text = "Staff Info").grid(columnspan = 4)
Label(staff, text = "NAME:").grid(row = 1, column =  0)
Entry(staff, textvariable = '', width = 20).grid(row = 1, column = 1)
Label(staff, text = "",pady = 10).grid(columnspan = 4)
Label(staff, text = "AGE:").grid(row = 2, column =  0)
Entry(staff, textvariable = '', width = 20).grid(row = 2, column = 1)
Label(staff, text = "",pady = 10).grid(columnspan = 4)
Label(staff, text = "CELLPHONE NO:").grid(row = 3, column =  0)
Entry(staff, textvariable = '', width = 20).grid(row = 3, column = 1)

Label(staff, text = "ID:").grid(row = 1, column =  2)
Entry(staff, textvariable = '', width = 20).grid(row = 1, column = 3)
Label(staff, text = "",pady = 10).grid(columnspan = 4)
Label(staff, text = "STAFF NO:").grid(row = 2, column =  2)
Entry(staff, textvariable = '', width = 20).grid(row = 2, column = 3)
Label(staff, text = "",pady = 10).grid(columnspan = 4)
Label(staff, text = "EMAIL:").grid(row = 3, column =  2)
Entry(staff, textvariable = '', width = 20).grid(row = 3, column = 3)

Radiobutton(staff,text = "Male",value ="male",variable = 1).grid(row = 4 ,column = 0)
Radiobutton(staff,text = "Female",value ="female",variable = 1).grid(row = 4 ,column = 1)
Radiobutton(staff,text = "Doctor",value ="doctor",variable = 2).grid(row = 4 ,column = 3)
Radiobutton(staff,text = "Nurse",value ="nurse",variable = 2).grid(row = 4 ,column = 4)

Label(staff,text ="DEPARTMENT:").grid(row =5 ,column =0)
OptionMenu(staff, var, *dep).grid(row =5,column =1)

Button(staff, text = "SAVE").grid(row = 6, column = 0)
Button(staff, text = "UPDATE").grid(row = 6, column = 1)
Button(staff, text = "DELETE").grid(row = 6, column = 2)
Button(staff, text = "MENU").grid(row = 6, column = 3)

staff.mainloop()

