from tkinter import *
from tkinter import messagebox
from db_tk import Database

win = Tk()
win.geometry('700x500')
win.configure(bg='#eef998')

db = Database('D:/mydb43.db')

def insert_data():
    fname = ent_fname.get()
    lname = ent_lname.get()
    password1 = ent_pass.get()
    password2 = ent_pass_2.get()
    name_w = ent_name_w.get()
    
    if fname and lname and password1 and name_w:  
        db.insert(fname, lname, password1, name_w)
        messagebox.showinfo("Success", "Data inserted successfully")
        clear_entries()
        
    else:
        messagebox.showerror("Error", "Please fill all fields")
        
def show_data():
    lst.delete(0, END)   
    records = db.fetch()
    for i in records:
        lst.insert(END, f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}')

def clear_entries():
    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_pass.delete(0, END)
    ent_pass_2.delete(0, END)
    ent_name_w.delete(0, END)



def login():
    entered_password = ent_pass_2.get()
    if not entered_password:
        messagebox.showerror("Error", "Please enter the password")
        return

    
    records = db.fetch()
    for record in records:
        if record[3] == entered_password:  
            messagebox.showinfo("Welcome", f"Welcome, {record[2]} {record[1]}!")  
           
            return

    messagebox.showerror("Error", "User not registered")
    
def select(event):
    clear_entries()  
    index = lst.curselection()
    if index:
        select_item = lst.get(index)
        records = select_item.split(',')

        ent_fname.insert(END, records[1])
        ent_lname.insert(END, records[2])
        ent_pass.insert(END, records[3])
        ent_name_w.insert(END, records[4])

def delete_data():
    if lst.size() == 0:  
        messagebox.showerror("Error", "No records to delete")
        return

    selected_item = lst.curselection() 
    if not selected_item:
        messagebox.showerror("Error", "Please select an item to delete")
        return

    selected_record = lst.get(selected_item)  
    record_id = selected_record.split(',')[0]  
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
    
    if confirm:
        db.remove(record_id)   
        messagebox.showinfo("Deleted", "Record deleted successfully")
        show_data()   
        clear_entries()  


    
lbl_fname = Label(win, text=':نام', font='arial 15 bold')
lbl_fname.place(x=500, y=50)

lbl_lname = Label(win, text=':نام خانوادگی', font='arial 15 bold')
lbl_lname.place(x=200, y=50)

lbl_name_w = Label(win, text=':نام دوره', font='arial 15 bold')
lbl_name_w.place(x=500, y=100)

lbl_pass = Label(win, text=':رمز ورود', font='arial 15 bold')
lbl_pass.place(x=200, y=100)

lbl_pass_2 = Label(win, text=':رمز ورود', font='arial 15 bold')
lbl_pass_2.place(x=350, y=450)

ent_pass_2 = Entry(win, font='arial 15 bold', width=25)
ent_pass_2.place(x=50, y=450)

ent_fname = Entry(win, font='arial 15 bold', width=10)
ent_fname.place(x=350, y=50)

ent_lname = Entry(win, font='arial 15 bold', width=10)
ent_lname.place(x=50, y=50)

ent_name_w = Entry(win, font='arial 15 bold', width=10)
ent_name_w.place(x=350, y=100)

ent_pass = Entry(win, font='arial 15 bold', width=10)
ent_pass.place(x=50, y=100)

lst = Listbox(win, font='arial 15', width=25)
lst.place(x=50, y=150)
lst.bind('<<ListboxSelect>>', select)   

btn_vu = Button(win, text='مشاهده همه', font='arial 12 bold', width=17, command=show_data)
btn_vu.place(x=350, y=150)

btn_insert = Button(win, text='اضافه کردن', font='arial 12 bold', width=17, command=insert_data)
btn_insert.place(x=350, y=200)

btn_reset = Button(win, text='خالی کردن ورودیها', font='arial 12 bold', width=17, command=clear_entries)
btn_reset.place(x=350, y=250)

btn_delete = Button(win, text='حذف کردن', font='arial 12 bold', width=17,command=delete_data)
btn_delete.place(x=350, y=300)

btn_exit = Button(win, text='خروج', font='arial 12 bold', width=17, command=win.destroy)
btn_exit.place(x=350, y=350)

btn_login = Button(win, text='ورود به سامانه', font='arial 12 bold', width=17,command=login)
btn_login.place(x=350, y=400)

win.mainloop()
