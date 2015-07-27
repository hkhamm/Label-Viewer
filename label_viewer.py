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
        self.widget_count = 0
        image = wx.Bitmap('./images/home.png', wx.BITMAP_TYPE_ANY)
        bitmap0 = wx.StaticBitmap(self, id=0, bitmap=image)
        self.add_widget(bitmap0)
        # TODO add more widgets here

        # Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(bitmap0, 0, wx.ALL)
        self.SetSizer(sizer)

        self.set_cursor()

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
        sizer.Add(bitmap0, 0, wx.ALL)
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
    MainFrame(None, (1280, 720)).Show()
    app.MainLoop()
