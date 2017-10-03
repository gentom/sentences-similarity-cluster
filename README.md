# similarity-cluster
sim_cluster.py calculates the similarity of text data(from file) using Levenshtein distance and clusters(hierarchical clustering) the result. Clustering results are displayed with dendrogram.  
## Usage
### 1. Prepare your data file 
### 2. Execute  
```
python sim_cluster.py your_file
```
## Example
### 1. Prepare the data file
./dataset/dummydata.csv
```
A,helloworld
B,hallawerld
C,helldwoody
D,hallowarld
E,galloworld
F,herroworld
```
### 2. Execute
```
python sim_cluster.py ./dataset/dummydata.csv
```
### 3. Result
![result](https://github.com/gentom/similarity-cluster/blob/master/img/hclustering_result.png)
```
[['A', 'helloworld'], ['B', 'hallawerld'], ['C', 'helldwoody'], ['D', 'hallowarld'], ['E', 'galloworld'], ['F', 'herroworld']]
['A', 'B', 'C', 'D', 'E', 'F']
['helloworld', 'hallawerld', 'helldwoody', 'hallowarld', 'galloworld', 'herroworld']
n0, n0 : 0
n0, n1 : 3
n0, n2 : 4
n0, n3 : 2
n0, n4 : 2
n0, n5 : 2
n1, n0 : 3
n1, n1 : 0
n1, n2 : 6
n1, n3 : 2
n1, n4 : 3
n1, n5 : 5
n2, n0 : 4
n2, n1 : 6
n2, n2 : 0
n2, n3 : 6
n2, n4 : 6
n2, n5 : 6
n3, n0 : 2
n3, n1 : 2
n3, n2 : 6
n3, n3 : 0
n3, n4 : 2
n3, n5 : 4
n4, n0 : 2
n4, n1 : 3
n4, n2 : 6
n4, n3 : 2
n4, n4 : 0
n4, n5 : 4
n5, n0 : 2
n5, n1 : 5
n5, n2 : 6
n5, n3 : 4
n5, n4 : 4
n5, n5 : 0
-------------------------
matrix: [[0, 3, 4, 2, 2, 2], [3, 0, 6, 2, 3, 5], [4, 6, 0, 6, 6, 6], [2, 2, 6, 0, 2, 4], [2, 3, 6, 2, 0, 4], [2, 5, 6, 4, 4, 0]]
-------------------------
[[  3.           4.           3.           2.        ]
 [  1.           6.           4.2031734    3.        ]
 [  0.           5.           4.89897949   2.        ]
 [  7.           8.           7.57187779   5.        ]
 [  2.           9.          12.05542755   6.        ]]
```