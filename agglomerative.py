import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset
dataset = pd.read_csv('product_ratings.csv')
x = dataset.iloc[:, [2, 3]].values

# using the dendrogram to find the optimal no. of clusters
import scipy.cluster.hierarchy as sch

dendrogram = sch.dendrogram(sch.linkage(x, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Product')
plt.ylabel('Euclidean distances')
plt.show()

# fitting Hierarchical clustering to the dataset
from sklearn.cluster import AgglomerativeClustering, KMeans

hc = AgglomerativeClustering(n_clusters=None,compute_full_tree=True, affinity='euclidean', linkage='ward',
                             distance_threshold=80000)
km = KMeans(n_clusters=10, init='k-means++')
y_km=km.fit_predict(x)
list_of_labels_kmeans=list(y_km)

y_hc = hc.fit_predict(x)
list_of_labels_agglomerative=list(y_hc)

print(y_hc)
print(y_km)
print('agglomerative:')
list_of_labels_agglomerative.sort()
hc_dict={i:list_of_labels_agglomerative.count(i) for i in list_of_labels_agglomerative}
print(hc_dict)
print('k means:')
list_of_labels_kmeans.sort()
km_dict={i:list_of_labels_kmeans.count(i) for i in list_of_labels_kmeans}
print(km_dict)
