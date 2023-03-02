from time import time


import pyvista as pv
import numpy as np
from rscad.boolean.polydata import diff


def add_pothole():
    t0 = time()
    street_mesh = pv.Plane(
        i_size=100, j_size=100, i_resolution=100, j_resolution=100
    ).triangulate()
    street_mesh.flip_normals()

    points = np.array(
        [
            [20, 30, 0],
            [50, 50, 0],
            [60, 30, 0],
            [20, 60, 0],
        ]
    ) - (50, 50, 0)
    for i in range(4):
        res = 40
        pothole_mesh = pv.ParametricEllipsoid(
            10, 5, 3, clean=True, u_res=res, v_res=res, w_res=res
        ).compute_normals(flip_normals=True)

        # ensure normals look normal ;) i.e thay are consistent and pointing outwards
        # pothole_mesh.plot_normals()

        # alternatively to get the half ellipsoid: (but boolean difference seemed to only work with the closed one
        # pothole_mesh = pv.ParametricEllipsoid(10,5,3, max_v=pi /2)
        pothole_mesh.translate(points[i], inplace=True)

        # "add" the pothole to the street
        street_mesh = diff(street_mesh, pothole_mesh)
        # street_mesh = street_mesh.boolean_difference(pothole_mesh)

    t = time() - t0
    print(f"time: {t} s")
    street_mesh.plot()


if __name__ == "__main__":
    add_pothole()
