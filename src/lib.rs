use pyo3::prelude::*;
#[derive(Debug, serde::Deserialize)]

struct Data {
 name: String,
 value: i32,
}

#[pyfunction]
fn sum(input: &str) -> i32 {
 let parsed: Data = serde_json::from_str(input).unwrap();
 parsed.name.len() as i32 + parsed.value
}



#[pyfunction]
fn fibonacci(n: i32) -> u64 {
    if n < 0 {
        panic!("{} is negative!", n);
    }
    match n {
        0 => panic!("zero is not a right argument to fibonacci_reccursive()!"),
        1 | 2 => 1,
        3 => 2,
        /*
        50    => 12586269025,
        */
        _ => fibonacci(n - 1) + fibonacci(n - 2),
    }
}



#[pymodule]
fn rust_json(_py: Python, m: &PyModule) -> PyResult<()> {
 m.add_function(wrap_pyfunction!(sum, m)?)?;
 m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
 Ok(())
}
