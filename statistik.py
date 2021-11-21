import pandas as pd

from tools import *

production_data = pd.read_csv("Electricity_Production_By_Source_Cleansed.csv")

quantitative_data = production_data.loc[(production_data["Year"] == 2019)].loc[:, production_types_semantic("coal"):production_types_semantic("nuclear")]

quantitative_data_2 = quantitative_data

print(quantitative_data)

percentile_list = [0.1, 0.25, 0.5, 0.75, 0.9]

for percentile in percentile_list:
    print(f"Persentil {percentile*100}%")
    print(quantitative_data.quantile(percentile))
    print("\n")

print("Maximum energy production")
print(quantitative_data.max())

print("Minimum energy production")
print(quantitative_data.min())

print("Mean energy production for each sector")
print(quantitative_data.mean())

print("Standard deviation of energy production of each sector")
print(quantitative_data.std())
