import unittest
import wx
from mock import Mock

class Main():
    
    
    def open(self):
        frame = wx.Frame(None, -1, "smartwStock")
        self.app.MainLoop()
    

class MainTest(unittest.TestCase):
    
    
    def setUp(self):
        self.app = wx.App()
        self.app.MainLoop = Mock()
        
        self.main = Main()
        self.main.app = self.app
        
        
    def test_start_application_main_loop(self):
        self.main.open()
        
        self.app.MainLoop.assert_called_with()

    
    def test_create_application_main_frame(self):
        wx.Frame = Mock()
        
        self.main.open()
        
        wx.Frame.assert_called_with(None, -1, 'smartwStock')
    
    