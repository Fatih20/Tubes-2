import pandas as pd

production_source_list = [
    "hydro",
    "solar",
    "wind",
    "other renewables",
    "coal",
    "oil",
    "gas",
    "nuclear",
]

def production_types_semantic (energy_source):
    return f"Electricity from {energy_source} (TWh)"

production_data = pd.read_csv("Electricity_Production_By_Source.csv")

production_data_new = production_data

#Cari indeks semua baris yang tahunnya bermasalah
index_of_removed_year = production_data_new.loc[((production_data_new["Year"] <= 1999) & (production_data_new["Year"] >= 1985)) | (production_data_new["Year"] == 2020)].index
#Hapus indeks tersebut dari dataframe
production_data_new = production_data_new.drop(index_of_removed_year)
production_data_new.to_csv("Electricity_Production_By_Source_Cleansed_1.csv")

#Hapus semua baris yang kolom produksi energinya tidak lengkap
production_data_new = production_data_new.dropna(how="any", subset=[production_types_semantic(production_source) for production_source in production_source_list])
#Berkurang 180
production_data_new.to_csv("Electricity_Production_By_Source_Cleansed_2.csv")
print(production_data_new)