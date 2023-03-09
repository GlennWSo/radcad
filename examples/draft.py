from time import time

import pyvista as pv

from rscad.draft.polydata import draft_angles, draft_mask, overhangs


mesh = pv.Sphere(radius=5)

mesh["angle"] = draft_angles(mesh, (0, 0, 1), degrees=True)
mesh.plot()


mesh.subdivide(1, inplace=True)
print(f"n faces: {mesh.n_faces}")


t0 = time()
mesh["mask"] = draft_mask(mesh, (0, 0, 1), 90, degrees=True, name="mask")
dt = time() - t0
print("mask took", dt)
mesh.set_active_scalars("mask")
mesh.plot()

blocked_points = overhangs(mesh, (0, 0, 1))
bmesh = pv.PolyData(mesh.points[blocked_points])
bmesh.plot()
