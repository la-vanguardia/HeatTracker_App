import wx 

import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np


matplotlib.use('WXAgg')

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
        self.timer = wx.Timer( self )

        self.Bind(wx.EVT_TIMER, self._time_interval, self.timer)

        self.timer.Start( 3000 ) 

    def _time_interval( self, event ):
        #TODO: Mockup de data se debe cambiar por la implementacion de RS232
        data = np.random.randint( -70, 150, ( 255, 255 ) )
        self.draw( data )


    def draw(self, data):
        self.figure.gca()
        self.axes.imshow( data )
        self.canvas.draw()
        