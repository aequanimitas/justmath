import pandas as pd
SKIPPEDROWS = [21,42,63]
df = pd.read_csv("../rondo/0607.csv", skiprows=SKIPPEDROWS)
