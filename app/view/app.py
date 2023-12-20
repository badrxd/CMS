import customtkinter as ctk
from PIL import Image
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
        self.__frames["LoginFrame"] = LoginFrame(self)
        if "DashboardFrame" in self.__frames:
            self.__frames["DashboardFrame"].destroy()
        self.__frames["LoginFrame"].place(
            relx=0.5, rely=0.5, anchor="center")

    def show_dashboard(self, userInfo):
        """
        creates dashboard frame
        and give it the user info
        """
        self.__frames["DashboardFrame"] = DashboardFrame(
            self, userInfo)
        """destroy login frame"""
        self.__frames["LoginFrame"].destroy()
        """show dashboard frame"""
        self.__frames["DashboardFrame"].grid(row=0, column=0, sticky="nwes")

    def notification(self, txt, s):
        status = {
            'Primary': {"fgc": "white"},
            'Secondary': {"fgc": "#FFCBD1"},
            'Success': {"fgc": "#03C041", "c": "white"},
            'Error': {"fgc": "#DE0A26", "c": "white"},
            'Warning': {"fgc": "#DE0A26", "c": "white"},
            'Info': {"fgc": "#DE0A26", "c": "white"},
            'Light': {"fgc": "#DE0A26", "c": "white"},
            'Dark': {"fgc": "#DE0A26", "c": "white"}
        }

        """check if there is an old popup then destroy it"""
        if hasattr(self, "popup"):
            self.popup.destroy()

        """create a popup level"""
        self.popup = ctk.CTkToplevel(self)

        """remove the top window bar"""
        self.popup.overrideredirect(True)

        """
        set a width, height and position
        the height depence on the text lenght
        """
        w = 300
        h = int(50 + (len(txt)/23) * 20)
        self.popup.geometry(
            f"{w}x{h}+{self.winfo_x()+ 50}+{self.winfo_y() + 50}")

        """Splite the popup"""
        self.popup.columnconfigure(0, weight=1)
        self.popup.rowconfigure(0, weight=1)

        """create and place a notification frame"""
        notif = ctk.CTkFrame(
            self.popup, corner_radius=7, fg_color=status[s]["fgc"], bg_color="transparent"
        )
        notif.grid(column=0, row=0, sticky="news")

        """Split the notification frame"""
        notif.columnconfigure(0, weight=1)
        notif.columnconfigure(1, weight=20)

        notif.rowconfigure(1, weight=1)

        """create and place a main frame"""
        main = ctk.CTkFrame(
            notif, fg_color="white", bg_color="white", width=200
        )
        main.grid(column=1, row=1, sticky="news")

        """Split the frame"""
        main.columnconfigure(0, weight=2)
        main.columnconfigure(1, weight=1)
        main.columnconfigure(2, weight=10)

        main.rowconfigure(0, weight=1)

        """create an image object"""
        image = ctk.CTkImage(light_image=Image.open(
            "/home/omarnem/omar/CMS/resources/icons/{}.png".format(s)))

        """add the image to a wiget"""
        image_label = ctk.CTkLabel(main, text="", image=image)
        image_label.grid(column=0, row=0, sticky="news")

        """create an text frame"""
        text_frame = ctk.CTkFrame(main, fg_color="white")
        text_frame.grid(column=2, row=0, sticky="news", pady=0)

        """Split the frame"""
        text_frame.rowconfigure(0, weight=1)
        text_frame.rowconfigure(1, weight=1)
        text_frame.columnconfigure(0, weight=1)

        """create an text labels"""
        status_label = ctk.CTkLabel(
            text_frame, text=s, font=("", 16), height=5)
        status_label.grid(row=0, column=0, sticky="ws")
        message_label = ctk.CTkLabel(
            text_frame, text=txt, height=5, width=150, wraplength=150, anchor="w")
        message_label.grid(row=1, column=0, padx=0, sticky="w")

        """wait five second then destroy the popup"""
        self.after(5000, self.popup.destroy)
