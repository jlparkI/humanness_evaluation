import pandas as pd
import os

template = pd.read_csv("heavy_abnativ_camel.txt")

for f in os.listdir():
    if ".py" in f:
        continue
    raw = pd.read_csv(f)
    raw = raw.iloc[:,4:8]
    raw.to_csv(f, index=False)
