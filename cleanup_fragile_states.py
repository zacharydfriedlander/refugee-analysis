#! /usr/local/bin/python2
import pandas

def cleanup_fragile_states():
    FSPATH = "data/fragilestatesindex/"
    data = pandas.DataFrame()
    for year in range(2006,2015):
        filename = FSPATH+"fragilestatesindex%d.csv" % year
        data_yr = pandas.read_csv(filename)
        data_yr.rename(index=str, columns=lambda col: col + str(year), inplace=True)
        data = pandas.concat([data, data_yr], axis=1)
    data.to_csv(FSPATH+"fragilestatesindex_joined.csv", index=False)
