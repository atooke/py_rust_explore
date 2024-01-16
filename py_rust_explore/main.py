import sys
import json
from datetime import datetime
import sys
from rust_json import sum as rust_sum
from rust_json import fibonacci as rust_fibonacci


def get_time():
    # TODO - make decorator to cutdown on code
    """helper to func"""
    return datetime.now()


def py_sum(file):
    """python implementation of summing the value from JSON"""
    s = 0
    for line in file :
        value = json.loads(line)
        s += value['value']
        s += len(value['name'])
    return s


def py_fibonacci(n=10):
    """python implementation of calculating Fibonacci for a given number"""
    # Check if input is >0 
    if n < 0:
        print("Incorrect input")
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
    else:
        return py_fibonacci(n-1) + py_fibonacci(n-2)


def run_fibbonaci_example(n=45):
    """Example of running Fibbonaci calculation via python & python with Rust backend """
    print(f"Running Fibonacci example for n={n}:")
    t = get_time()
    res = py_fibonacci(n)
    dur = get_time()-t
    print(f"\tDuration using standard python time to execute : {dur}, result:{res}")
    # now run in Rust:
    t2 = get_time()
    res2 = rust_fibonacci(n)
    dur2 = get_time()-t2
    print(f"\tDuration using python/rust time to execute: {dur2}, result:{res2}")


def run_json_example():
    print("Running loading JSON file example:")
    t = get_time()
    s = 0
    for line in sys.stdin:
        value = json.loads(line)
        s += value['value']
        s += len(value['name'])
    dur = datetime.now()-t
    print(f"\tDuration loading JSON file via Standard Python: {dur}")
    t2 = get_time()
    s = 0
    for line in sys.stdin:
        s += rust_sum(line)
    dur2 = datetime.now()-t2
    print(f"\tDuration loading JSON file via Python/Rust: {dur2}" )


def main():
    run_fibbonaci_example()
    run_json_example()


if __name__ == "__main__":
    main()
