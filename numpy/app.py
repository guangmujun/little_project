import seaborn as sns
import numpy as np

iris = sns.load_dataset('iris')
print(iris.head())

np.savetxt('./data/iris.csv', iris.values[:,:4], fmt='%3.1f,%3.1f,%3.1f,%3.1f', delimiter=',')  # 逗号分隔
data = np.loadtxt('./data/iris.csv',delimiter=',')

print(np.mean(data[:,2:3]))