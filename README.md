# humanness_evaluation

This repository contains code needed to reproduce the main experiments from
Parkinson et al. 2024 for humanness evaluation.

### Installation

This repo makes use of AntPack v0.1.0, which requires numpy, scipy,
Biopython and pybind11. A variety of other dependencies are
required to run the notebooks that generate experimental results.
To install, first, clone this repository, then 
activate a virtual environment. From the command line, run:

```
pip install -r requirements.txt
```

Next, to retrieve the test dataset, run the ```data_retrieval.py```
script from the command line. If all goes well, you should see
a "data" folder containing subdirectories with training and test
data. The test data is used by the files under notebooks.

### Antibody sequence numbering

To reproduce experiments associated with the antibody sequence
numbering tool in AntPack v0.1.0, see the notebooks folder and
under it the ``sequence_numbering`` directory.


### Sequence humanization

To repeat the experiments associated with humanness evaluation,
run the notebooks under ```notebooks/sequence_humanization```.
We use results from Prihoda et al. obtained from for comparator
humanization results.


### Sequence humanness scoring

To reproduce results of scoring held-out test data, run
the notebooks under ``notebooks/sequence_scoring``.
