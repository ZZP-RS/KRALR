# KRALR

This is the code for the paper:
>Zhipeng Zhang, Yuhang Zhang, Tianyang Hao, Zuoqing Li, Yao Zhang, and Masahiro Inuiguchi(2023). Unearthing Undiscovered Interests: Knowledge Enhanced Representation Aggregation for Long-Tail Recommendation. In: Honda, K., Le, B., Huynh, VN., Inuiguchi, M., Kohda, Y. (eds) Integrated Uncertainty in Knowledge Modelling and Decision Making. IUKM 2023. Lecture Notes in Computer Science(), vol 14376. Springer, Cham. https://doi.org/10.1007/978-3-031-46781-3_9


## Introduction
KRALR discovers users' long tail interests through random walks and enhances the quality of long tail items by constructing co-occurrence graphs

If you want to use codes and datasets in your research, please contact the paper authors and cite the following paper as the reference:
```
@inproceedings{KRALR,
  author    = {Zhipeng Zhang and
               Yuhang Zhang and
               Tianyang Hao and
               Zuoqing Li and
               Yao Zhang and
               Masahiro Inuiguchi,
  title     = {Unearthing Undiscovered Interests: Knowledge Enhanced Representation Aggregation for Long-Tail Recommendation},
  booktitle = {{IUKM2023}},
  pages     = {91–-103},
  year      = {2023}
}
```


## Environment Requirement
```
The code has been tested running under Python 3.7.10. The required packages are as follows:
* torch == 1.8.0
* numpy == 1.23.5
* pandas == 1.5.3
* scipy == 1.10.1
* tqdm == 4.65.0
* scikit-learn == 1.2.2
```

## KRALR operation steps
```
1. run Neighbors_Sample.py to generate Long-tail Neighbors
2. run doCooccur.py to construct Co-occurrence graph and merge Co-occurrence graph and KG
3. Run code 'python main_KRALR.py' to start KRALR
```

## datasets
We provided a dataset to validate KRALR: last-fm, which obtained from KGAT,  The following table shows the information of Last-FM dataset:

|                | Last-FM |
| :------------: | :-----: |
|    n_users     |  23566  |
|    n_items     |  48123  |
| n_interactions | 3034796 |
|   n_entities   | 106389  |
|  n_relations   |    9    |
|   n_triples    | 464567  |


