from app.gui.main_window import Login, Dashboard
# from app import app


# def user_login(self):
#     """"""
#     app.notification("good")
#     app.login_frame.configure()


def run_dash(prev=""):
    dash = Dashboard(func[prev])
    dash.mainloop()


def run_logic(next=""):
    login = Login(250, 300, func[next])
    login.mainloop()


func = {"dash": run_logic, "log": run_dash}

if __name__ == "__main__":
    run_logic("log")
