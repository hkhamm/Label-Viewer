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
        self.add_image('duiker_hoof_necklace', 0, (430, 50))
        self.add_image('eggshell_necklace', 1, (936, 50))
        self.add_image('teeth_glass_necklace', 13, (430, 290))
        self.add_image('leather_leggings', 2, (690, 300))
        self.add_image('metal_pendant', 12, (690, 420))
        self.add_image('ainu_necklaces', 1, (936, 290))
        self.add_image('ivory_necklace', 7, (435, 530))
        self.add_image('wood_prayer_beads', 16, (670, 530))
        self.add_image('birch_bark_necklace', 10, (800, 530))
        self.add_image('ceramic_necklace', 134, (935, 530))
        self.add_image('paper_necklace', 3, (935, 665))
        self.add_image('jade_necklace', 15, (470, 810))
        self.add_image('stone_necklace', 8, (540, 770))
        self.add_image('turquoise_necklace', 11, (737, 770))
        self.add_image('seed_necklaces', 5, (720, 895))
        self.add_image('snail_shell_necklace', 9, (936, 766))

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

    def __init__(self, parent, background, images, buttons, panel_id, panel_size):
        LabelViewerPanel.__init__(self, parent, background, panel_id, panel_size)

        # Images
        self.add_image(images[0][0], -1, images[0][1])
        self.add_image(images[1][0], -1, images[1][1])
        self.add_image(images[2][0], -1, images[2][1])

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

        # 1,2 - Ainu necklace
        images = [['ainu_necklace/ainu_necklaces_s.png', (50, 50)],
                  ['ainu_necklace/ainu_map.png', (870, 650)],
                  ['ainu_necklace/ainu_woman.png', (1525, 650)]]
        buttons = [2, 999]  # [zoom_panel_id, next_panel_id]
        self.add_label_panel('ainu_necklace/background.png', images, buttons, 1)
        self.add_zoom_panel('ainu_necklace/ainu_necklaces.png', 2, 1)

        # 3,4 - Paper necklace
        images = [['paper_necklace/paper_necklace_s.png', (50, 50)],
                  ['blank.png', (0, 0)],
                  ['paper_necklace/samoan_woman.png', (1525, 650)]]
        buttons = [4, 999]  # [zoom_panel_id, next_panel_id]
        self.add_label_panel('paper_necklace/background.png', images, buttons, 3)
        self.add_zoom_panel('paper_necklace/paper_necklace.png', 4, 3)

        # 5,6 - Seed necklaces
        images = [['seed_necklaces/seed_necklaces_s.png', (50, 50)],
                  ['seed_necklaces/jobs_tears.png', (870, 595)],
                  ['seed_necklaces/papua_new_guinea_woman.png', (1277, 595)]]
        buttons = [6, 999]  # [zoom_panel_id, next_panel_id]
        self.add_label_panel('seed_necklaces/background.png', images, buttons, 5)
        self.add_zoom_panel('seed_necklaces/seed_necklaces.png', 6, 5)

        # 7,8 - Ivory necklace
        images = [['ivory_necklace/ivory_necklace_s.png', (50, 50)],
                  ['blank.png', (0, 0)],
                  ['ivory_necklace/walrus.png', (900, 645)]]
        buttons = [8, 999]  # [zoom_panel_id, next_panel_id]
        self.add_label_panel('ivory_necklace/background.png', images, buttons, 7)
        self.add_zoom_panel('ivory_necklace/ivory_necklace.png', 8, 7)

        # 9,10 - Snail necklace
        images = [['snail_necklace/snail_necklace_s.png', (50, 50)],
                  ['blank.png', (0, 0)],
                  ['snail_necklace/periwinkle_snail.png', (960, 740)]]
        buttons = [10, 999]  # [zoom_panel_id, next_panel_id]
        self.add_label_panel('snail_necklace/background.png', images, buttons, 9)
        self.add_zoom_panel('snail_necklace/snail_necklace.png', 10, 9)

        # 11,12 - Turquoise necklace
        images = [['turquoise_necklace/turquoise_necklace_s.png', (50, 50)],
                  ['blank.png', (0, 0)],
                  ['turquoise_necklace/navajo_metalsmith.png', (865, 540)]]
        buttons = [12, 999]  # [zoom_panel_id, next_panel_id]
        self.add_label_panel('turquoise_necklace/background.png', images, buttons, 11)
        self.add_zoom_panel('turquoise_necklace/turquoise_necklace.png', 12, 11)

    def add_label_panel(self, background, images, buttons, panel_id):
        bg = './images/' + background
        panel = LabelPanel(self, bg, images, buttons, panel_id, self.size)
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
