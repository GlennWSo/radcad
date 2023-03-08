use geo::{ConcaveHull, MultiPoint};

use pyo3::prelude::*;
// use pyo3::wrap_pyfunction;

type Points = Vec<[f64; 2]>;


#[pymodule]
fn rconcave(_py: Python, m: &PyModule) -> PyResult<()> {
    /// concave_hull(points: Vec[n, 2], concavity: float, /) -> Vec[m, 2]
    /// --
    ///
    /// Finds the concave path around the points, the concavity factor controlls how concave/jagged the result is.
    /// concavity=0 -> the uncomprimising concave path. 
    /// concavity=big num -> the convex path
    #[pyfn(m)]
    fn concave_hull(points: Points, concavity: f64 ) -> PyResult<Points> {
        let m_points: MultiPoint<f64> = points.into();

        let hull = m_points.concave_hull(concavity);
    
        let hull_points = hull.exterior().coords().map(|c| [c.x, c.y]).collect();
        Ok(hull_points)
    }
    Ok(())
}
