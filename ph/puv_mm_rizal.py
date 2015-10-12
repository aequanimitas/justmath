import pandas as pd

rizal_area = "Binangonan|Cainta|Taytay|Antipolo|Angono|Tanay"

rizal_routes = pd.read_csv("data/routespublicutilityvehiclesmetromanila.csv")

def routes_by_area(cond_area):
    return rizal_routes[rizal_routes["route"].str.contains(cond_area)].groupby("puv")

print routes_by_area(rizal_area).count()
