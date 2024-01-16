# Overview 
* This repo is a quick explore of how to refactor code from python to Rust to explore the capability.
* In this repo there is an example of how to load a simple 1.2m JSON file with python and then how to move code to Rust and provide python binding.
* Overview of repo structure:
   * py_rust_explore - contains python code
   * src - contains rust code



# Benchmarking:
Run using Macbook (2.6 GHz 6-Core Intel Core i7 / 32gb RAM)

## JSON load example:
* 1.2m record JSON:
    * Pure python ~3.2 secs
    * Rust in python: 0.000011 secs

## Fibonacci example when n=45:
  * Pure python 5mins 30 secs
  * Rust in python: 4 secs


# Notes:
* Install maturin which build and publish crates with pyo3 so Rust code can run in python: `pip install maturin`.
* Above directory/file structure is recommended by maturin project to avoid import issues
* Once rust dev is complete you need to build code using: `maturin develop`, this will create necessary rust->py code/bindings
* Rust code shouldn't have main.rs or main().  Instead code should be placed in lib.rs file. 


# To-do's:
* Implement decorator for time functions in main.py & remove duplicate code.
