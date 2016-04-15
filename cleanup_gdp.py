import pandas

def cleanup_gdp():
    gdp_info = pandas.read_csv("data/world_bank_gdp/GDP_2011-2015.csv",
    skiprows=4)

    gdp_info.drop(["Country Code", "Indicator Name", "Indicator Code",
                   "Unnamed: 60"],
                  inplace=True, axis=1)
    gdp_info.drop([str(x) for x in range(1960, 2000)], inplace=True, axis=1)

    rename_cols = {col: "GDP (%s, billions of $)" % col
                   for col in gdp_info.columns[1:]}
    gdp_info.rename(index=str, columns=rename_cols, inplace=True)

    scaled_gdp = gdp_info.iloc[:, 1:].apply(lambda x: x  / (10**9))
    gdp_info  = pandas.concat([gdp_info["Country Name"], scaled_gdp], axis=1)
    gdp_info.to_csv("data/world_bank_gdp/GDP_filtered.csv", index=False)
