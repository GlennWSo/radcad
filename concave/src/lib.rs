use geo::{ConcaveHull, MultiPoint};

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

type Points = Vec<[f64; 3]>;

#[pyfunction]
fn concave_hull(points: Points, concavity: f64 ) -> PyResult<Points> {
    let points: MultiPoint<f64>= points.into()

    hull = points.concave_hull(concavity)
    hull.exterior().0
}


#[pymodule]
fn rconcave(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(concave_hull, m)?)?;
    Ok(())
}
