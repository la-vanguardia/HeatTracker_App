import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from Panels import *

from App import *

matplotlib.use('WXAgg')



#datos de prueba 

data = np.random.randint( -70, 150, ( 255, 255 ) )

app = App()

if __name__ == "__main__":
    app.draw( data )
    app.run()
    