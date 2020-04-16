from tkinter import *
import tkinter.messagebox


root = Tk()
root.title("Sign up")
root.geometry("350x200")
root.configure(background='lightblue')
my_file = open("C:/Users/User/Desktop/Python Development/Python login system/test_file.txt", "w")

def encrypt_password(passw):
    return passw[::-1]

def write_to_file(userdata_name, userdata_pass):
    main_name = str(userdata_name.get())
    main_pass = str(userdata_pass.get())
    # Encrypting password using reverse cipher
    password = encrypt_password(main_pass)
    my_file.write(main_name + "\n" + password)
    my_file.close()
    tkinter.messagebox.showinfo("Congrats on sign up!", "You signed up just fine!!")

    
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
signup = Button(root, text="Click me to sign you up", bg="Red", fg="Blue", command=lambda: write_to_file(user_name_entry, user_pass_entry), font=("cambria", 11))
signup.grid(column=0, row=5, columnspan=2)


root.mainloop()

input()