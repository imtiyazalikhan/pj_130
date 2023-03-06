import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Luminosit"]
del df[""]
del df["mass"]
del df["Distance"]
del df["radius"]

df.to_csv('main.csv')