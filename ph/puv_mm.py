import os
import numpy as np
import pandas as pd
import matplotlib

import data as phdata

rizal_area = "Binangonan|Cainta|Taytay|Antipolo|Angono|Tanay"

ncr_routes_data = phdata.ncr_routes_data

def routes_by_area(cond_area):
    return ncr_routes_data[ncr_routes_data["route"].str.contains(cond_area)].groupby("puv")

print "Rizal"
print routes_by_area(rizal_area).count()

# seperate origins and destination into their own columns

def by_endpoint(df, col='route', idx=0, splt=' - '):
    return pd.Series(df[col].str.split(splt).str[idx], index=df.index)
    
ncr_routes_data["origin"] = by_endpoint(ncr_routes_data, idx=0)
ncr_routes_data["destination"] = by_endpoint(ncr_routes_data, idx=1)

# filter paths
passage = pd.DataFrame()
passage['pair']  = ncr_routes_data['destination'].str.split(' via ')
