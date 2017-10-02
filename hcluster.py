#!/usr/bin/env python
# -*- coding: utf-8 -*-

from levenshteinDistance import editDistance
from scipy.cluster.hierarchy import ward, dendrogram, linkage
import matplotlib.pyplot as plt 


def main(datafile):
    list = []
    ret_list = []
    data_list = [line.rstrip('\n') for line in open(datafile)]
    len_list = len(data_list)
    for i in range(0, len(data_list)):
        pivot = data_list[i]
        for j in range(0, len_list):
            ret = editDistance(pivot, data_list[j])
            print('n{}, n{} : {}'.format(i, j, ret))
            list.append(ret)
            if j == len_list-1:
                ret_list.append(list)
                list = []
    print('-------------------------')
    print('matrix: {}'.format(ret_list))
    return ret_list

dist = main('./dataset/dummydata.csv')
linkage_matrix = ward(dist)
print(linkage_matrix)
dendrogram(linkage_matrix)
plt.show()