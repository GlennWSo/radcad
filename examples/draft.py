from time import time

import pyvista as pv
import numpy as np

from rscad.draft.polydata import draft_angles, draft_mask, overhangs


sp1 = pv.Sphere(radius=5)

sp1["angle"] = draft_angles(sp1, (0, 0, 1), degrees=True)
sp1.plot()


sp1.subdivide(1, inplace=True)
print(f"n faces: {sp1.n_faces}")


t0 = time()
sp1["mask"] = draft_mask(sp1, (0, 0, 1), 90, degrees=True, name="mask")
dt = time() - t0
print("mask took", dt)
sp1.set_active_scalars("mask")
sp1.plot()


sp2 = pv.Sphere().translate((0, 0, 8))

mesh = sp1 + sp2

blocked_mask = overhangs(mesh, (0, 0, 1))
mesh["blocked"] = blocked_mask
mesh.plot()

mesh.extract_points(blocked_mask).plot()
mesh.clip_scalar("blocked").plot()
