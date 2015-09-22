import pandas as pd

df = pd.DataFrame.from_csv("data/Concessions.csv")

actual_profit = sum(df['Actual Profit'].str.replace(r'[$]','').astype('float').tolist())

