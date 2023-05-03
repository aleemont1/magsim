import numpy as np
import matplotlib.pyplot as plt
import magpylib as magpy

avv = int(input("Numero di avvolgimenti:"))
l1 = int(input("Lato 1:"))
l2 = int(input("Lato 2:"))
h = float(input("Altezza bobina:"))
i = float(input("Corrente:"))
sensor = magpy.Sensor()
coil = magpy.Collection()
vertices=(
            (0,0,0),
            (l1,0,0),
            (l1,l2,0),
            (0,l2,0),
            (0,0,h/avv)
        )

for z in np.linspace(0, h, avv):
    winding = magpy.current.Line(
        current = i, 
        vertices = vertices,
        position = (0,0,z)
    )
    coil.add(winding)
magpy.show(sensor, coil, backend='plotly')
#B = sensor.getB(coil)

#plt.plot(B, label=['Bx', 'By', 'Bz'])
#plt.legend()
#plt.grid(color='.8')
#plt.show()