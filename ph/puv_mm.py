import numpy as np
import pandas as pd
import matplotlib

import os

rizal_area = "Binangonan|Cainta|Taytay|Antipolo|Angono|Tanay"

file_path = os.path.join(os.path.dirname(__file__), "data/routespuvmm.csv")

ncr_routes_data = pd.read_csv(file_path)

def routes_by_area(cond_area):
    return ncr_routes_data[ncr_routes_data["route"].str.contains(cond_area)].groupby("puv")

print "Rizal"
print routes_by_area(rizal_area).count()

# seperate origins and destination into their own columns

ncr_routes_data["origin"] = pd.Series(
                                ncr_routes_data["route"].str.split(" - ").str[0],
                                index=ncr_routes_data.index)

ncr_routes_data["destination"] = pd.Series(
                                ncr_routes_data["route"].str.split(" - ").str[1],
                                index=ncr_routes_data.index)
