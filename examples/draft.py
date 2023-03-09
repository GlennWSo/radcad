from time import time

import pyvista as pv

from rscad.draft.polydata import add_draft_angles, add_draft_mask


mesh = pv.Sphere()

add_draft_angles(mesh, (0, 0, 1), degrees=True)
mesh.plot()


mesh.subdivide(3, inplace=True)
print(f"n faces: {mesh.n_faces}")


t0 = time()
add_draft_mask(mesh, (0, 0, 1), 90, degrees=True, name="mask")
dt = time() - t0
print("mask took", dt)
mesh.set_active_scalars("mask")
mesh.plot()
