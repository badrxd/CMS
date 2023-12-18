import tkinter
import tkinter.messagebox
import customtkinter


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    _width = 0
    _height = 0
    login_param = False

    def __init__(self):
        super().__init__()
        self.title("CMS")
        self._width = self.winfo_screenwidth() - 100
        self._height = self.winfo_screenheight() - 100
        self.geometry(f"{self._width}x{self._height}")

    def notification(self, txt):
        notif = customtkinter.CTkLabel(
            self, text=txt, corner_radius=7, fg_color="white"
        )
        notif.pack(pady=(50, 10), padx=20)


class Login(App):
    def __init__(self, box_width, box_height, next_step):
        """create login frame"""
        super().__init__()
        self.next_step = next_step
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
            self.login_frame, text="login", command=self.checkout)
        button.pack(pady=(10, 50), padx=20)

    def checkout(self):
        self.notification("success")
        self.destroy()
        self.next_step("dash")


class Dashboard(App):
    def __init__(self, prev_step):
        """create login frame"""
        super().__init__()
        self.prev_step = prev_step
        self.login_frame = customtkinter.CTkFrame(
            self, corner_radius=7, width=self._width, height=self._height)
        self.login_frame.pack(pady=0, padx=0)
        """login button"""
        button = customtkinter.CTkButton(
            self.login_frame, text="logout", command=self.logout)
        button.pack(pady=(10, 50), padx=20)

    def logout(self):
        self.notification("success")
        self.destroy()
        self.prev_step("log")
