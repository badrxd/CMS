import customtkinter as ctk
import tkinter
import tkinter.messagebox
from .login_frame import LoginFrame
from .dashboard_frame import DashboardFrame


# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    __width = 0
    __height = 0

    def __init__(self):
        super().__init__()
        self.title("CMS")
        self.width = self.winfo_screenwidth() - 100
        self.height = self.winfo_screenheight() - 100
        self.geometry(f"{self.__width}x{self.__height}")

        self.frames = {}
        self.notif = None

        # Initialize frames
        # self.frames["DashboardFrame"] = DashboardFrame(self, self.show_login)
        # self.frames["LoginFrame"] = LoginFrame(self, self.show_dashboard)

        # Show the initial frame
        self.show_login()

    def show_login(self):
        self.frames["LoginFrame"] = LoginFrame(self, self.show_dashboard)
        if "DashboardFrame" in self.frames:
            self.frames["DashboardFrame"].destroy()
        self.frames["LoginFrame"].place(
            relx=0.5, rely=0.5, anchor="center")

    def show_dashboard(self):
        self.frames["DashboardFrame"] = DashboardFrame(self, self.show_login)
        self.frames["LoginFrame"].destroy()
        self.frames["DashboardFrame"].pack()

    def notification(self, txt):
        self.notif = ctk.CTkLabel(
            self, text=txt, corner_radius=7, fg_color="white"
        )

        self.notif.pack(pady=(50, 10), padx=20)
