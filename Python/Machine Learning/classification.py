import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

#Read dataset from CSV
df = pd.read_csv('breast-cancer-wisconsin.data')
#Make missing data equal to -99999 so it is treated as outlier by ML algorithm
df.replace('?', -99999, inplace=True)
#Drop any data columns that aren't relevant.. like the ID (97% accuracy without it, 50% with it.)
df.drop(['id'], axis=1, inplace=True)


x = np.array(df.drop(['class'], axis=1))
y = np.array(df['class'])

#train model on data
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

#call kneighbors classifier
clf = neighbors.KNeighborsClassifier()
clf.fit(x_train, y_train)

accuracy = clf.score(x_test, y_test)

print(accuracy)

# add an example data point to see how close it is
example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,2,2,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures), -1)
prediction = clf.predict(example_measures)
print(prediction)