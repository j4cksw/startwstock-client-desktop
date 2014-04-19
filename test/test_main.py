import unittest
import wx
from mock import Mock

class Main():
    
    
    def open(self):
        self.app.MainLoop()
    

class MainTest(unittest.TestCase):
    
    
    def test_start_application_main_loop(self):
        app = wx.App()
        app.MainLoop = Mock()
        
        main = Main()
        main.app = app
        
        main.open()
        
        app.MainLoop.assert_called_with()

    
    def test_open_application_main_frame(self):
        pass