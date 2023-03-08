import numpy as np
import pyvista as pv
from rscad.concave.rconcave import concave_hull


def pad(arr):
    return np.pad(arr, ((0, 0), (0, 1)))


def random_concave(factor):

    # generate random points
    randp = np.random.rand(50, 2)
    rand_mesh = pv.PolyData(pad(randp))
    # rand_mesh.plot() #  inspect input

    # find the concave path around the points and create a polygon
    concave_points = concave_hull(randp, factor)
    n = len(concave_points)
    lines = [n] + [i for i in range(n)] + [2, n - 1, 0]
    polygon = pv.PolyData(pad(concave_points), lines=lines)

    # inpect input and result
    p = pv.Plotter()
    p.add_mesh(rand_mesh, color="green")
    p.add_mesh(polygon, color="blue")
    p.show()


if __name__ == "__main__":
    for _ in range(10):
        random_concave(2.0)
