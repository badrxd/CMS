
import tkinter
import customtkinter

root_tk = customtkinter.CTk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")


def button_function():
    print("omar")


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(
    master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()
