from radcad.boolean.polydata import diff
import pyvista as pv

sp1 = pv.Sphere()
sp2 = pv.Sphere()
sp.points[:, 0] += 0.2


res = diff(sp1, sp2)
