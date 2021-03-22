import mysql.connector
from tkinter import *
#from prettytable import from_db_cursor

def connectdatabase():
    global mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="PYproject"
    )

def insertd(name, lname, studid, add, dob, gen, smobile, semail):
    connectdatabase()
    mycursor = mydb.cursor()

    sql = "INSERT INTO students (fname, lname, studID, address, DOB, gender, mobile, email) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name, lname, studid, add, dob, gen, smobile, semail)

    mycursor.execute(sql, val)
    mydb.commit()

"""def showdata():
    connectdatabase()
    mycursor  = mydb.cursor()
    mycursor.execute("SELECT * FROM students")
    data = from_db_cursor(mycursor)

    window = Tk()
    window.geometry('1000x1000')
    window.config(bg='#e6f2ff')

    textb = Text(window,width=200)
    textb.insert(INSERT, data)
    textb.grid(row=0,column=0)

    window.mainloop()

"""
def showdata():
    connectdatabase()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM students")
    data = mycursor.fetchall()
    row=len(data)
    #print(row, data)

    root = Tk()
    root.geometry('1150x800')
    root.config(bg='#e6f2ff')

    Label(root, text="Name",fg='white',bg='#4da3ff',width=19).grid(row=0, column=0, padx=1, pady=1)
    Label(root, text="Lname",fg='white',bg='#4da3ff',width=19).grid(row=0, column=1, padx=1, pady=1)
    Label(root, text="StudID", fg='white', bg='#4da3ff', width=19).grid(row=0, column=2, padx=1, pady=1)
    Label(root, text="Adrress", fg='white', bg='#4da3ff', width=19).grid(row=0, column=3, padx=1, pady=1)
    Label(root, text="DOB", fg='white', bg='#4da3ff', width=19).grid(row=0, column=4, padx=1, pady=1)
    Label(root, text="Gender", fg='white', bg='#4da3ff', width=19).grid(row=0, column=5, padx=1, pady=1)
    Label(root, text="Mobile", fg='white', bg='#4da3ff', width=19).grid(row=0, column=6, padx=1, pady=1)
    Label(root, text="Email", fg='white', bg='#4da3ff', width=19).grid(row=0, column=7, padx=1, pady=1)

    width = 8
    for i in range(row):
        for j in range(width):
            tab=Text(root, bg='white', width=17,height=2)
            tab.insert(INSERT,data[i][j])
            tab.grid(row=i+1, column=j, padx=1, pady=1)

    root.mainloop()
