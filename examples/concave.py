import numpy as np
import pyvista as pv


from rscad.concave.rconcave import concave_hull


randp = np.random.rand(10, 2)


def pad(arr):
    return np.pad(arr, ((0, 0), (0, 1)))


rand_mesh = pv.PolyData(pad(randp))
rand_mesh.plot()

concave_points = concave_hull(randp, 2.0)
n = len(concave_points)

lines = [n] + [i for i in range(n)]
print(concave_points[0], concave_points[-1])

con_mesh = pv.PolyData(pad(concave_points), lines)
con_mesh.plot()
