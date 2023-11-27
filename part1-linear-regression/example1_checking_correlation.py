import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# gets the data and sets x and y values
data = pd.read_csv("part1-linear-regression/chirping_data.csv")
print(data)
x = data["Temp"]
y = data["Chirps"]

# sets the size of the graph
plt.figure(figsize=(6,4))

# creates a scatter plot and labels the axes
plt.scatter(x,y)
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure vs Age")

# prints the correlation coefficient
print(f"Correlation between Temperature and Chirps/Min: {x.corr(y)}")

# show the plot
plt.show()