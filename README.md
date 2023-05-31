# KRALR

## Environment Requirement
The code has been tested running under Python 3.7.10. The required packages are as follows:
* torch == 1.8.0
* numpy == 1.23.5
* pandas == 1.5.3
* scipy == 1.10.1
* tqdm == 4.65.0
* scikit-learn == 1.2.2

## KRALR operation steps

1. run Neighbors_Sample.py to generate Long-tail Neighbors
2. run doCooccur.py to construct Co-occurrence graph and merge Co-occurrence graph and KG
3. Run code 'python main_KRALR.py' to start KRALR