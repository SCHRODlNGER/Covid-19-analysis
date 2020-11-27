import datatable as dt
import pandas as pd
import json
from pathlib import Path
from pprint import pprint
import os

base_path = Path("./dataset")
print(os.listdir(base_path))

with open(base_path/"states_lat_long.json") as f:
    st_m = json.load(f)

lat_m = {}
long_m = {}
for i in st_m:
    lat_m[i["state"]] = i["latitude"]
    long_m[i["state"]] = i["longitude"]

df = dt.fread(base_path/"modified_usa.csv").to_pandas()

states = lat_m.keys()
df = df[df["State"].isin(states)]

df["lat"] = df["State"].map(lat_m)
df["long"] = df["State"].map(long_m)

print("Added Latitudes and Longitudes to dataset")
df.drop(["Admin"], axis = 1, inplace = True)
df.to_csv(base_path/"modified_usa.csv", index = False)
print("Saved Dataset")