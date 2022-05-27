from tkinter import *
from tkinter import messagebox
import random
import pyperclip

f = None


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)





generated_password = ""
print(f"Your password is: {generated_password}")

def generate_password():
    entry3.delete(0, END)
    global generated_password
    generated_password = ""
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    for char in password_list:
        generated_password += char
    entry3.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global f
    f = open("data.txt", "a")
    website = entry1.get()
    username = entry2.get()
    password = entry3.get()

    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title="fill all form", message="Please fill all form, do not leave any field blank")
    else:
        dialog_is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {username} \nPassword: {password} \n is it ok to save?")

        if dialog_is_ok:
            text_to_write = f"{website} | {username} | {password} \r"

            f.write(text_to_write)
            f.close()
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            pyperclip.copy(generated_password)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator by Aquomedirion")
window.config(padx=20, pady=50)

canvas = Canvas(width=200, height=200)
safelock_image = PhotoImage(file="logo.png")
canvas.create_image(55, 100, image=safelock_image)
canvas.grid(column=1, row=0)

# Label 1
label1 = Label(text="Website:")
label1.grid(column=0, row=2)
# Label 2
label2 = Label(text="Email/Username:")
label2.grid(column=0, row=3)
# Label 3
label3 = Label(text="Password:")
label3.grid(column=0, row=4)

# Entry 1
entry1 = Entry()
entry1.focus()
entry1.config(width=35)
entry1.grid(sticky="w", column=1, row=2, columnspan=2)
# Entry 2
entry2 = Entry()
entry2.insert(0, "aquome@test.com")
entry2.config(width=35)
entry2.grid(sticky="w", column=1, row=3, columnspan=2)
# Entry 3
entry3 = Entry()
entry3.config(width=35)
entry3.grid(sticky="w", column=1, row=4, )

# Button 1
button1 = Button()
button1.config(text="Generate Password", command=generate_password)
button1.grid(sticky="e", column=1, row=4, )
# Button 2
button2 = Button()
button2.config(width=36, text="Add", command= save)
button2.grid(sticky="w", column=1, row=5, )
window.mainloop()
