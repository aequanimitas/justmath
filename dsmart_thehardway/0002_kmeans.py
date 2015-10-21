import pandas as pd

wine_kmc = pd.ExcelFile("data/WineKMC.xlsx")
sheet = {}
sheet["Transactions"] = wine_kmc.parse("Transactions")
sheet["Pivot"] = pd.pivot_table(sheet["Transactions"],
                                columns=["Customer Last Name"],
                                index=["Offer #"],
                                aggfunc=len).fillna(" ")
# adjust index, defaults to 0
sheet["OfferInformation"] = wine_kmc.parse("OfferInformation")

sheet["Matrix"] = pd.concat([sheet["OfferInformation"].set_index([range(1,33)]), 
                             sheet["Pivot"]], axis=1)
sheet["4MC"] = sheet["OfferInformation"]

# add the 4 cluster columns
for _, v in enumerate(range(1,5)):
    sheet["4MC"]["Cluster {}".format(v)] = pd.Series(0, index=sheet["Matrix"].index)


