from tkinter import *
from tkcalendar import *
from data import insertd,showdata
from validation import check
from popup import mobilepop, emailpop, emailmob

screen = Tk()
screen.title("Project 1.0")
screen.geometry("400x440")
screen.config(bg='#e6f2ff')
screen.resizable(FALSE,FALSE)

# Function
def submitdata():
    fname = fname_entry.get()
    lname = lname_entry.get()
    sid = sid_entry.get()
    add = add_entry.get()
    if var.get() == 1:
        gen = "male"
    elif var.get() == 2:
        gen = "female"
    else:
        gen = "others"

    date = dob_entry.get_date()
    mobile = mob_entry.get()
    email = email_entry.get()
    valid = check(mobile, email)
    if (not valid[0] and valid[1]):
        mobilepop()
        #screen.withdraw()
    elif (valid[0] and not valid[1]):
        emailpop()
    elif (not valid[0] and not valid[1]):
        emailmob()
    else:
        insertd(fname, lname, sid, add, date, gen, mobile, email)
        fname_entry.delete( 0,END )
        lname_entry.delete( 0,END )
        sid_entry.delete( 0,END )
        add_entry.delete( 0,END )
        dob_entry.delete( 0,END )
        mob_entry.delete( 0,END )
        email_entry.delete( 0,END )

# GUI
border_label = Label(screen, text='', bg='#40a5c5', width=48, height=23,)
border_label.place(x=30, y=45)

main_label = Label(screen, text="  Student Management  ", bg='#cce5ff', fg='black', font=("Helvetica", 10, 'bold'))
main_label.place(x=123, y=20)

fname_label = Label(screen, text="First Name: ", font=("Helvetica", 10), bg="#40a5c5", fg="black")
fname_label.place(x=80, y=70)
fname_entry = Entry(screen, width=19, bd=2)
fname_entry.place(x=200, y=70)

lname_label = Label(screen, text="Last Name: ", font=("Helvetica", 10), bg="#40a5c5", fg="black")
lname_label.place(x=80, y=100)
lname_entry = Entry(screen, width=19, bd=2)
lname_entry.place(x=200, y=100)

sid_label = Label(screen, text="Student ID: ", font=("Helvetica", 10), bg="#40a5c5", fg="black")
sid_label.place(x=80, y=130)
sid_entry = Entry(screen, width=19, bd=2)
sid_entry.place(x=200, y=130)

add_label = Label(screen, text="Address: ", font=("Helvetica", 10), bg="#40a5c5", fg="black")
add_label.place(x=80, y=160)
add_entry = Entry(screen, width=19, bd=2)
add_entry.place(x=200, y=160)

dob_label = Label(screen, text="DOB: ", font=("Helvetica", 10), bg="#40a5c5", fg="black")
dob_label.place(x=80, y=190)
dob_entry = DateEntry(screen, width=9,background="#00254d")
dob_entry.place(x=200, y=190)

gender_label = Label(screen, text="Gender: ", font=("Helvetica", 10), bg="#40a5c5", fg="black")
gender_label.place(x=80, y=220)
var = IntVar()
m_btn = Radiobutton(screen, text=' Male ', variable=var, value=1, bg="#40a5c5",activebackground="#b3d7ff")
m_btn.place(x=200, y=220)
f_btn = Radiobutton(screen, text=' Female ', variable=var, value=2, bg="#40a5c5",activebackground="#b3d7ff")
f_btn.place(x=270, y=220)
o_btn = Radiobutton(screen, text=' others ', variable=var, value=3, bg="#40a5c5",activebackground="#b3d7ff")
o_btn.place(x=200, y=254)

mob_label = Label(screen, text="Mobile: ", font=("Helvetica", 10), bg="#40a5c5", fg="black")
mob_label.place(x=80, y=284)
mob_entry = Entry(screen, width=19, bd=2)
mob_entry.place(x=200, y=284)

email_label = Label(screen, text="Email: ", font=("Helvetica", 10), bg="#40a5c5", fg="black")
email_label.place(x=80, y=314)
email_entry = Entry(screen, width=19, bd=2)
email_entry.place(x=200, y=314)

submit_btn = Button(screen, text="Submit", font=("Helvetica", 10,'bold'), bg="#fe8266", fg="#00254d", bd=0, command=lambda:submitdata(), activebackground="#feac9a", activeforeground="black", width=12)
submit_btn.place(x=90, y=350)

display_btn = Button(screen, text="Display", font=("Helvetica", 10,'bold'),bg="#fcbe47", fg="#00254d", bd=0, command=showdata, activebackground="#fdd281", activeforeground="black", width=12)
display_btn.place(x=210, y=350)

exit_btn = Button(screen, text="EXIT", font=("Helvetica", 10,'bold'),bg="#4da3ff", command=screen.destroy, width=8, activebackground="white", activeforeground="#00254d", bd=0)
exit_btn.place(x=165, y=400)

screen.mainloop()
