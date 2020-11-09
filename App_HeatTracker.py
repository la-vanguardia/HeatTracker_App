import numpy 
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx as NavigationToolbar
from matplotlib.figure import Figure

import wx

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        #Barra de herramientas del heatmap
        self.toolbar = NavigationToolbar(self.canvas) 
        self.toolbar.Realize()
        self.toolbar.SetBackgroundColour(wx.WHITE)
        
        #Sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL) #Forma de organizar Box
        self.sizer.Add(self.canvas, 1, wx.RIGHT | wx.TOP | wx.GROW | wx.ALL , 20) #Le agrego el gráfico al sizer
        self.sizer.Add(self.toolbar, 0,  wx.CENTER | wx.ALL,20) 
        self.SetSizer(self.sizer) #Seteo el sizer de nuestro Panel
        self.Fit()

    def draw(self):
        datos = numpy.arange(100 * 100).reshape(100, 100)
        heatmap = self.axes.imshow(datos, cmap='viridis')
        self.figure.colorbar(heatmap, ax = self.axes)
        
       


class AccionesPanel(wx.Panel):
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




if __name__ == "__main__":
    app = wx.App()

    #Ventana principal
    fr = wx.Frame(None, title='Heat Tracker',size =(900,700))
    fr.Center(True)
    fr.SetBackgroundColour(wx.WHITE)
    frsizer = wx.BoxSizer(wx.HORIZONTAL)

    #Panel del HeatMap
    panel = CanvasPanel(fr)
    panel.draw()

    #Panel de las acciones
    panel2= AccionesPanel(fr)

    #Sizer ventana principal
    frsizer.Add(panel2,0,wx.EXPAND)
    frsizer.Add(panel,1,wx.EXPAND)
    fr.SetSizer(frsizer)


    fr.Show()
    app.MainLoop()