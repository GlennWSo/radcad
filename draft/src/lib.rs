extern crate nalgebra as na;
use na::{DVector, Vector3, OMatrix, Dyn, U3};

use pyo3::prelude::*;


type _Normal = Vector3<f64>;
/// used to represent angle in radians
type _Normals = OMatrix<f64, Dyn, U3>;
type _Angles = DVector<f64>;


/// normals: Vec[r=n, c=3]
/// normal: Vec[r=3]

 fn _normals2angles(normals: _Normals, ref_normal: _Normal) -> _Angles{
    let product = normals * ref_normal;
    product.map(|e| e.acos())
}


type Normal = [f64; 3];
/// used to represent angle in radians
type Normals = Vec<Normal>;
type Angles = Vec<f64>;

#[pymodule]
fn rdraft(_py: Python, m: &PyModule) -> PyResult<()> {
    /// Finds the concave path around the points, the concavity factor controlls how concave/jagged the result is.
    /// concavity=0 -> the uncomprimising concave path. 
    /// concavity=big num -> the convex path
    ///
    /// # args: 
    /// normals: Vec[r=n, c=3]
    /// normal: Vec[r=3]
    ///
    /// returns angles: Vec[r=n]
    #[pyfn(m)]
    #[pyo3(text_signature = "(points, concavity, /)")]
    fn normals2angles(normals: Normals, ref_normal: Normal) -> PyResult<Angles> {
        let _normals = _Normals::from_fn(normals.len(), |r, c| normals[r][c]);
        let _ref_normal = _Normal::from_row_slice(&ref_normal);
        let res = _normals2angles(_normals, _ref_normal);
        Ok(res.data.into())
    }

    Ok(())
}