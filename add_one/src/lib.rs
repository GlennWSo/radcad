use pyo3::prelude::*;

pub fn increment(x: i32) -> i32 {
    x + 1
}

#[pyfunction]
pub fn add_one(x: i32) -> PyResult<i32> {
    Ok(increment(x))
}

#[pymodule]
fn radd_one(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_one, m)?)?;
    Ok(())
}
