import pandas as pd
import matplotlib.pyplot as plt

production_data = pd.read_csv("Electricity_Production_By_Source_Cleansed.csv")

production_types = {
    "renewables" : [
        "hydro",
        "solar",
        "wind",
        "other renewables",

    ],
    "fossil" : [
        "coal",
        "oil",
        "gas",

    ],
    "nuclear" : [
        "nuclear",
    ]
}

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

def state_production_raw(country_name, cleaned=False):
    if cleaned:
        return production_data.loc[production_data["Entity"] == country_name].loc[:, "Entity":production_types_semantic("nuclear")]
    else:
        return production_data.loc[production_data["Entity"] == country_name]
# Dengan menggunakan production of state, kita bisa langsung mengambil data produksi sebuah negara yang kemudian bisa dimasukkan ke fungsi-fungsi lain

def state_production_specific_type (country, energy_source, year_start=2000, year_end = 2020):
    examined_state_data = state_production_raw(country)
    return (examined_state_data.loc[(examined_state_data["Year"] >= year_start) & (examined_state_data["Year"] < year_end), production_types_semantic(energy_source)])

def group_type_grabber (examined_state_data, year, group_type):
    global production_types
    examined_row = examined_state_data.loc[(examined_state_data["Year"] == year)]
    result = 0
    for production_type in production_types[group_type]:
        result += float(examined_row.loc[:, production_types_semantic(production_type)])
    return result

#Gunakan tahun sebagai baris
def state_production_group_type (country, year_start=2000, year_end = 2020):
    examined_state_data = state_production_raw(country)
    result_dict = {
        "Year" : [i for i in range(year_start, year_end)],
        "Energy From Fossil Fuels (TWH)" : [group_type_grabber(examined_state_data, year, "fossil") for year in range(year_start, year_end)],
        "Energy From Renewables (TWH)" : [group_type_grabber(examined_state_data, year, "renewables") for year in range(year_start, year_end)],
        "Energy From Nuclear (TWH)" :  [group_type_grabber(examined_state_data, year, "nuclear") for year in range(year_start, year_end)],       
    }   
    result = pd.DataFrame(data=result_dict)
    return result

#Gunakan tahun sebagai baris
def state_production_total (country, year_start=2000, year_end = 2020):
    examined_state_data = state_production_raw(country)
    result_dict = {
        "Year" : [i for i in range(year_start, year_end)],
        "Total Energy Production (TWH)" : [float(examined_state_data.loc[(examined_state_data["Year"] == i), production_types_semantic("coal") : production_types_semantic("nuclear")].sum(axis=1)) for i in range(year_start, year_end)]
    }   
    result = pd.DataFrame(data=result_dict)
    return result

state_production_specific_type("Eastern Africa", "oil", 2000)
# state_production_total("Eastern Africa", 2000)
# state_production_group_type("Eastern Africa", 2000)

