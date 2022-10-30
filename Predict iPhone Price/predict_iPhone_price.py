import pandas
#import matplotlib.pyplot as plt
#print(data.head())

#plt.barh(data['version'], data['price']) # x axis -> version, y axis -> price
#plt.show()

from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')

model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[20]]))
print(model.predict([[30]]))

