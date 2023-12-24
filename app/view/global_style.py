

class Style:
    isDark = bool()
    large = 20
    meduim = 16
    small = 12
    font_family = "Segoe UI"
    font_color = "#1C4E80"
    head_font_color = "#ecf0f1"
    login_font_color = "#ecf0f1"
    input_font_color = "#2c3e50"
    input_font_size = 12
    bg = "#ecf0f1"
    login_bg = "#0091D5"
    header_bg = "#1C4E80"
    sidebar_bg = "#0091D5"
    frames_bg = "#ecf0f1"
    frames_font_color = "#0091D5"
    frames_border = "#0091D5"
    buttons_bg = "#1C4E80"
    buttons_hover_color = "#7E909A"

    # def __init__(self):
    #     self.make_it_dark()

    def switch_mode(self):
        if not self.isDark:
            self.isDark = True
            self.font_color = "#D4ADFC"
            self.head_font_color = "#0C134F"
            self.login_font_color = "#0C134F"
            self.input_font_color = "#2c3e50"
            self.bg = "#0C134F"
            self.login_bg = "#1D267D"
            self.header_bg = "#5C469C"
            self.sidebar_bg = "#1D267D"
            self.frames_bg = "#0C134F"
            self.frames_font_color = "#1D267D"
            self.frames_border = "#1D267D"
            self.buttons_bg = "#5C469C"
            self.buttons_hover_color = "#7E909A"
        else:
            self.isDark = False
            self.font_color = Style.font_color
            self.head_font_color = Style.head_font_color
            self.login_font_color = Style.login_font_color
            self.input_font_color = Style.input_font_color
            self.bg = Style.bg
            self.login_bg = Style.login_bg
            self.header_bg = Style.header_bg
            self.sidebar_bg = Style.sidebar_bg
            self.frames_bg = Style.frames_bg
            self.frames_font_color = Style.frames_font_color
            self.frames_border = Style.frames_border
            self.buttons_bg = Style.buttons_bg
            self.buttons_hover_color = Style.buttons_hover_color


GStyle = Style()
