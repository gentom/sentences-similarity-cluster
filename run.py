# -*- coding: utf-8 -*-
import sys
from sensim_cluster.sensim_cluster import SensimCluster
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram

cluster = SensimCluster(sys.argv[1])
ids = cluster.get_ids()
result = cluster.ward()
mod_ids = [id[-6:] for id in ids]
r = dendrogram(result, p=100, truncate_mode='lastp', labels=mod_ids, leaf_rotation=90)
print(r['leaves'])
print(r['ivl'])
plt.ylim(ymin=-10.0)
plt.show()