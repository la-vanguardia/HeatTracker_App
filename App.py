import wx 
from Panels import * 

class App( wx.App ): 

    def __init__( self ):
        self._app = wx.App()

        #Ventana principal
        self._fr = wx.Frame( None, title='Heat Tracker', size =(900,700) )
        self._fr.Center( True )
        self._fr.SetBackgroundColour( wx.WHITE )
        frsizer = wx.BoxSizer( wx.HORIZONTAL )

        #Panel del HeatMap
        self._canvas_panel = CanvasPanel( self._fr)
    
      


        #Panel de las acciones
        self._accion_panel= AccionPanel( self._fr )

        #Sizer ventana principal
        frsizer.Add( self._accion_panel ,wx.EXPAND)

        frsizer.Add( self._canvas_panel ,0,wx.EXPAND)
        self._fr.SetSizer(frsizer)

    def draw( self, data ):
        self._canvas_panel.draw( data )

    def run( self ):
        self._fr.Show()
        self._app.MainLoop()