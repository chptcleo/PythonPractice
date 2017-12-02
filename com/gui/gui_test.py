'''
@author: Wallace Chen
'''
import wx

def load(event):
    file1 = open(file_name.GetValue())
    contents.SetValue(file1.read())
    file1.close()
    
def save(event):
    file1 = open(file_name.GetValue(), 'w')
    file1.write(contents.GetValue())
    file1.close()


if __name__ == '__main__':
    app = wx.App()
    win = wx.Frame(None, title='Simple Editor', size=(410, 335))
    bkg = wx.Panel(win)
    load_btn = wx.Button(bkg, label='Open')
    load_btn.Bind(wx.EVT_BUTTON, load)
    save_btn = wx.Button(bkg, label='Save')
    save_btn.Bind(wx.EVT_BUTTON, save)
    file_name = wx.TextCtrl(bkg)
    contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
    
    hbox = wx.BoxSizer()
    hbox.Add(file_name, proportion=1, flag=wx.EXPAND)
    hbox.Add(load_btn, proportion=0, flag=wx.LEFT, border=5)
    hbox.Add(save_btn, proportion=0, flag=wx.LEFT, border=5)
    
    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
    vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
    
    bkg.SetSizer(vbox)
    win.Show()
    app.MainLoop()
