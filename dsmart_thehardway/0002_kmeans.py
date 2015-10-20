import pandas as pd

wine_kmc = pd.ExcelFile("data/WineKMC.xlsx")
sheet = {}
sheet["Transactions"] = wine_kmc.parse("Transactions")
sheet["Pivot"] = pd.pivot_table(sheet["Transactions"],
                                columns=["Customer Last Name"],
                                index=["Offer #"],
                                aggfunc=len).fillna(" ")
sheet["Matrix"] = pd.concat([wine_kmc.parse("OfferInformation"), sheet["Pivot"]], axis=1)
