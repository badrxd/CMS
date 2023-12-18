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
    _width = 0
    _height = 0

    def __init__(self):
        super().__init__()
        self.title("CMS")
        self._width = self.winfo_screenwidth() - 100
        self._height = self.winfo_screenheight() - 100
        self.geometry(f"{self._width}x{self._height}")

        self.frames = {}

        # Initialize frames
        self.frames["LoginFrame"] = LoginFrame(self, self.show_dashboard)
        self.frames["DashboardFrame"] = DashboardFrame(self, self.show_login)

        # Show the initial frame
        self.show_login()

    def show_login(self):
        self.frames["DashboardFrame"].pack_forget()
        self.frames["LoginFrame"].place(
            relx=0.5, rely=0.5, anchor="center")

    def show_dashboard(self):
        self.frames["LoginFrame"].place_forget()
        self.frames["DashboardFrame"].pack()

    def notification(self, txt):
        notif = ctk.CTkLabel(
            self, text=txt, corner_radius=7, fg_color="white"
        )
        notif.pack(pady=(50, 10), padx=20)
