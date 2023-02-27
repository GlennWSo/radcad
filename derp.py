from radcad.boolean.polydata import union, diff, common
import pyvista as pv

sp1 = pv.Sphere()
sp2 = pv.Sphere()
sp2.points[:, 0] += 0.2


diff(sp1, sp2).plot()
union(sp1, sp2).plot()
