import wx

########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial")

        # Add a self.panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        btn = wx.Button(self.panel, label="Change Cursor")
        btn.Bind(wx.EVT_BUTTON, self.changeCursor)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(btn)
        self.panel.SetSizer(sizer)
        myCursor= wx.StockCursor(wx.CURSOR_BLANK)
        self.panel.SetCursor(myCursor)

    #----------------------------------------------------------------------
    def changeCursor(self, event):
        """"""
        myCursor= wx.StockCursor(wx.CURSOR_BLANK)
        self.panel.SetCursor(myCursor)


#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()