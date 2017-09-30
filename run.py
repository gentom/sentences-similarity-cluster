#!/usr/bin/env python
# -*- coding: utf-8 -*-

from levenshteinDistance import editDistance

def main(datafile):
    list = []
    data_list = [line.rstrip('\n') for line in open(datafile)] # ファイルから一行ずつ読み込み、リストにinsert
    #print(data_list)
    
    for i in range(0, len(data_list)):
        pivot = data_list[i]
        for j in range(0, len(data_list)):
            ret = editDistance(pivot, data_list[j])
            print('n{}, n{} : {}'.format(i, j, ret))
            list.append(ret)
    print('Result: {}'.format(list))

main('./dataset/dummydata.csv')