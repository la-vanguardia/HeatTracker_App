import wx 

import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np


matplotlib.use('WXAgg')

class CanvasPanel(wx.Panel):

    _TIME_DRAW = 1

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._figure = Figure()
        cmap = matplotlib.cm.cool
        norm = matplotlib.colors.Normalize(vmin=25, vmax=250)
        self._figure.colorbar(matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap))
        self._axes = self._figure.add_subplot(111)
        self._canvas = FigureCanvas(self, -1, self._figure)

        #Barra de herramientas del heatmap
        self.toolbar = NavigationToolbar(self._canvas) 
        self.toolbar.Realize()
        self.toolbar.SetBackgroundColour(wx.WHITE)
        
        #Sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL) #Forma de organizar Box
        self.sizer.Add(self._canvas, 1, wx.RIGHT | wx.TOP | wx.GROW | wx.ALL , 20) #Le agrego el gráfico al sizer
        self.sizer.Add(self.toolbar, 0,  wx.CENTER | wx.ALL,20) 
        self.SetSizer(self.sizer) #Seteo el sizer de nuestro Panel
        self.Fit()
        self._timer = wx.Timer( self )

        self.Bind(wx.EVT_TIMER, self._time_interval, self._timer)

        self._timer.Start( self._TIME_DRAW ) 
        

    def _time_interval( self, event ):
        #TODO: Mockup de data se debe cambiar por la implementacion de RS232
        data = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
        self.draw( data )
        


    def draw(self, data):
        self._figure.gca()
        c=self._axes.imshow(data,cmap='cool', interpolation='none')
        
        self._canvas.draw()
        