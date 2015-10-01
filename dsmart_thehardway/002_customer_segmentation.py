import pandas as pd

# I didn't know that you can read xls files directly
df_offers = pd.read_excel("./data/WineKMC.xlsx", sheetname=0)

# change the column names
df_offers.columns = ["offer_id", "campaign", "varietal", "min_qty", 
                     "discount", "origin", "past_peak"]

# now the transactions sheet
df_transactions = pd.read_excel("./data/WineKMC.xlsx", sheetname=1)

# change again the column names
df_transactions.columns = ["customer_name", "offer_id"]

# I don't know the purpose of this one other than it just added a column labelled "n" with
# values set to 1
df_transactions["n"] = 1

# join the two tables
df = pd.merge(df_offers, df_transactions)

# create a pivot table which will give us the number of times each customer responded to a
# given offer
# for each transaction, we log 1 which means a response from our customer
matrix = df.pivot_table(index=["customer_name"], columns=["offer_id"], values="n")

# now clean the NAs
matrix = matrix.fillna(0).reset_index()

# convert index into a column
# matrix = matrix.reset_index()

# save a list of the 0/1 columns
x_cols = matrix[1:]
# 
from sklearn.cluster import KMeans
# 
cluster = KMeans(n_clusters=5)
# 
matrix["cluster"] = cluster.fit_predict(matrix[matrix.columns[2:]])
# matrix.cluster.value_counts()
# 
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
matrix["x"] = pca.fit_transform(matrix[x_cols])[:,0]
