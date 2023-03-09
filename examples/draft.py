import pyvista as pv

from rscad.draft.polydata import add_draft_angles, add_draft_mask


mesh = pv.Sphere()

add_draft_angles(mesh, (0, 0, 1), degrees=True)
mesh.plot()

add_draft_mask(mesh, (0, 0, 1), 90, degrees=True, name="mask")
mesh.set_active_scalars("mask")
mesh.plot()
