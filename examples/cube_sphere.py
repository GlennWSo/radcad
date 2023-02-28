from radcad.boolean.polydata import union, diff, common
import pyvista as pv

cube = pv.Cube()
sp = pv.Sphere(radius=0.6)

diff(cube, sp).plot()
union(cube, sp).plot()
common(cube, sp).plot()
