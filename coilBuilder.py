import numpy as np
import matplotlib.pyplot as plt
import magpylib as magpy
import pyvista as pv

pl = pv.Plotter(
    multi_samples=8,
    lighting='none'
)

avv = int(input("Numero di avvolgimenti:"))
l1 = int(input("Lato 1:"))
l2 = int(input("Lato 2:"))
h = float(input("Altezza bobina:"))
i = float(input("Corrente:"))

sensor = magpy.Sensor(
    position=(0, l2/2, h/2)
    )
coil = magpy.Collection()
vertices=(
            (-l1/2,0,0),
            (l1/2,0,0),
            (l1/2,l2,0),
            (-l1/2,l2,0),
            (-l1/2,0,h/avv)
        )

#Build a coil centered in the origin
for z in np.linspace(0, h, avv):
    winding = magpy.current.Line(
        current = i, 
        vertices = vertices,
        position = (0,0,z)
    )
    coil.add(winding)

magpy.show(coil, backend='pyvista', canvas=pl)
pl.show()

# compute step size based on input data
max_dim = max(l1, l2, h)
min_dim = min(l1, l2, h)
step_size = 0.01 * max_dim / (max_dim // 100)
if step_size > 0.5 * min_dim:
    step_size = 0.5 * min_dim

# create grid
grid_dim = int(max_dim * 2)
ts = np.arange(-grid_dim, grid_dim + step_size, step_size)
grid = np.array([[(x,0,z) for x in ts] for z in ts])

# calculate B-field [mT]
B = magpy.getB(sources=coil, observers=grid)
print(B)

Bamp = np.linalg.norm(B, axis=2)
Bamp /= np.amax(Bamp)

sp = plt.streamplot(
    grid[:,:,0], grid[:,:,2], B[:,:,0], B[:,:,2],
    density=2,
    color=Bamp,
    linewidth=np.sqrt(Bamp)*3,
    cmap='coolwarm'
)

plt.colorbar(sp.lines, label='[mT]')
plt.tight_layout()
plt.show()
