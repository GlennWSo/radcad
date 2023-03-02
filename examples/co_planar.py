from warnings import warn


from rscad.boolean.polydata import diff, common, union
import pyvista as pv

co_planar_buggs = """
    co planar inputs are not yet supported
    if the input meshes are co_coplaner expect buggs!
"""

warn(co_planar_buggs)

cube1 = pv.Cube((0.5, 0.5, 0.5), x_length=5.0, y_length=1.0, z_length=1.0)
cube2 = pv.Cube((1.0, 1.0, 1.0), x_length=2.0, y_length=2.0, z_length=2.0)

p = pv.Plotter()
p.add_mesh(cube1, color="blue", opacity=0.5)
p.add_mesh(cube2, color="green", opacity=0.5)
p.show_axes()
p.show()

diff(cube2, cube1).plot(text="diff", color="yellow")
