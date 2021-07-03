import csv
import plotly_express as px
import pandas as pd
import math

with open("classA.csv",newline="") as f:
    reader = csv.reader(f)
    data = list(reader)
    data.pop(0)
# print(data)

marks = []
total = 0
count = 0
for item in data:
    num = float(item[1])
    marks.append(num)
    total = total + num
    count = count + 1

average = total / count
print(average)

df = pd.read_csv("classA.csv")

fig = px.scatter(df,x="Student Number", y="Marks")

fig.update_layout(shapes=[
    dict(type="line",x0=0,y0=average,x1=count,y1=average)
])

fig.show()

sdtotal = 0

for mark in marks:
    m = mark - average
    m2 = m*m
    sdtotal = sdtotal + m2

sdtotal = sdtotal / count 
sd = math.sqrt(sdtotal)
print(sd)
