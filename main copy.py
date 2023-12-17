# # import tkinter
# # import tkinter.messagebox
# # import customtkinter

# # # Modes: "System" (standard), "Dark", "Light"
# # customtkinter.set_appearance_mode("System")
# # # Themes: "blue" (standard), "green", "dark-blue"
# # customtkinter.set_default_color_theme("blue")


# # def get_resolution(self):
# #     width = self.winfo_screenwidth()
# #     height = self.winfo_screenheight()
# #     return f"{width-100}x{height-100}"


# # class App(customtkinter.CTk):
# #     def __init__(self):
# #         super().__init__()

# #         # configure window
# #         self.title("CMS")
# #         # self.geometry(f"{1400}x{800}")
# #         self.geometry(get_resolution(self))


# # if __name__ == "__main__":
# #     app = App()
# #     app.mainloop()

# import tkinter as tk
# import tkinter.messagebox
# import customtkinter

# # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_appearance_mode("System")
# # Themes: "blue" (standard), "green", "dark-blue"
# customtkinter.set_default_color_theme("blue")


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         # configure window
#         self.title("CMS")
#         self.geometry(self.get_resolution())

#         # create widgets for login page
#         self.login_frame = tk.Frame(self)
#         self.login_frame.pack(expand=True, fill="both")

#         tk.Label(self.login_frame, text="Username:").pack(pady=5)
#         self.username_entry = tk.Entry(self.login_frame)
#         self.username_entry.pack(pady=5)

#         tk.Label(self.login_frame, text="Password:").pack(pady=5)
#         self.password_entry = tk.Entry(self.login_frame, show="*")
#         self.password_entry.pack(pady=5)

#         login_button = tk.Button(self.login_frame, text="Login", command=self.perform_login)
#         login_button.pack(pady=10)

#         # create widgets for dashboard
#         self.dashboard_frame = tk.Frame(self)
#         tk.Label(self.dashboard_frame, text="Dashboard").pack(pady=10)

#         # initially hide the dashboard
#         self.dashboard_frame.pack_forget()

#     def get_resolution(self):
#         width = self.winfo_screenwidth()
#         height = self.winfo_screenheight()
#         return f"{width - 100}x{height - 100}"

#     def perform_login(self):
#         entered_username = self.username_entry.get()
#         entered_password = self.password_entry.get()

#         # Replace this with your authentication logic
#         if entered_username == "user" and entered_password == "password":
#             # Show dashboard and hide login page upon successful login
#             self.login_frame.pack_forget()
#             self.dashboard_frame.pack(expand=True, fill="both")
#         else:
#             tkinter.messagebox.showerror("Login Failed", "Invalid username or password")


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the login frame
        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(side="top", fill="both", expand=True)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        ttk.Label(self.login_frame, text="Username:").pack(pady=5)
        entry_username = ttk.Entry(self.login_frame, textvariable=self.username_var)
        entry_username.pack(pady=5)

        ttk.Label(self.login_frame, text="Password:").pack(pady=5)
        entry_password = ttk.Entry(self.login_frame, textvariable=self.password_var, show="*")
        entry_password.pack(pady=5)

        btn_login = ttk.Button(self.login_frame, text="Login", command=self.login)
        btn_login.pack(pady=10)

        # Create dashboard frames
        self.dashboard_frame = ttk.Frame(self)
        self.dashboard_frame.pack(side="top", fill="both", expand=True)

        # Create sidebar frame
        self.sidebar_frame = ttk.Frame(self.dashboard_frame, width=200, height=600, relief="raised")
        self.sidebar_frame.pack(side="left", fill="y")

        # Create main section frame
        self.main_frame = ttk.Frame(self.dashboard_frame, width=600, height=600, relief="raised")
        self.main_frame.pack(side="left", fill="both", expand=True)

        # Create widgets for the main section
        self.label_section1 = ttk.Label(self.main_frame, text="This is Section 1")
        self.label_section1.pack(expand=True)

        self.label_section2 = ttk.Label(self.main_frame, text="This is Section 2", foreground="blue")
        self.label_section2.pack(expand=True)

        # Create buttons in the sidebar
        btn_section1 = ttk.Button(self.sidebar_frame, text="Section 1", command=self.show_section1)
        btn_section1.pack(pady=10)

        btn_section2 = ttk.Button(self.sidebar_frame, text="Section 2", command=self.show_section2)
        btn_section2.pack(pady=10)

        # Initially show the login frame
        self.show_login_frame()

    def show_login_frame(self):
        self.login_frame.pack(side="top", fill="both", expand=True)
        self.dashboard_frame.pack_forget()

    def show_dashboard_frame(self):
        self.dashboard_frame.pack(side="top", fill="both", expand=True)
        self.login_frame.pack_forget()

    def login(self):
        # Dummy authentication (replace with proper authentication mechanism)
        if self.username_var.get() == "user" and self.password_var.get() == "password":
            messagebox.showinfo("Login Successful", "Welcome!")
            self.show_dashboard_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_section1(self):
        self.label_section1.pack(expand=True)
        self.label_section2.pack_forget()

    def show_section2(self):
        self.label_section1.pack_forget()
        self.label_section2.pack(expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()

