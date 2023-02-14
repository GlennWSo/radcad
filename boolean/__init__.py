from .rboolean import pyintersect
import numpy as np


def poly2mesh(poly):
    poly = poly.triangulate()
    points = poly.points
    faces = poly.faces.reshape((-1, 4))[:, 1:]
    return points, faces


def mesh2poly(mesh):
    faces = np.array(mesh[1])
    polys = np.hstack((np.full((faces.shape[0], 1), 3), faces)).ravel()
    return pv.PolyData(mesh[0], polys)


def intersect_poly(poly1, poly2, flip1: bool, flip2: bool):
    m1 = poly2mesh(poly1)
    m2 = poly2mesh(poly2)
    res = pyintersect(m1, m2, flip1, flip2)
    return mesh2poly(res)
