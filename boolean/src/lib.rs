use parry3d_f64::na::{Isometry3, Point3, Vector3};
use parry3d_f64::shape::{Cuboid, TriMesh, TriMeshFlags};
use parry3d_f64::transformation::intersect_meshes_track as intersect_meshes;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

fn prepare_mesh(mesh: &mut TriMesh) {
    let flags = TriMeshFlags::HALF_EDGE_TOPOLOGY | TriMeshFlags::ORIENTED;
    mesh.set_flags(flags).expect("mesh should be manifold");
}

fn brick(b: f64) -> TriMesh {
    let halfb: f64 = b / 2.0;
    let dims = Vector3::new(halfb, halfb, halfb);

    let mut mesh = TriMesh::from(Cuboid::new(dims));
    prepare_mesh(&mut mesh);
    mesh
}

type Points = Vec<[f64; 3]>;
type Faces = Vec<[u32; 3]>;
type Mesh = (Points, Faces);

fn mesh2trimesh(mut m: Mesh) -> TriMesh {
    let points =
        m.0.drain(..)
            .map(|p| Point3::new(p[0], p[1], p[2]))
            .collect();

    let mut tri = TriMesh::new(points, m.1);
    prepare_mesh(&mut tri);
    tri
}

fn trimesh2mesh(trimesh: TriMesh) -> Mesh {
    let points = trimesh
        .vertices()
        .iter()
        .copied()
        .map(|v| [v.x, v.y, v.z])
        .collect();
    let faces = trimesh.indices().clone();
    (points, faces)
}

pub fn intersect(m1: Mesh, m2: Mesh, flip1: bool, flip2: bool) -> Option<(Mesh, Vec<[u32; 3]>)> {
    let origo = Isometry3::identity();
    let m1 = mesh2trimesh(m1);
    let m2 = mesh2trimesh(m2);
    match intersect_meshes(&origo, &m1, flip1, &origo, &m2, flip2) {
        Ok(opval) => match opval {
            Some((tri, inds)) => Some((trimesh2mesh(tri), inds)),
            None => None,
        },
        Err(n) => {
            println!("Error {n}");
            None
        }
    }
}

use pyo3::create_exception;

create_exception!(module, MyError, pyo3::exceptions::PyException);

#[pyfunction]
fn pyintersect(m1: Mesh, m2: Mesh, flip1: bool, flip2: bool) -> PyResult<(Mesh, Vec<[u32; 3]>)> {
    match intersect(m1, m2, flip1, flip2) {
        Some(val) => Ok(val),
        None => Err(MyError::new_err("derp")),
    }
}

#[pyfunction]
fn pycube(b: f64) -> PyResult<Mesh> {
    let c = brick(b);
    Ok(trimesh2mesh(c))
}

#[pymodule]
fn rboolean(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(pycube, m)?)?;
    m.add_function(wrap_pyfunction!(pyintersect, m)?)?;
    Ok(())
}
