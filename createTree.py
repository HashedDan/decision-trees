from __future__ import print_function

import os
import subprocess
import pydotplus
import graphviz

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_graphviz

def get_data():
    if os.path.exists("NYCSchools.xlsx"):
        print("-- data found locally")
        df = pd.read_excel("NYCSchools.xlsx", index_col=0)
    else :
    	print("-- unable to find file")

    return df



df = get_data()

df = df.fillna('')

print("* df.head()", df.head(), sep="\n", end="\n\n")
print("* df.tail()", df.tail(), sep="\n", end="\n\n")

y = df['Total Grads - % of cohort']
x = df[['asian_per', 'total_enrollment','grade12']]


dt = DecisionTreeRegressor()
dt.fit(x, y)

features = list(x)
print(features)

with open("NYCSchools.dot", 'w') as f:
    export_graphviz(dt, out_file=f, feature_names=features)

command = ["dot", "-Tpng", "NYCSchools.dot", "-o", "NYCSchools.png"]

subprocess.check_call(command)