import imp_unittest, unittest
import wtc
import wx
import wx.webkit

#---------------------------------------------------------------------------

class webkit_Tests(wtc.WidgetTestCase):

    def test_webkit01(self):
        wk = wx.webkit.WebKitCtrl()
        wk.Create(self.frame)
        
    def test_webkit02(self):
        wk = wx.webkit.WebKitCtrl(self.frame)
        
    def test_webkit03(self):
        wk = wx.webkit.WebKitCtrl(self.frame, -1, "http://wxpython.org")


    def test_webkit04(self):
        e = wx.webkit.WebKitBeforeLoadEvent()
        
    def test_webkit05(self):
        e = wx.webkit.WebKitStateChangedEvent()

    def test_webkit06(self):
        e = wx.webkit.WebKitNewWindowEvent()

    def test_webkit07(self):
        wx.webkit.WEBKIT_STATE_START
        wx.webkit.WEBKIT_STATE_NEGOTIATING
        wx.webkit.WEBKIT_STATE_REDIRECTING
        wx.webkit.WEBKIT_STATE_TRANSFERRING
        wx.webkit.WEBKIT_STATE_STOP
        wx.webkit.WEBKIT_STATE_FAILED

        wx.webkit.WEBKIT_NAV_LINK_CLICKED
        wx.webkit.WEBKIT_NAV_BACK_NEXT
        wx.webkit.WEBKIT_NAV_FORM_SUBMITTED
        wx.webkit.WEBKIT_NAV_RELOAD
        wx.webkit.WEBKIT_NAV_FORM_RESUBMITTED
        wx.webkit.WEBKIT_NAV_OTHER
        
        wx.webkit.wxEVT_WEBKIT_STATE_CHANGED
        wx.webkit.wxEVT_WEBKIT_BEFORE_LOAD
        wx.webkit.wxEVT_WEBKIT_NEW_WINDOW
        
        wx.webkit.EVT_WEBKIT_STATE_CHANGED
        wx.webkit.EVT_WEBKIT_BEFORE_LOAD
        wx.webkit.EVT_WEBKIT_NEW_WINDOW
        
        
    def test_webkit08(self):
        wx.webkit.wxEVT_WEBKIT_STATE_CHANGED
        wx.webkit.wxEVT_WEBKIT_BEFORE_LOAD
        wx.webkit.wxEVT_WEBKIT_NEW_WINDOW
        
        wx.webkit.EVT_WEBKIT_STATE_CHANGED
        wx.webkit.EVT_WEBKIT_BEFORE_LOAD
        wx.webkit.EVT_WEBKIT_NEW_WINDOW

        
#---------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
