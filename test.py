from radcad.boolean.polydata import union, common, diff
import pyvista as pv

sp2 = pv.Sphere()
sp1 = pv.Sphere()

diff(sp1, sp2)
