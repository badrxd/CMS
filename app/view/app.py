import customtkinter as ctk
import tkinter
import tkinter.messagebox
from .login_frame import LoginFrame
from .dashboard_frame import DashboardFrame


""" Modes: System (standard), Dark, Light"""
ctk.set_appearance_mode("System")
"""Themes: blue (standard), green, dark-blue"""
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    width = 0
    height = 0

    __frames = {}

    def __init__(self):
        """create a window"""
        super().__init__()

        """set the title of the window"""
        self.title("CMS")

        """set resulation"""
        self.width = self.winfo_screenwidth() - 100
        self.height = self.winfo_screenheight() - 100
        self.geometry(f"{self.width}x{self.height}")

        """split the window"""
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        """create login frame"""
        self.show_login()

    def show_login(self):
        self.__frames["LoginFrame"] = LoginFrame(self, self.show_dashboard)
        if "DashboardFrame" in self.__frames:
            self.__frames["DashboardFrame"].destroy()
        self.__frames["LoginFrame"].place(
            relx=0.5, rely=0.5, anchor="center")

    def show_dashboard(self, userInfo):
        """creates dashboard frame """
        self.__frames["DashboardFrame"] = DashboardFrame(
            self, self.show_login, userInfo)
        """destroy login frame """
        self.__frames["LoginFrame"].destroy()
        """show dashboard frame"""
        self.__frames["DashboardFrame"].grid(row=0, column=0, sticky="nwes")

    def notification(self, txt):
        self.notif = ctk.CTkLabel(
            self, text=txt, corner_radius=7, fg_color="white"
        )

        self.notif.pack(pady=(50, 10), padx=20)
        self.after(3000, self.notif.destroy)
