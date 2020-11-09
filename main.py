from Panels import *

from App import *

#datos de prueba 

data = np.random.randint( -70, 150, ( 255, 255 ) )

app = App()

if __name__ == "__main__":
    app.draw( data )
    app.run()
    