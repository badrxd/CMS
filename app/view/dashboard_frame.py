import customtkinter as ctk
import tkinter
import tkinter.messagebox
from app.core.Data_Handler.statistic import getStatistic


class DashboardFrame(ctk.CTkFrame):
    userId = ""

    def __init__(self, master, on_logout, userInfo):
        super().__init__(master)
        self.on_logout = on_logout
        self.userInfo = userInfo
        # logout_button = ctk.CTkButton(
        #     self, text="Logout", width=50, command=self.on_logout)
        logout_button = ctk.CTkButton(
            self, text="Logout", width=50, command=getStatistic)
        logout_button.pack()
