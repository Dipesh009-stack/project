from tkinter import*
import os
import webbrowser

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()
    
def delete4():
    screen5.destroy()

def logout():
    global screen7
    screen7.distroy()

def saved():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Saved")
    screen10.geometry("100x100")
    Label(screen10, text="Saved", fg = "green", font = ("calibri", 11)).pack()

def save():
    global filename
    global notes
    global data
    filename = raw_filename.get()
    notes = raw_notes.get()
    data = open(filename/file, "w")
    data.write(notes)
    data.close()
    saved()

def function1():
    os.system("py firstpage.py")
    
def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Success", fg = "green", font = ("Times New Roman", 11)).pack()
    Label(screen3, text="").pack()
    Button(screen3, text = "Return", width = 5, height = 1, command = delete2).pack()
    function1()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Error, try Again")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error", fg="red", font=("calibri", 11)).pack()
    Label(screen4, text="").pack()
    Button(screen4, text= "Try Again", width=5, height=1, command=delete3).pack()
    

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error, try Again")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found", fg="red", font=("calibri", 11)).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="OK, Back", width=8, height=1, command=delete4).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text = "Registration Successful", fg = "green", font = ("calibri", 11)).pack()

def login_verify():
    print("working...")
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

def register():
    global scree1
    screen1 = Toplevel(screen)
    screen1.title(" Register")
    screen1.geometry("600x500")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text="Register", bg = "blue", width = "300", height = "3", font = ("Times New Roman", 16)).pack()
    Label(screen1, text="").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "Confirm Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("600x500")
    Label(screen2, text="Login", bg = "blue", width = "300", height = "3", font = ("Times New Roman", 16)).pack()
    Label(screen2, text="").pack()
    global username_entry1
    global password_entry1
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    print("Login session started")

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x500")
    screen.title("Employee Facial Attendacne System")
    Label(text = "Employee Facial Attendacne System", bg = "blue", width = "300", height = "3", font = ("Times New Roman", 20)).pack()
    Label(text = "").pack()
    Button(text = "LOGIN", height = "4", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "REGISTER", height = "4", width = "30", command = register).pack()
    screen.mainloop()
main_screen()
