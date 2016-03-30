#! /usr/local/bin/python2
import pandas

def cleanup_fragile_states():
    FSPATH = "data/fragilestatesindex-2006to2014.xlsx"
    fsi_sheets = pandas.read_excel(FSPATH, sheetname=None, parse_cols="B:O")
    data = pandas.DataFrame()
    for year, data_yr in sorted(fsi_sheets.iteritems()):
        # Cover all bases - they chaned naming at some point through
        failed= "Failed States Index %s" % year
        fragile = "Fragile States Index %s" % year
        renaming_dict = {failed: "Country Name", fragile:"Country Name"}
        data_yr.rename(index=str, columns=renaming_dict, inplace=True)
        data_yr.rename(index=str, columns=lambda col: col + " " + str(year),
                       inplace=True)
        data_yr.rename(index=str, columns={"Country Name "+year:"Country Name"},
         inplace=True)
        cols_to_use = data_yr.columns.difference(data.columns)
        data = pandas.concat([data, data_yr[cols_to_use]], axis=1)
    data.to_csv("data/fragilestatesindex_joined.csv", index=False)

    return data
