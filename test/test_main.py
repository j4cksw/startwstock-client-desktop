import unittest
import wx
from mock import Mock
from Main import Main

class MainTest(unittest.TestCase):
    
    
    def setUp(self):
        self.app = wx.App()
        self.app.MainLoop = Mock()
        
        self.frame = wx.Frame(None)
        self.frame.Show = Mock()
        
        self.main = Main()
        self.main.app = self.app
        self.main.frame = self.frame
        
        
    def test_start_application_main_loop(self):
        self.main.open()
        
        self.app.MainLoop.assert_called_with()

    
    def test_show_application_main_frame(self):
        self.main.open()
        
        self.frame.Show.assert_called_with()
    
    