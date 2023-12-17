from app.gui.main_window import App
from app.core.business_logic import run_logic

if __name__ == "__main__":
    app = App()
    run_logic(app)
    app.mainloop()
