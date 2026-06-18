from sklearn.linear_model import LinearRegression

X = [[1000,2],[1500,3],[2000,4]]
y = [5500000,8200000,12000000]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[1300,3]])

print(prediction)
