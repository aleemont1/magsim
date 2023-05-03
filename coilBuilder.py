import numpy as np
#import matplotlib.pyplot as plt
import magpylib as magpy
import pyvista as pv

avv = int(input("Numero di avvolgimenti:"))
l1 = int(input("Lato 1:"))
l2 = int(input("Lato 2:"))
h = float(input("Altezza bobina:"))
i = float(input("Corrente:"))
sensor = magpy.Sensor()
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
magpy.show(sensor, coil, backend='plotly')

grid = pv.UniformGrid(
    dimensions=(l1, l1, l1),
    spacing=(2, 2, 2),
)

grid['B'] = coil.getB(grid.points)

seed = pv.Disc(inner=1, outer=5.2, r_res=3, c_res=12)
strl = grid.streamlines_from_source(
    seed,
    vectors='B',
    max_time=180,
    initial_step_length=0.01,
    integration_direction='both',
)

# create plotting scene
pl = pv.Plotter()

# add field lines and legend to scene
legend_args = {
    'title': 'B [mT]',
    'title_font_size': 20,
    'color': 'black',
    'position_y': 0.25,
    'vertical': True,
}

# draw coils
magpy.show(coil, canvas=pl, backend='pyvista')

# add streamlines
pl.add_mesh(
    strl.tube(radius=.2),
    cmap="bwr",
    scalar_bar_args=legend_args,
)
# display scene
pl.camera.position=(160, 10, -10)
pl.set_background("white")
pl.show()