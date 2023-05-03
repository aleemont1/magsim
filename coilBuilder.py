import numpy as np
import matplotlib.pyplot as plt
import magpylib as magpy

avv = int(input("Numero di avvolgimenti:"))
l1 = int(input("Lato 1:"))
l2 = int(input("Lato 2:"))
h = int(input("Altezza bobina:"))
i = float(input("Corrente:"))


coil = magpy.Collection()

for z in np.linspace(0, h, avv):
    winding = magpy.current.Line(
        current=i, 
        vertices=(
            (0,0,0),
            (l1,0,0),
            (l1,l2,0),
            (0,l2,0),
            (0,0,avv/h)
        ),
        position = (0,0,z)
    )
    coil.add(winding)
coil.show()
#B = sensor.getB(coil, sumup=True)

#plt.plot(B, label=['Bx', 'By', 'Bz'])
#plt.legend()
#plt.grid(color='.8')
#plt.show()