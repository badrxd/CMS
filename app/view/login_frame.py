import customtkinter as ctk
import tkinter
import tkinter.messagebox
from app.core.authentication import GetUser


class LoginFrame(ctk.CTkFrame):
    __loginSyle = {
        "corner_radius": 7,
        "width": 220,
        "height": 390,
        "fg_color": "#758CFE",
    }

    def __init__(self, master):
        self.__loginSyle["master"] = master
        """create login frame"""
        super().__init__(**self.__loginSyle)

        """place the frame"""
        self.place(relx=0.5, rely=0.5, anchor="center")
        self.master = master

        name_label = ctk.CTkLabel(
            self, text="Login", font=("", 32), text_color="white", bg_color="#758CFE")
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
            self, text="Login", fg_color="#3DAF8D", bg_color="#758CFE", border_width=1, border_color="white", hover_color="#4C917D", command=self.login, font=("", 16), height=40)
        button.pack(pady=(10, 50), padx=20)

    def login(self):
        """ database connection"""
        if self.username.get() == "" or self.password.get() == "":
            """display error notification"""
            self.master.notification("Please Fill the fields", "Error")

            """make the fields border red"""
            self.username.configure(border_width=1, border_color="red")
            self.password.configure(border_width=1, border_color="red")

            """back to default configurations after 2s"""
            self.master.after(2000, self.default_config)

        else:
            """get user from database"""
            req = GetUser(self.username.get(), self.password.get())

            """check if the user exists"""
            if req['status']:
                """start login"""
                self.master.notification(
                    req['message'], "Success")
                self.master.show_dashboard(req['userInfo'])
            else:
                """display error notification"""
                self.master.notification(
                    req['message'], "Error")

                """make the fields border red"""
                self.username.configure(border_width=1, border_color="red")
                self.password.configure(border_width=1, border_color="red")

                """back to default configurations after 2s"""
                self.master.after(2000, self.default_config)

    def default_config(self):
        """default confurations"""
        self.username.configure(border_width=0)
        self.password.configure(border_width=0)
