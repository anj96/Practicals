import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


iris = datasets.load_iris()

x = pd.DataFrame(iris.data)
x.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']

y = pd.DataFrame(iris.target)
y.columns = ['Targets']


colormap = np.array(['red', 'lime', 'black'])

plt.subplot(221)
plt.scatter(x.Sepal_Length, x.Sepal_Width, c=colormap[y.Targets], s=100)
plt.title('Sepal')

plt.subplot(222)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=100)
plt.title('Petal')


model = KMeans(n_clusters=3)
model.fit(x)


colormap = np.array(['red', 'lime', 'black'])

plt.subplot(223)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=100)
plt.title('Real Classification')

plt.subplot(224)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[model.labels_], s=100)
plt.title('K Mean Classification')
plt.show()
