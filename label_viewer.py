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

        # Widgets
        # background_bmp = wx.Bitmap('./images/home.png', wx.BITMAP_TYPE_PNG)
        # background = wx.StaticBitmap(self, id=0, bitmap=background_bmp)
        # self.widgets.append(background)
        # self.add_widget(background)

        img = './images/shelf/duiker_hoof_necklace.png'
        hoof_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        hoof_necklace = wx.StaticBitmap(self, id=0, pos=(430, 50),
                                        bitmap=hoof_necklace_bmp)
        self.add_widget(hoof_necklace)

        img = './images/shelf/eggshell_necklace.png'
        eggshell_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        eggshell_necklace = wx.StaticBitmap(self, id=0, pos=(936, 50),
                                            bitmap=eggshell_necklace_bmp)
        self.add_widget(eggshell_necklace)

        img = './images/shelf/leather_leggings.png'
        leather_leggings_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        leather_leggings = wx.StaticBitmap(self, id=0, pos=(690, 300),
                                           bitmap=leather_leggings_bmp)
        self.add_widget(leather_leggings)

        img = './images/shelf/metal_pendant.png'
        metal_pendant_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        metal_pendant = wx.StaticBitmap(self, id=0, pos=(690, 420),
                                        bitmap=metal_pendant_bmp)
        self.add_widget(metal_pendant)

        img = './images/shelf/ainu_necklaces.png'
        ainu_necklaces_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        ainu_necklaces = wx.StaticBitmap(self, id=0, pos=(936, 290),
                                         bitmap=ainu_necklaces_bmp)
        self.add_widget(ainu_necklaces)

        img = './images/shelf/jade_necklace.png'
        jade_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        jade_necklace = wx.StaticBitmap(self, id=0, pos=(450, 300),
                                        bitmap=jade_necklace_bmp)
        self.add_widget(jade_necklace)

        img = './images/shelf/turquoise_necklace.png'
        turquoise_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        turquoise_necklace = wx.StaticBitmap(self, id=0, pos=(530, 300),
                                             bitmap=turquoise_necklace_bmp)
        self.add_widget(turquoise_necklace)

        img = './images/shelf/stone_necklace.png'
        stone_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        stone_necklace = wx.StaticBitmap(self, id=0, pos=(430, 430),
                                         bitmap=stone_necklace_bmp)
        self.add_widget(stone_necklace)

        img = './images/shelf/ivory_necklace.png'
        ivory_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        ivory_necklace = wx.StaticBitmap(self, id=0, pos=(435, 530),
                                         bitmap=ivory_necklace_bmp)
        self.add_widget(ivory_necklace)

        img = './images/shelf/wood_prayer_beads.png'
        wood_prayer_beads_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        wood_prayer_beads = wx.StaticBitmap(self, id=0, pos=(670, 530),
                                            bitmap=wood_prayer_beads_bmp)
        self.add_widget(wood_prayer_beads)

        img = './images/shelf/birch_bark_necklace.png'
        birch_bark_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        birch_bark_necklace = wx.StaticBitmap(self, id=0, pos=(800, 530),
                                              bitmap=birch_bark_necklace_bmp)
        self.add_widget(birch_bark_necklace)

        img = './images/shelf/ceramic_necklace.png'
        ceramic_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        ceramic_necklace = wx.StaticBitmap(self, id=0, pos=(935, 530),
                                           bitmap=ceramic_necklace_bmp)
        self.add_widget(ceramic_necklace)

        img = './images/shelf/paper_necklace.png'
        paper_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        paper_necklace = wx.StaticBitmap(self, id=0, pos=(935, 660),
                                         bitmap=paper_necklace_bmp)
        self.add_widget(paper_necklace)

        img = './images/shelf/teeth_glass_necklace.png'
        teeth_glass_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        teeth_glass_necklace = wx.StaticBitmap(self, id=0, pos=(435, 766),
                                               bitmap=teeth_glass_necklace_bmp)
        self.add_widget(teeth_glass_necklace)

        img = './images/shelf/seed_shell_necklace.png'
        seed_shell_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        seed_shell_necklace = wx.StaticBitmap(self, id=0, pos=(682, 770),
                                              bitmap=seed_shell_necklace_bmp)
        self.add_widget(seed_shell_necklace)

        img = './images/shelf/seed_necklace.png'
        seed_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        seed_necklace = wx.StaticBitmap(self, id=0, pos=(690, 890),
                                        bitmap=seed_necklace_bmp)
        self.add_widget(seed_necklace)

        img = './images/shelf/snail_shell_necklace.png'
        snail_shell_necklace_bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
        snail_shell_necklace = wx.StaticBitmap(self, id=0, pos=(936, 766),
                                               bitmap=snail_shell_necklace_bmp)
        self.add_widget(snail_shell_necklace)

        # Layout
        # main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # main_sizer.Add(background, 0, wx.EXPAND)
        # self.SetSizer(main_sizer)

        self.set_cursor()
        self.SetFocus()

    def add_widget(self, widget):
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

        # Widgets
        image = wx.Bitmap('./images/blue720.png', wx.BITMAP_TYPE_ANY)
        bitmap0 = wx.StaticBitmap(self, bitmap=image)
        self.add_widget(bitmap0)
        # TODO add more widgets here

        # Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(bitmap0, 0, wx.EXPAND)
        self.SetSizer(sizer)

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
        self.Bind(wx.EVT_CHAR, self.on_keypress)

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

    def on_keypress(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.frame.close()

    def close(self):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App(False)
    MainFrame(None, (1920, 1080)).Show()
    app.MainLoop()
