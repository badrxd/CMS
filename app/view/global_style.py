

class Style:
    isDark = bool()
    icon = "resources/icons/light-mode.png"
    xl = 31
    large = 26
    meduim = 16
    small = 13
    xs = 10
    font_family = "Nunito Sans"
    font_color = "#1C4E80"
    # head_font_color = "#ecf0f1"
    head_font_color = "#1C4E80"
    login_font_color = "#ecf0f1"
    input_font_color = "#2c3e50"
    input_font_size = 12
    bg = "#ecf0f1"
    login_bg = "#0091D5"
    # header_bg = "#1C4E80"
    header_bg = "#fff"
    # sidebar_bg = "#ecf0f1"#1C4E80
    sidebar_bg = "#fff"
    sidebar_font_color = "#ecf0f1"
    # frames_bg = "#ff3767"
    frames_bg = "#fff"
    frames_font_color = "#0091D5"
    # frames_border = "#0091D5"
    frames_border = "#d3d6d7"
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
            self.bg = "#0f111a"
            self.login_bg = "#1f263c"
            self.header_bg = "#141824"
            self.sidebar_font_color = "#e2e3e6"
            self.sidebar_bg = "#141824"
            self.frames_bg = "#141824"
            self.frames_font_color = "#e2e3e6"
            self.frames_border = "#373e53"
            self.buttons_bg = "#161a2b"
            self.buttons_hover_color = "#ff3767"
        else:
            self.isDark = False
            self.icon = Style.icon
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
