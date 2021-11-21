import pandas as pd
from tools import *

production_data = pd.read_csv("Electricity_Production_By_Source.csv")

def change_to_1 (value):
    if value < 1:
        return 0
    else :
        return 1

#Jumlah baris data tahun 1985 sampai 1999 inklusif
previous_year_data = production_data.loc[(production_data["Year"] <= 1999) & (production_data["Year"] >= 1985)].loc[:, production_types_semantic("coal"):production_types_semantic("nuclear")]
print(len(previous_year_data.index))

# Jumlah baris data 2000 sampai 2019 inklusif yang memiliki sel kosong di kolom produksi energi
current_year_data = production_data.loc[(production_data["Year"] >= 2000) & (production_data["Year"] <= 2019)].loc[:, production_types_semantic("coal") : production_types_semantic("nuclear")]
series_of_index_with_empty_cell = current_year_data.isnull().sum(axis=1).apply(change_to_1)
print(series_of_index_with_empty_cell.sum())

#Jumlah baris data tahun 2020
print(len(production_data.loc[production_data["Year"] == 2020].index))