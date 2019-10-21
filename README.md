# MinCov
MinCov is a Python implementation of a decision procedure for the Petri net coverability set problem 

## Installation

MinCov does not require any installation. However, [Python 3.7](https://www.python.org/download/releases/2.7/) must be installed with the following additional packages:

* [NumPy](http://www.numpy.org/) ≥1.16.4 (e.g. on Debian-based Linux distributions: `sudo apt-get install python-numpy`),
* [SciPy](https://www.scipy.org/) ≥0.13.3 (e.g. on Debian-based Linux distributions: `sudo apt-get install python-scipy`),
* [Z3](https://github.com/Z3Prover/) ≥4.4.0: follow installation instructions for Python bindings.

## Usage
MinCov is executed by runinng the scrip "./benchmarks/run_all_benchmarks" which runs all the benchmarks in the folder "benchmarks" and produses an output ".csv" output summarising the run. 

## Input file format

MinCov supports a *strict subset of* the `.spec` format from [mist](https://github.com/pierreganty/mist) described [here](https://github.com/pierreganty/mist/wiki#input-format-of-mist). QCover loads `.spec` files as Petri nets. 

## Questions

For any question concerning MinCov, contact [Igor Khmelnitsky](http://www.lsv.fr/~khmelnitsky/).


