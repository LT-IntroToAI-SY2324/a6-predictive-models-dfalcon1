import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

x, y = datasets.load_diabetes(return_X_y=True)
x = x[:,np.neaxis, 2]
print(x)
print(y)

print(coef, intercept)

prediction = model.predict(xtest)







