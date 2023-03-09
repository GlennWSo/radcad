# std
from typing import Optional

# thirdparty
import numpy as np
from pyvista import PolyData

# local
from . import core


def add_draft_angles(mesh, ref_normal, name="angle", degrees=False, face=True):
    if face:
        normals = mesh.face_normals
    else:
        normals = mesh.point_normals

    mesh["angle"] = core.normals2angles(normals, ref_normal, degrees)


def add_draft_mask(mesh, ref_normal, value, name="Top", degrees=False, face=True):
    if face:
        normals = mesh.face_normals
    else:
        normals = mesh.point_normals

    if degrees:
        value = np.deg2rad(value)

    mesh[name] = core.draft_mask(normals, ref_normal, value)
