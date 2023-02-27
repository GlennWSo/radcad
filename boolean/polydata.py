# std
from typing import Optional

# thirdparty
import numpy as np
from pyvista import PolyData

# local
from radcad.boolean import core


def poly2mesh(poly: PolyData) -> core.Mesh:
    poly = poly.triangulate()
    points = poly.points
    faces = poly.faces.reshape((-1, 4))[:, 1:]
    return (points, faces)


def mesh2poly(mesh: core.Mesh) -> PolyData:
    faces = np.array(mesh[1])
    polys = np.hstack((np.full((faces.shape[0], 1), 3), faces)).ravel()
    return PolyData(mesh[0], polys)


def boolean_function(
    poly1: PolyData,
    poly2: PolyData,
    boolean_operator,
) -> Optional[PolyData]:
    m1 = poly2mesh(poly1)
    m2 = poly2mesh(poly2)
    res, tracks = boolean_operator(m1, m2)
    if res is None:
        raise Exception("core.union failed")
    poly = mesh2poly(res)
    n_faces = len(poly.faces) // 4
    poly["rid"] = np.zeros(n_faces)

    for i, (s0, s1) in enumerate(zip([0] + tracks, tracks + [n_faces])):
        poly["rid"][s0:s1] = i
    return poly


def union(poly1: PolyData, poly2: PolyData) -> Optional[PolyData]:
    """
    TODO add documentation
    """
    return boolean_function(poly1, poly2, core.union)


def common(poly1: PolyData, poly2: PolyData) -> Optional[None]:
    m1 = poly2mesh(poly1)
    m2 = poly2mesh(poly2)
    res, region = core.common(m1, m2)
    if res is None:
        raise Exception("core.common failed")
    poly = mesh2poly(res)
    return mesh2poly(res), region


def diff(poly1: PolyData, poly2: PolyData) -> Optional[None]:
    """
    TODO add documentation
    """
    return boolean_function(poly1, poly2, core.diff)
