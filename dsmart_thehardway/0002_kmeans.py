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
sheet["OfferInformation"].set_index([range(1,33)])

sheet["Matrix"] = pd.concat([sheet["OfferInformation"], sheet["Pivot"]], axis=1)
