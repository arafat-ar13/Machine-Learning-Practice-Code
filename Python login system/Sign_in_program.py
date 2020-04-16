from tkinter import *


root = Tk()
file_check = open("C:/Users/User/Desktop/Python Development/Python login system/test_file.txt", "r")
lines = file_check.read().splitlines()
file_username = lines[0]
file_userpass = lines[1]

def decrypt_password(passw):
    return passw[::-1]

file_userpass = decrypt_password(file_userpass)

print(file_username, file_userpass)

def check_login_info(name, passw):
    real_name = str(name.get())
    real_pass = str(passw.get())
    print(real_name, real_pass)
    if real_name == file_username and real_pass == file_userpass:
        print("You have successfully logged in to my system")
    else:
        print("Your info doesn't match my system. Please sign up or correct your entered info")
    file_check.close()

    
user_name = Label(root, text="Enter your username: ", font=("arial", 13, "bold"), bg="orange")
user_pass = Label(root, text="Enter password: ", font=("calibri", 13, "italic"), bg= "lime")
user_name.grid(row=2)
user_pass.grid(row=3, sticky=E)

user_name_entry = Entry(root)
user_pass_entry = Entry(root)
user_name_entry.grid(row=2, column=1)
user_pass_entry.grid(row=3, column=1)

empty_label = Label(root, bg="lightblue")
empty_label.grid(row=4)
login = Button(root, text="Sign in to your account", bg="Red", fg="Blue", command=lambda: check_login_info(user_name_entry, user_pass_entry), font=("cambria", 11))
login.grid(column=0, row=5, columnspan=2)



root.mainloop()

input()