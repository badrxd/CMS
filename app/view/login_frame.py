import customtkinter as ctk
import tkinter
import tkinter.messagebox
from app.core.authentication import GetUser


class LoginFrame(ctk.CTkFrame):
    __loginSyle = {
        "corner_radius": 7,
        "width": 220,
        "height": 390,
        "fg_color": "#758CFE"
    }

    def __init__(self, master, on_login):
        self.__loginSyle["master"] = master
        super().__init__(
            **self.__loginSyle
        )
        self.place(relx=0.5, rely=0.5, anchor="center")
        self.master = master
        self.on_login = on_login

        name_label = ctk.CTkLabel(
            self, text="Login", font=("", 32), text_color="white")
        name_label.pack(pady=(20, 0), padx=20)

        """username input"""
        self.username = ctk.CTkEntry(
            self, placeholder_text="Enter Your Username", border_width=0, width=320, height=40, font=("", 16))
        self.username.pack(pady=(50, 10), padx=20)

        """passworld input"""
        self.password = ctk.CTkEntry(
            self, placeholder_text="Enter Your Password", border_width=0, width=320, height=40, show="*", font=("", 16))
        self.password.pack(pady=(10, 50), padx=20)

        """login button"""
        button = ctk.CTkButton(
            self, text="Login", fg_color="#3DAF8D", border_width=1, border_color="white", hover_color="#4C917D", command=self.login, font=("", 16), height=40)
        button.pack(pady=(10, 50), padx=20)

    def login(self):
        """ database connection"""
        if self.username.get() == "" or self.password.get() == "":
            tkinter.messagebox.showerror(
                "Login Failed", "Please Fill the fields")
        else:
            req = GetUser(self.username.get(), self.password.get())
            if req['status']:
                self.on_login(req['userId'])
            else:
                tkinter.messagebox.showerror(
                    "Login Failed", f"Invalid: {req['message']}")
