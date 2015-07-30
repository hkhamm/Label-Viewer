import wx


class LabelViewerPanel(wx.Panel):
    """
    Parent class for other custom panels. Hides the cursor and handles
    keypress events.
    """

    def __init__(self, parent, panel_id, panel_size):
        wx.Panel.__init__(self, parent, id=panel_id, size=panel_size)
        self.frame = parent
        self.panel_id = panel_id
        self.Bind(wx.EVT_CHAR, self.on_keypress)
        self.cursor = wx.StockCursor(wx.CURSOR_BLANK)
        self.BackgroundColour = wx.BLACK
        self.widgets = []

    def set_cursor(self):
        for widget in self.widgets:
            widget.SetCursor(self.cursor)

    def on_keypress(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.frame.close()


class MainPanel(LabelViewerPanel):
    """
    Main shelf panel. When touched/clicked each object opens a new ObjectPanel.
    """

    def __init__(self, parent, panel_id, panel_size):
        LabelViewerPanel.__init__(self, parent, panel_id, panel_size)
        # self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.draw_image)

        # Images
        self.add_image('./images/shelf/duiker_hoof_necklace.png', 0, (430, 50))
        self.add_image('./images/shelf/eggshell_necklace.png', 0, (936, 50))
        self.add_image('./images/shelf/leather_leggings.png', 0, (690, 300))
        self.add_image('./images/shelf/metal_pendant.png', 0, (690, 420))
        self.add_image('./images/shelf/ainu_necklaces.png', 0, (936, 290))
        self.add_image('./images/shelf/jade_necklace.png', 0, (450, 300))
        self.add_image('./images/shelf/turquoise_necklace.png', 0, (530, 300))
        self.add_image('./images/shelf/stone_necklace.png', 0, (430, 430))
        self.add_image('./images/shelf/ivory_necklace.png', 0, (435, 530))
        self.add_image('./images/shelf/wood_prayer_beads.png', 0, (670, 530))
        self.add_image('./images/shelf/birch_bark_necklace.png', 0, (800, 530))
        self.add_image('./images/shelf/ceramic_necklace.png', 0, (935, 530))
        self.add_image('./images/shelf/paper_necklace.png', 0, (935, 660))
        self.add_image('./images/shelf/teeth_glass_necklace.png', 0, (435, 766))
        self.add_image('./images/shelf/seed_shell_necklace.png', 0, (682, 770))
        self.add_image('./images/shelf/seed_necklace.png', 0, (690, 890))
        self.add_image('./images/shelf/snail_shell_necklace.png', 0, (936, 766))

        # Layout
        # main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # main_sizer.Add(bg, 0, wx.EXPAND)
        # self.SetSizer(main_sizer)

        self.set_cursor()
        self.SetFocus()

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
        image = wx.Bitmap('./images/home.png')
        dc.DrawBitmap(image, 0, 0)
        self.SetFocus()

    def add_image(self, image_path, img_id, position):
        bmp = wx.Bitmap(image_path, wx.BITMAP_TYPE_PNG)
        widget = wx.StaticBitmap(self, id=img_id, pos=position, bitmap=bmp)
        widget.Bind(wx.EVT_LEFT_DOWN, self.switch_panel)
        self.widgets.append(widget)

    def switch_panel(self, event):
        self.frame.switch_panel(event.GetEventObject().GetId())


class ObjectPanel(LabelViewerPanel):
    """
    Individual object panel. Contains information and additional images about
    the object.
    """

    def __init__(self, parent, panel_id, panel_size):
        LabelViewerPanel.__init__(self, parent, panel_id, panel_size)

        # Images
        image = wx.Bitmap('./images/blue720.png', wx.BITMAP_TYPE_ANY)
        bitmap0 = wx.StaticBitmap(self, bitmap=image)
        self.add_widget(bitmap0)
        # TODO add more images here

        # Layout
        # sizer = wx.BoxSizer(wx.HORIZONTAL)
        # sizer.Add(bitmap0, 0, wx.EXPAND)
        # self.SetSizer(sizer)

        self.set_cursor()

    def add_widget(self, widget):
        widget.Bind(wx.EVT_LEFT_DOWN, self.switch_panel)
        self.widgets.append(widget)

    def switch_panel(self, event):
        event.Skip()
        self.frame.switch_panel(self.panel_id)


class MainFrame(wx.Frame):
    """
    Main panel frame. Switches between panels.
    """

    def __init__(self, parent, image_size):
        wx.Frame.__init__(self, parent, wx.ID_ANY, size=image_size)
        self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
        self.BackgroundColour = wx.BLACK

        self.main_panel = MainPanel(self, -1, image_size)
        object1_panel = ObjectPanel(self, 0, image_size)
        object1_panel.Hide()
        # TODO add more panels here

        self.panels = [object1_panel]

    def switch_panel(self, index):
        if self.main_panel.IsShown():
            self.main_panel.Hide()
            self.panels[index].Show()
            self.panels[index].SetFocus()
        else:
            self.main_panel.Show()
            self.panels[index].Hide()
            self.main_panel.SetFocus()
        self.Layout()

    def close(self):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App(False)
    MainFrame(None, (1920, 1080)).Show()
    app.MainLoop()
