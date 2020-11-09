import wx

class AccionPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)

        #Botones
        self.BtIniciar = wx.Button(self, -1, "Iniciar")
        self.BtParar = wx.Button(self,-1,"Parar")

        #Imput
        self.LabelTiempT= wx.StaticText(self,-1,"Tiempo total [seg]")
        self.Tiempototal= wx.TextCtrl(self,value="60",size=(50,20),style=wx.TE_PROCESS_ENTER)



        #Sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.BtIniciar, 0,  wx.LEFT | wx.LEFT | wx.TOP , 20) 
        self.sizer.Add(self.BtParar, 0,  wx.LEFT | wx.LEFT | wx.TOP , 20)
        self.sizer.Add(self.LabelTiempT, 0,  wx.CENTER | wx.LEFT | wx.TOP ,20)  
        self.sizer.Add(self.Tiempototal, 0, wx.CENTER | wx.TOP , 5) 
        self.SetSizer(self.sizer)
        self.Fit()
