import pandas as pd
import numpy as np

wine_kmc = pd.ExcelFile("data/WineKMC.xlsx")
sheet = {}
sheet["Transactions"] = wine_kmc.parse("Transactions")
sheet["Pivot"] = pd.pivot_table(sheet["Transactions"],
                                columns=["Customer Last Name"],
                                index=["Offer #"],
                                aggfunc=len).fillna(0)
# adjust index, defaults to 0
sheet["OfferInformation"] = wine_kmc.parse("OfferInformation")

sheet["Matrix"] = pd.concat([sheet["OfferInformation"].set_index([range(1,33)]), 
                             sheet["Pivot"]], axis=1)
sheet["4MC"] = sheet["OfferInformation"]

# add the 4 cluster columns
for _, v in enumerate(range(1,5)):
    sheet["4MC"]["Cluster {}".format(v)] = pd.Series(0, index=sheet["Matrix"].index)

dtc_initvals = np.array([sheet["Pivot"].apply(np.sum).apply(np.sqrt) for x in range(1,5)])
dtc_indexes = ["Distance from Cluster {}".format(x) for x in range(1,5)]
sheet["Distance to Cluster"] = pd.DataFrame(dtc_initvals, index=dtc_indexes, columns=sheet["Pivot"].columns)
