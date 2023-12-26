

class Style:
    isDark = bool()
    icon = "resources/icons/light-mode.png"
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
    sidebar_bg = "#ecf0f1"
    sidebar_font_color = "#ecf0f1"
    frames_bg = "#ff3767"
    frames_font_color = "#0091D5"
    frames_border = "#0091D5"
    buttons_bg = "#1C4E80"
    buttons_hover_color = "#ff3767"

    # def __init__(self):
    #     self.make_it_dark()

    def switch_mode(self):
        if not self.isDark:
            self.isDark = True
            self.icon = "resources/icons/dark-mode.png"
            self.font_color = "#e2e3e6"
            self.head_font_color = "#e2e3e6"
            self.login_font_color = "#e2e3e6"
            self.input_font_color = "#1f263c"
            self.bg = "#161a2b"
            self.login_bg = "#1f263c"
            self.header_bg = "#1f263c"
            self.sidebar_font_color = "#e2e3e6"
            self.sidebar_bg = "#1f263c"
            self.frames_bg = "#1f263c"
            self.frames_font_color = "#e2e3e6"
            self.frames_border = "#1f263c"
            self.buttons_bg = "#161a2b"
            self.buttons_hover_color = "#ff3767"
        else:
            self.isDark = False
            self.icon = "/home/omarnem/omar/CMS/resources/icons/light-mode.png"
            self.font_color = Style.font_color
            self.head_font_color = Style.head_font_color
            self.login_font_color = Style.login_font_color
            self.input_font_color = Style.input_font_color
            self.bg = Style.bg
            self.login_bg = Style.login_bg
            self.header_bg = Style.header_bg
            self.sidebar_bg = Style.sidebar_bg
            self.sidebar_font_color = Style.sidebar_font_color
            self.frames_bg = Style.frames_bg
            self.frames_font_color = Style.frames_font_color
            self.frames_border = Style.frames_border
            self.buttons_bg = Style.buttons_bg
            self.buttons_hover_color = Style.buttons_hover_color


GStyle = Style()
