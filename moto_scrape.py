from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime

path = "/Users/jonasmiosga/Desktop/motorcycle_analysis/mo_re_01092020.txt"

with open(path) as f:
    soup = BeautifulSoup(f.read(),features="lxml")

# find info about new bike or first registration with date and mileage (in km)
a = soup.find_all("div", class_="rbt-regMilPow")
# find prices
b = soup.find_all("span", class_="h3 u-block")

# first registration
ez = []
for i in range(0,len(a)):
    if a[i].get_text()[0:3] == "Neu":
        ez.append(0)
    else:
        c = re.search(r"\d{2}(\D)\d{4}",a[i].get_text())
        age = datetime.today() - datetime.strptime(c.group(0),'%m/%Y')
        ez.append(age.days)
ez = [int(i) for i in ez]

# mileage in km
km = []
for i in range(0,len(a)):
    if a[i].get_text()[0:3] == "Neu":
        km.append("0")
    else:
        c = re.search(r"\,\s(.*)\skm",a[i].get_text())
        km.append(c.group(1))
km = [i.replace(".","") for i in km]
km = [int(i) for i in km]

# clean prices
price = []
for i in range(0,len(b)):
    c = b[i].get_text()[0:5]
    price.append(int(c[0]+c[2:5]))

df = pd.DataFrame({'ez': ez, 'price': price, 'km': km})

# ols
X = np.column_stack([ez,km])
reg = LinearRegression().fit(X, price)
print(reg.score(X,price))
