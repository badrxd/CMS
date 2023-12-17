import tkinter
import tkinter.messagebox
import customtkinter
from app.core.business_logic import user_login

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    __width = 0
    __height = 0

    def __init__(self):
        super().__init__()
        self.title("CMS")
        self.__width = self.winfo_screenwidth() - 100
        self.__height = self.winfo_screenheight() - 100
        self.geometry(f"{self.__width}x{self.__height}")

    def login(self, box_width, box_height):
        """create login frame"""
        self.login_frame = customtkinter.CTkFrame(
            self, corner_radius=7, width=box_width, height=box_height)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        """username input"""
        username = customtkinter.CTkEntry(
            self.login_frame, placeholder_text="Enter Your Username", width=180, height=20)
        username.pack(pady=(50, 10), padx=20)

        """passworld input"""
        password = customtkinter.CTkEntry(
            self.login_frame, placeholder_text="Enter Your Password", width=180, height=20, show="*")
        password.pack(pady=(10, 50), padx=20)

        """login button"""
        button = customtkinter.CTkButton(
            self.login_frame, text="login", command=user_login(self))
        button.pack(pady=(10, 50), padx=20)

    def dashboard(self):
        # dashboard_frame = customtkinter.CTkFrame(
        #     self, corner_radius=7)
        # dashboard_frame.pack(pady=0, padx=0)
        self.login_frame.pack_forget()
