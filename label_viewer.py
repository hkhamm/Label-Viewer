import wx


class LabelViewerPanel(wx.Panel):
    """
    Parent class for other custom panels. Hides the cursor and handles
    keypress events.
    """

    def __init__(self, parent, image, panel_id, panel_size):
        wx.Panel.__init__(self, parent, id=panel_id, size=panel_size)
        self.frame = parent
        self.panel_id = panel_id
        self.Bind(wx.EVT_CHAR, self.on_keypress)
        self.cursor = wx.StockCursor(wx.CURSOR_BLANK)
        self.BackgroundColour = wx.BLACK
        self.widgets = []
        self.image = image
        # Uncomment the follow line on wxpython 2.x
        # self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.draw_image)

    def set_cursor(self):
        for widget in self.widgets:
            widget.SetCursor(self.cursor)

    def on_keypress(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.frame.close()

    def draw_image(self, event):
        """
        Draws the image to the panel's background.
        """
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        image = wx.Bitmap(self.image)
        dc.DrawBitmap(image, 0, 0)
        self.SetFocus()

    def switch_panel(self, event):
        self.frame.switch_panel(self.panel_id, event.GetEventObject().GetId())


class MainPanel(LabelViewerPanel):
    """
    Main shelf panel. When touched/clicked each object opens a new ObjectPanel.
    """

    def __init__(self, parent, image, panel_id, panel_size):
        LabelViewerPanel.__init__(self, parent, image, panel_id, panel_size)

        # Images
        self.add_image('glass', 1, (936, 290))
        self.add_image('paper', 3, (935, 665))
        self.add_image('seeds', 5, (720, 895))
        self.add_image('snail_shell', 7, (936, 766))
        self.add_image('silver_turquoise', 9, (737, 770))
        self.add_image('birch_bark', 11, (800, 530))
        self.add_image('ceramic', 13, (935, 530))
        self.add_image('eggshell', 15, (936, 50))
        self.add_image('duiker_hoof', 17, (430, 50))
        self.add_image('glass_teeth', 19, (430, 290))
        self.add_image('jade', 21, (470, 810))
        self.add_image('leather', 23, (690, 300))
        self.add_image('wood', 25, (670, 530))
        self.add_image('metal', 27, (690, 420))
        self.add_image('stone', 29, (540, 770))
        self.add_image('ivory', 31, (435, 530))

        self.set_cursor()
        self.SetFocus()

    def add_image(self, image_path, img_id, position):
        image_path = './images/shelf/' + image_path + '.png'
        bmp = wx.Bitmap(image_path, wx.BITMAP_TYPE_PNG)
        widget = wx.StaticBitmap(self, id=img_id, pos=position, bitmap=bmp)
        widget.Bind(wx.EVT_LEFT_DOWN, self.switch_panel)
        self.widgets.append(widget)


class ObjectPanel(LabelViewerPanel):
    """
    Individual object panel. Contains information and additional images about
    the object.
    """

    def __init__(self, parent, image, panel_id, panel_size):
        LabelViewerPanel.__init__(self, parent, image, panel_id, panel_size)

    def add_button(self, image_path, img_id, position):
        widget = self.add_image(image_path, img_id, position)
        widget.Bind(wx.EVT_LEFT_DOWN, self.switch_panel)
        self.widgets.append(widget)

    def add_image(self, image_path, img_id, position):
        image_path = './images/' + image_path
        bmp = wx.Bitmap(image_path, wx.BITMAP_TYPE_PNG)
        return wx.StaticBitmap(self, id=img_id, pos=position, bitmap=bmp)


class LabelPanel(ObjectPanel):
    """
    A detailed object panel. Contains information and additional images about
    the object.
    """

    def __init__(self, parent, background, buttons, panel_id, panel_size):
        ObjectPanel.__init__(self, parent, background, panel_id, panel_size)

        # Images
        # self.add_image(images[0][0], -1, images[0][1])
        # self.add_image(images[1][0], -1, images[1][1])
        # self.add_image(images[2][0], -1, images[2][1])

        # Buttons
        self.add_button('buttons/zoom.png', buttons[0], (50, 950))
        self.add_button('buttons/next.png', buttons[1], (250, 950))
        self.add_button('buttons/home.png', 0, (450, 950))

        self.set_cursor()


class ZoomPanel(ObjectPanel):
    """
    A zoomed object panel.
    """

    def __init__(self, parent, image, panel_id, label_id, panel_size):
        ObjectPanel.__init__(self, parent, image, panel_id, panel_size)

        # Buttons
        self.add_button('buttons/return.png', label_id, (50, 950))

        self.set_cursor()


class IvoryPanel(ObjectPanel):
    """
    A detailed object panel with additional image button. Contains information and additional images about
    the object.
    """

    def __init__(self, parent, background, buttons, images, panel_id, panel_size):
        ObjectPanel.__init__(self, parent, background, panel_id, panel_size)

        # Images
        self.add_image_button(images[0][0], buttons[2], images[0][1])

        # Buttons
        self.add_button('buttons/zoom.png', buttons[0], (50, 950))
        self.add_button('buttons/next.png', buttons[1], (250, 950))
        self.add_button('buttons/home.png', 0, (450, 950))

        self.set_cursor()

    def add_image_button(self, image_path, img_id, position):
        image_path = './images/' + image_path
        bmp = wx.Bitmap(image_path, wx.BITMAP_TYPE_PNG)
        widget = wx.StaticBitmap(self, id=img_id, pos=position, bitmap=bmp)
        widget.Bind(wx.EVT_LEFT_DOWN, self.switch_panel)
        self.widgets.append(widget)


class MainFrame(wx.Frame):
    """
    Main panel frame. Switches between panels.
    """

    def __init__(self, parent, image_size):
        wx.Frame.__init__(self, parent, wx.ID_ANY, size=image_size)
        self.size = image_size
        self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
        self.BackgroundColour = wx.BLACK
        self.panels = []

        # Main
        main_bg = './images/shelf/background.png'
        main_panel = MainPanel(self, main_bg, 0, image_size)
        self.panels.append(main_panel)

        # <panel id>,<zoom panel id> - Template
        # buttons = [zoom_panel_id, next_panel_id]
        # self.add_label_panel('folder/background.png', buttons, <panel id>)
        # self.add_zoom_panel('folder/large_image.png', <zoom panel id>, <panel id>)

        # 1,2 - glass
        buttons = [2, 31]
        self.add_label_panel('glass/background.png', buttons, 1)
        self.add_zoom_panel('glass/glass.png', 2, 1)

        # 3,4 - paper
        buttons = [4, 21]
        self.add_label_panel('paper/background.png', buttons, 3)
        self.add_zoom_panel('paper/paper.png', 4, 3)

        # 5,6 - seeds
        buttons = [6, 7]
        self.add_label_panel('seeds/background.png', buttons, 5)
        self.add_zoom_panel('seeds/seeds.png', 6, 5)

        # 7,8 - snail shell
        buttons = [8, 17]
        self.add_label_panel('snail_shell/background.png', buttons, 7)
        self.add_zoom_panel('snail_shell/snail_shell.png', 8, 7)

        # 9,10 - silver and turquoise
        buttons = [10, 5]
        self.add_label_panel('silver_turquoise/background.png', buttons, 9)
        self.add_zoom_panel('silver_turquoise/silver_turquoise.png', 10, 9)

        # 11, 12 - birch bark
        buttons = [12, 13]
        self.add_label_panel('birch_bark/background.png', buttons, 11)
        self.add_zoom_panel('birch_bark/birch_bark.png', 12, 11)

        # 13, 14 - ceramic
        buttons = [14, 3]
        self.add_label_panel('ceramic/background.png', buttons, 13)
        self.add_zoom_panel('ceramic/ceramic.png', 14, 13)

        # 15, 16 - eggshell
        buttons = [16, 19]
        self.add_label_panel('eggshell/background.png', buttons, 15)
        self.add_zoom_panel('eggshell/eggshell.png', 16, 15)

        # 17, 18 - duiker hoof
        buttons = [18, 15]
        self.add_label_panel('duiker_hoof/background.png', buttons, 17)
        self.add_zoom_panel('duiker_hoof/duiker_hoof.png', 18, 17)

        # 19, 20 - glass and teeth
        buttons = [20, 23]
        self.add_label_panel('glass_teeth/background.png', buttons, 19)
        self.add_zoom_panel('glass_teeth/glass_teeth.png', 20, 19)

        # 21, 22 - jade
        buttons = [2, 29]
        self.add_label_panel('jade/background.png', buttons, 21)
        self.add_zoom_panel('jade/jade.png', 22, 21)

        # 23, 24 - leather
        buttons = [24, 27]
        self.add_label_panel('leather/background.png', buttons, 23)
        self.add_zoom_panel('leather/leather.png', 24, 23)

        # 25, 26 - wood
        buttons = [26, 11]
        self.add_label_panel('wood/background.png', buttons, 25)
        self.add_zoom_panel('wood/wood.png', 26, 25)

        # 27, 28 - metal
        buttons = [28, 1]
        self.add_label_panel('metal/background.png', buttons, 27)
        self.add_zoom_panel('metal/metal.png', 28, 27)

        # 29, 30 - stone
        buttons = [30, 9]
        self.add_label_panel('stone/background.png', buttons, 29)
        self.add_zoom_panel('stone/stone.png', 30, 29)

        # 31,32 - ivory_1
        images = [['ivory/walrus.png', (868, 629)]]
        buttons = [32, 25, 33]  # [zoom_panel_id, next_panel_id, panel_2_id]
        self.add_ivory_panel('ivory/background01.png', buttons, images, 31)
        self.add_zoom_panel('ivory/ivory.png', 32, 31)

        # 33,34 - ivory_2
        buttons = [34, 25]
        self.add_label_panel('ivory/background02.png', buttons, 33)
        self.add_zoom_panel('ivory/ivory.png', 34, 33)

    def add_ivory_panel(self, background, buttons, images, panel_id):
        bg = './images/' + background
        panel = IvoryPanel(self, bg, buttons, images, panel_id, self.size)
        panel.Hide()
        self.panels.append(panel)

    def add_label_panel(self, background, buttons, panel_id):
        bg = './images/' + background
        panel = LabelPanel(self, bg, buttons, panel_id, self.size)
        panel.Hide()
        self.panels.append(panel)

    def add_zoom_panel(self, image, panel_id, label_id):
        background = './images/' + image
        panel = ZoomPanel(self, background, panel_id, label_id, self.size)
        panel.Hide()
        self.panels.append(panel)

    def switch_panel(self, src_id, dest_id):
        self.panels[src_id].Hide()
        self.panels[dest_id].Show()
        self.panels[dest_id].SetFocus()
        self.Layout()

    def close(self):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App(False)
    MainFrame(None, (1920, 1080)).Show()
    app.MainLoop()
