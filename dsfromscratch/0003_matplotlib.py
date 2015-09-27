from matplotlib import pyplot as plt

years = range(1950,2020,10)
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color="green", marker="o", linestyle="solid")
 
plt.title("Nominal GDP")

plt.ylabel("Billions of $")
plt.show()
