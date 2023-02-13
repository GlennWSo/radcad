use pyo3::prelude::*;

#[pyfunction]
pub fn add_one(x: i32) -> PyResult<i32> {
    Ok(x + 1)
}

#[pymodule]
fn radd_one(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_one, m)?)?;
    Ok(())
}
