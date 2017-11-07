from __future__ import print_function

import os
import subprocess
import pydotplus
import graphviz

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_graphviz

def get_data():
    if os.path.exists("STLParcel.xlsx"):
        print("-- data found locally")
        df = pd.read_excel("STLParcel.xlsx", index_col=0)
    else :
    	print("-- unable to find file")

    return df

def encode_target(df, target_column, new_name):
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod[new_name] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)


df = get_data()

df = df.fillna('')

# print("* df.head()", df.head(), sep="\n", end="\n\n")
# print("* df.tail()", df.tail(), sep="\n", end="\n\n")




df2, targets1 = encode_target(df, '21 Graffiti?', 'GCoded')

print("* df2.head()", df2[["GCoded", '21 Graffiti?']].head(),
      sep="\n", end="\n\n")
print("* df2.tail()", df2[["GCoded", '21 Graffiti?']].tail(),
      sep="\n", end="\n\n")
print("* targets", targets1, sep="\n", end="\n\n")

y = df2['GCoded']

df2, targets1 = encode_target(df2, '22 Unsheltered Person(s) Use of Site?', 'UCoded')

print("* df2.head()", df2[["UCoded", '22 Unsheltered Person(s) Use of Site?']].head(),
      sep="\n", end="\n\n")
print("* df2.tail()", df2[["UCoded", '22 Unsheltered Person(s) Use of Site?']].tail(),
      sep="\n", end="\n\n")
print("* targets", targets1, sep="\n", end="\n\n")

df2, targets1 = encode_target(df2, '23 Number of Trees', 'TCoded')

print("* df2.head()", df2[["TCoded", '23 Number of Trees']].head(),
      sep="\n", end="\n\n")
print("* df2.tail()", df2[["TCoded", '23 Number of Trees']].tail(),
      sep="\n", end="\n\n")
print("* targets", targets1, sep="\n", end="\n\n")


x = df2[['UCoded', 'TCoded']]

dt = DecisionTreeRegressor()
dt.fit(x, y)

features = list(x)
print(features)

with open("STLParcel.dot", 'w') as f:
    export_graphviz(dt, out_file=f, feature_names=features)

command = ["dot", "-Tpng", "STLParcel.dot", "-o", "STLParcel.png"]

subprocess.check_call(command)