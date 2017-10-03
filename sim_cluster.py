#!/usr/bin/env python
# -*- coding: utf-8 -*-

from levenshteinDistance import editDistance
from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt 
import sys


def HierarchicalCluster(datafile):
    list = []
    sim_matrix = []
    data_list = [line.rstrip('\n') for line in open(datafile)]
    data_list = [line.split(",") for line in data_list]
    print(data_list)
    len_list = len(data_list)
    label_list = [data_list[l][0] for l in range(0,len(data_list))]
    text_list = [data_list[l][1] for l in range(0,len(data_list))]
    print(label_list)
    print(text_list)

    for i in range(0, len_list):
        pivot = text_list[i]
        for j in range(0, len_list):
            sim = editDistance(pivot, text_list[j]) # calcurate similarity(distance)
            print('n{}, n{} : {}'.format(i, j, sim))
            list.append(sim)
            if j == len_list-1:
                sim_matrix.append(list)
                list = []
                
    print('-------------------------')
    print('matrix: {}'.format(sim_matrix))
    linkage_matrix = ward(sim_matrix)
    print('--------------------------')
    print(linkage_matrix)
    dendrogram(linkage_matrix, labels=label_list)
    plt.show()
    
HierarchicalCluster(sys.argv[1])