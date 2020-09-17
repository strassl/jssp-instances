# Benchmark instances for the JSSP

## Description

The instances in `lit` are existing instances found in the literature as collected by [1].
Refer to http://jobshop.jjvh.nl/ for a list of their sources.

The instances in `gen` are novel instances with uniformly distributed number of jobs, number of machines and processing times drawn from various probability distributions.

## Generator

### Setup

#### With `pipenv`

1. Make sure `pipenv` is installed on your system
2. Run `pipenv sync` to set up the virtual environment and install dependencies
3. Run `pipenv shell` to activate the virtual environment

#### Without `pipenv`

1. Make sure the following requirements are statisfied on your system:
   - `python == 3.7`
   - `numpy == 1.19.2`
   - `scipy == 1.5.2`
2. Run `python main.py` to launch the generator

### Run

Run the generator using

```bash
python main.py --seed SEED --output OUTPUT --prefix PREFIX --instances-per-size INSTANCES_PER_SIZE --duration-distributions DURATION_DISTRIBUTIONS --job-counts JOB_COUNTS --machine-counts MACHINE_COUNTS
```

Where:

- `SEED` is the seed for the random number generators.
- `OUTPUT` is the directory to which the instances shall be written.
- `PREFIX` is the prefix for the generated instance files.
- `INSTANCES_PER_SIZE` is the number of instances to generate for each configuration.
- `DURATION_DISTRIBUTIONS` is a list of duration distributions to use. Can be any subset of `const-1,uniform-1-99,uniform-1-200,binom-0.5-1-99,nbinom-0.5-1`.
- `JOB_COUNTS` is a list of integers defining the number of jobs per instance.
- `MACHINE_COUNTS` is a list of integers defining the number of machines per instance.

## About

This work is part of Strassl, Simon. “Instance Space Analysis for the Job Shop Scheduling Problem.” Master’s Thesis, TU Vienna, 2020.

## References

[1] van Hoorn, Jelke J. “The Current State of Bounds on Benchmark Instances of the Job-Shop Scheduling Problem.” Journal of Scheduling 21, no. 1 (2018): 127–128. https://doi.org/10.1007/s10951-017-0547-8.
