import pandas

def cleanup_pov():
    gdp_info = pandas.read_csv("data/world_bank_poverty/Poverty_raw.csv",
    skiprows=4)

    gdp_info.drop(["Country Code", "Indicator Name", "Indicator Code",
                   "Unnamed: 60"],
                  inplace=True, axis=1)
    gdp_info.drop([str(x) for x in range(1960, 2000)], inplace=True, axis=1)

    gdp_info.to_csv("data/world_bank_poverty/Poverty_filtered.csv", index=False)
