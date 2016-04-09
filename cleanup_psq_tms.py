import pandas, numpy

def cleanup_psq_tms():
    PSQ_TMS = pandas.read_csv("data/PSQ_TMS.csv", skiprows=range(5),
     na_values="*")
    PSQ_TMS.drop(["Origin / Returned from", "Population type"], axis=1,
    inplace=True)
    countries = PSQ_TMS["Country Name"].unique()

    filtered = pandas.DataFrame()

    for c in countries:
        country_rows = PSQ_TMS[PSQ_TMS["Country Name"] == c]
        country_sum = country_rows.iloc[:,1:].sum()
        new_values = pandas.Series([c], ["Country Name"]).append(country_sum)
        filtered = pandas.concat([filtered,
                                  pandas.DataFrame(new_values).transpose()])
    filtered.to_csv("data/PSQ_TMS_filtered.csv", index=False)
    return filtered
