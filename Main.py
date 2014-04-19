import wx

class Main():
    
    
    def open(self):
        self.frame.Show()
        self.app.MainLoop()


if __name__ == "__main__":
    main = Main()
    main.app = wx.App()
    main.frame = wx.Frame(None, -1, "smartwStock")
    main.open()
    
    