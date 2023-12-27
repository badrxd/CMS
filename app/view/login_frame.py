import customtkinter as ctk
import tkinter
import tkinter.messagebox
from app.core.authentication import GetUser
from .global_style import GStyle, Style


class LoginFrame(ctk.CTkFrame):
    __loginSyle = {
        "corner_radius": 7,
        "width": 220,
        "height": 390,
    }

    def __init__(self, master):
        self.__loginSyle["master"] = master
        self.__loginSyle["fg_color"] = GStyle.login_bg
        self.__loginSyle["bg_color"] = GStyle.bg

        """create login frame"""
        super().__init__(**self.__loginSyle)
        """place the frame"""
        self.place(relx=0.5, rely=0.5, anchor="center")
        self.master = master

        name_label = ctk.CTkLabel(
            self, text="Login", font=(GStyle.font_family, 32, "bold"), text_color=GStyle.login_font_color, bg_color=GStyle.login_bg)
        name_label.pack(pady=(20, 0), padx=20)

        """username input"""
        self.username = ctk.CTkEntry(
            self, placeholder_text_color=GStyle.input_font_color, placeholder_text="Enter Your Username", border_width=0, width=320, height=40, font=(GStyle.font_family, GStyle.input_font_size))
        self.username.pack(pady=(50, 10), padx=20)

        """passworld input"""
        self.password = ctk.CTkEntry(
            self, placeholder_text_color=GStyle.input_font_color, placeholder_text="Enter Your Password", border_width=0, width=320, height=40, show="*", font=("", GStyle.input_font_size))
        self.password.pack(pady=(10, 50), padx=20)

        """login button"""
        button = ctk.CTkButton(
            self, text="Login", fg_color=GStyle.buttons_bg, bg_color=GStyle.login_bg, hover_color=GStyle.buttons_hover_color, command=self.login, font=(GStyle.font_family, 16), height=40, width=320)
        button.pack(pady=(10, 50), padx=20)

    def login(self):
        # dark = not self.GStyle.isDark
        # self.GStyle = Style(dark)
        # self.configure(fg_color=self.GStyle.bg)
        # print(self.GStyle.isDark)
        """ database connection"""
        if self.username.get() == "" or self.password.get() == "":
            """display error notification"""
            self.master.notification(
                "Please Fill the fields", "Error", GStyle.bg)

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
                self.master.show_dashboard(req['userInfo'])
                self.master.notification(
                    req['message'], "Success", GStyle.bg)
            else:
                """display error notification"""
                self.master.notification(
                    req['message'], "Error", GStyle.bg)

                """make the fields border red"""
                self.username.configure(border_width=1, border_color="red")
                self.password.configure(border_width=1, border_color="red")

                """back to default configurations after 2s"""
                self.master.after(2000, self.default_config)

    def default_config(self):
        """default confurations"""
        self.username.configure(border_width=0)
        self.password.configure(border_width=0)
