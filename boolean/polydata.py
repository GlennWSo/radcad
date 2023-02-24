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


def union(poly1: PolyData, poly2: PolyData) -> Optional[None]:
    m1 = poly2mesh(poly1)
    m2 = poly2mesh(poly2)
    res, region = core.union(m1, m2)
    print(region)
    if res is None:
        raise Exception("core.union failed")
    poly = mesh2poly(res)
    poly["rid"] = region
    return mesh2poly(res)


def common(poly1: PolyData, poly2: PolyData) -> Optional[None]:
    m1 = poly2mesh(poly1)
    m2 = poly2mesh(poly2)
    res, region = core.common(m1, m2)
    if res is None:
        raise Exception("core.common failed")
    poly = mesh2poly(res)
    poly["rid"] = region
    return mesh2poly(res)


def diff(poly1: PolyData, poly2: PolyData) -> Optional[None]:
    m1 = poly2mesh(poly1)
    m2 = poly2mesh(poly2)
    res, region = core.diff(m1, m2)
    if res is None:
        raise Exception("core.diff failed")
    poly = mesh2poly(res)
    poly["rid"] = region
    return mesh2poly(res)
