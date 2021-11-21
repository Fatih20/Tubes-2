import pandas as pd
import matplotlib.pyplot as plt

from tools import *

colors_of_specific_energy_source = ["dimgrey", "red", "steelblue", "lawngreen", "orange", "black", "gainsboro", "gold"]
colors_of_source_group_type = {
    "Energy From Fossil Fuels (TWH)" : "dimgrey", 
    "Energy From Renewables (TWH)" : "lawngreen", 
    "Energy From Nuclear (TWH)": "gold"
}

specific_energy_source_color ={}
for production_source in production_source_list:
    for color in colors_of_specific_energy_source:
        specific_energy_source_color[production_source] = color 


production_data = pd.read_csv("Electricity_Production_By_Source_Cleansed.csv")

def state_production_in_year (country, year):
    examined_state_data = state_production_raw(country)
    examined_row = examined_state_data.loc[(examined_state_data["Year"] == year)]
    return examined_row

def state_source_in_year (country, year):
    data = state_production_in_year(country, year)
    for production_source in production_source_list:
        data.rename(columns={production_types_semantic(production_source): production_source}, inplace=True)
    transposed_row = data.loc[:, "coal":"nuclear"].transpose()
    return (transposed_row)

#Perbandingan kategori
# state_source_in_year("United States", year=2019).plot(kind="pie", subplots=True, ylabel="", colors=colors_of_specific_energy_source, title="Electricity production in the US based on their source (2019)")
# plt.show()

# state_source_in_year("Indonesia", year=2019).plot(kind="pie", subplots=True, ylabel="", colors=colors_of_specific_energy_source, title="Electricity production in the Indonesia based on their source (2019)")
# plt.show()

# Penampilan perubahan terhadap waktu
# state_production_group_type("Ireland").plot(kind="line", x="Year", y=["Energy From Fossil Fuels (TWH)", "Energy From Renewables (TWH)", "Energy From Nuclear (TWH)"], title="Evolution of Ireland's source of electricity (2000-2019)", style=colors_of_source_group_type)
# plt.show()

# state_production_group_type("Japan").plot(kind="line", x="Year", y=["Energy From Fossil Fuels (TWH)", "Energy From Renewables (TWH)", "Energy From Nuclear (TWH)"], title="Evolution of Japan's source of electricity (2000-2019)", style=colors_of_source_group_type)
# plt.show()

#Penampilan hubungan keseluruhan-bagian
# state_production_raw("France", cleaned=True).plot(kind="bar", stacked=True, x="Year", title="Composition of France's source of electricity (2000-2019)", color=colors_of_specific_energy_source)
# plt.show()

# state_production_raw("Germany", cleaned=True).plot(kind="bar", stacked=True, x="Year", title="Composition of Germany's source of electricity (2000-2019)")
# plt.show()

#Scatter plot
# state_production_group_type("Belgium").plot.scatter(x="Energy From Fossil Fuels (TWH)", y="Energy From Renewables (TWH)", title="Comparison of Belgium's electricity from renewables vs fossil fuels (2000-2019)")
# plt.show()

# state_production_group_type("India").plot.scatter(x="Energy From Fossil Fuels (TWH)", y="Energy From Renewables (TWH)", title="Comparison of India's electricity from renewables vs fossil fuels (2000-2019)")
# plt.show()