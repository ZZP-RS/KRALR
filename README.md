# KRALR

This is the code for the paper:
>Zhipeng Zhang, Yuhang Zhang, Tianyang Hao, Zuoqing Li, Yao Zhang, Masahiro Inuiguchi. Unearthing undiscovered interests: knowledge enhanced representation aggregation for long-tail recommendation[C]. Proceedings of the 10th International Conference on Integrated Uncertainty in Knowledge Modelling and Decision Making(IUKM), pp.91-103, Kanazawa, Japan, November 2-4, 2023. https://doi.org/10.1007/978-3-031-46781-3_9.
In this paper, we only utilized Last-FM to evaluate our proposed approach.
>
Also for the speical issue of IUKM2023 in Annals of Operations Research:
>KRALR: knowledge enhanced representation aggregation for long-tail recommendation[J]. Annals of Operations Research, Under Review.


## 1. Introduction
KRALR can recommend long-tail items to users as many as possible while maintaining the recommendation accuracy. Firstly, KRALR utilizes a user long-tail interests representation aggregation to capture the long-tail interests of the target users by employing random walks on knowledge graph under item popularity constraints.
Next, KRALR employs a long-tail item representation aggregation to enhance the representation quality of long-tail items by constructing a co-occurence graph and integrating it with knowledge graph. Finally, KRALR calculate the prediction scores for non-interacted items and recommend top $N$ with highest prediction scores for target users.


## 2. Environment Requirement
```
The code has been tested running under Python 3.7.10. The required packages are as follows:
* torch == 1.8.0
* numpy == 1.23.5
* pandas == 1.5.3
* scipy == 1.10.1
* tqdm == 4.65.0
* scikit-learn == 1.2.2
```

## 3. KRALR operation steps
```
1. run Neighbors_Sample.py to generate Long-tail Neighbors
2. run doCooccur.py to construct Co-occurrence graph and merge Co-occurrence graph and KG
3. Run code 'python main_KRALR.py' to start KRALR
```

## 4. Ablation study
### 4.1 Base
1. Replace the training set from trainCKG.txt to train.txt (set on line 21 of the data_loader.py),and trainCKG.txt is generated by Neighbors_ Sample.py, please do not replace data_ Line 22 of the loader.py file, which is used to calculate evaluation metrics
2. Replace the knowledge graph file from kg_ Replace final2.txt to kg_ Final.txt(set on line 24 of the data_loader.py), and final2.txt is generated by doCooccur.py
3. Run code 'python main_KRALR.py' to start Base

### 4.2 KRALR-URA
1. Replace the knowledge graph file from kg_ Replace final2.txt to kg_ Final.txt(set on line 24 of the data_loader.py)
2. Run code 'python main_KRALR.py' to start KRALR-URA

### 4.3 KRALR-IRA
1. Replace the training set from trainCKG.txt to train.txt (set on line 21 of the data_loader.py)
2. Run code 'python main_KRALR.py' to start KRALR-IRA



## 5. datasets
We provided two datasets to validate KRALR: last-fm and ml-1m. 

In the Last.fm dataset, we provide a pretrain file, which can be utilized by setting --use_pretrain 1. Additionally, you have the option to employ your own pretrain file by modifying the load_pretrained_data function in the data_loader.py file.

The following table shows the interaction information of last-fm  and ml-1m :


|  Interaction Datasets   |    last-fm     |  ml-1m  |
|  :---------------:   |:--------------:|:-------:|
|       #users        |     23566      |  6040   |
|       #items        |     48123      |  3655   |
|    #interactions    |    3034796     | 997579  |

 Besides the user-item interactions, we need to construct item knowledge for each dataset. For last-fm, we mapped items to Microsoft Satori entities. For ml-1m, we employed Freebase to map movies in MovieLens1M to construct KG.
The following table shows the KG information of last-fm  and ml-1m :

| Knowledge Graph |   Microsoft Satori (last-fm)   |  Freebase(ml-1m)  |
|:---------------:|          :-----------:         |     :-------:     |
|   #entities    |              58266            |       398505      |
|   #relations   |                 9              |         57        |
|    #triples    |              464567            |       3396595     |



