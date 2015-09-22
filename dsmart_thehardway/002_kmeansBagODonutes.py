# from numpy import genfromtxt
# 
# order_information = genfromtxt("data/OrderInformation.csv", delimiter=",")

# use pandas for data frame
import pandas as pd

order_information = pd.read_csv("data/OrderInformation.csv", sep=",")
transactions = pd.read_csv("data/Transactions.csv", sep=",")
