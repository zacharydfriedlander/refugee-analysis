import pandas

def cleanup_cpia():
    metadata = pandas.read_csv("data/cpia/CPIA-Series.csv")

    series_codes = metadata["Series Code"]

    data = pandas.read_csv("data/cpia/CPIA-Data.csv")

    data_clean = pandas.DataFrame(data["Country Name"], columns=["Country Name"])

    for code in series_codes:
        data_slice = data[data["Indicator Code"] == code]
        data_slice.drop(["Country Code", "Indicator Name", "Indicator Code"],
                        axis=1, inplace=True)
        data_slice.rename(columns={str(year) : code + ", " + str(year)
                                   for year in range(2005, 2015)}, inplace=True)
        data_clean = data_clean.merge(data_slice, on="Country Name", how='outer')

    data_clean.to_csv("data/cpia/CPIA-Data_clean.csv", index=False)
