import pandas as pd
import quandl
import math, datetime 
import numpy as np
from sklearn import preprocessing, svm, model_selection
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

# Fetching data from Quandl
df = quandl.get('WIKI/GOOGL')

# Selecting relevant features
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# Creating the final dataframe
df = df[['Adj. Close', 'HL_PCT','PCT_change','Adj. Volume']]

# Setting up the forecast column
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

# Defining the forecast period
forecast_out = int(math.ceil(0.1*len(df)))



# Creating the label column
df['label'] = df[forecast_col].shift(-forecast_out)

# Creating feature set (X) and label set (y)
x = np.array(df.drop(['label'], axis=1))


# Scaling the features
x = preprocessing.scale(x)
x_lately = x[-forecast_out:]
x = x[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])


x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

clf = LinearRegression(n_jobs=10)
clf.fit(x_train, y_train)
# Save the classifier
with open('linearregression.pickle','wb') as f:
    pickle.dump(clf, f)

pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(x_test, y_test)
#print(accuracy)

forecast_set = clf.predict(x_lately)

print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
                         
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()                         