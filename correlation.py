import matplotlib.pyplot as plt
import pandas as pd

from tools import *
import itertools

production_data = pd.read_csv("Electricity_Production_By_Source_Cleansed.csv")
new_data = production_data

group_name_list = {
    "fossil":"Energy From Fossil Fuels (TWH)",
    "renewables":"Energy From Renewables (TWH)",
    "nuclear":"Energy From Nuclear (TWH)",
}
    
grouped_by_year = production_data.groupby("Year").sum()


for production_type in production_types:
    column = [production_types_semantic(production_specific_type) for production_specific_type in production_types[production_type]]
    new_data[group_name_list[production_type]] = new_data[column].sum(axis=1)
    new_data.drop([production_types_semantic(production_type) for production_type in production_types[production_type]], 1, inplace=True)

print(new_data)

production_source_type_combination_list = tuple(itertools.permutations([group_name for group_name in group_name_list], 2))

for production_source_type_combination in production_source_type_combination_list:
    production_source_1, production_source_2 = production_source_type_combination
    correlation = new_data[group_name_list[production_source_1]].corr(production_data[group_name_list[production_source_2]])
    new_data.plot.scatter(x=group_name_list[production_source_1], y=group_name_list[production_source_1], title=f"Correlation between electricity production from {production_source_1} and electricity production from {production_source_2} of individual nations (2019)", xlabel=production_types_semantic(production_source_1), ylabel=production_types_semantic(production_source_2))
    plt.show()