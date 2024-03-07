#code block 1 import libraries 

import pandas as pd
import matplotlib.pyplot as plt

#code block 2, it loads the data. It is a dataframe (like a spreadsheet in Python)
data = pd.read_csv('data.csv')

#code block 3, set up the plot 
plt.figure(figsize=(8,5))
plt.gca().set_aspect('equal', adjustable='box')
#plt.axis('off')

#code block 4, create the bar chart
#each row represent each year that represent each bar
bars = data.shape[0]
barWidth = 800/ bars
barHeight = 500

#for loop that iterates over each row of DataFrame
for i in range(bars):
   x = i*barWidth 
   y = 0
   d = data.iloc[i,1]
   if d > 0:
     col = plt.cm.Reds(d)
   else:  
     col = plt.cm.Blues(-d)
   plt.bar(x, barHeight, width= barWidth, bottom=y, color= col)

plt.show()