# -*- coding: utf-8 -*-

import codecs
from scipy.cluster.hierarchy import linkage

def levenshtein(s1,s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

class SensimCluster:
    def __init__(self, datafile):
        try:
            f = codecs.open(datafile, "r", "utf-8")
        except OSError:
            print('Cannot open', datafile)
            return

        self.ids = []
        self.data_list = []
        self.data_size = 0
        self.distances = []

        self._f2l(f)
        self.data_size = len(self.data_list)
        self._distance()

    def _f2l(self, f):
        for line in f:
            id, data = line.rstrip('\n\r').split(',', 1)
            self.ids.append(id)
            self.data_list.append(data)

    def _distance(self):
        for i in range(self.data_size - 1):
            for j in range(i+1, self.data_size):
                similarity = levenshtein(self.data_list[i], self.data_list[j])
                self.distances.append(similarity)
    
    def get_ids(self):
        return self.ids
    
    def ward(self):
        return linkage(self.distances, method='ward')