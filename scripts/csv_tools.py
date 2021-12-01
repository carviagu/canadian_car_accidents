############################################
# Script with functions to manage data files
############################################

import pandas as pd
import os


def csv_parquet_converter(origin="", dest="output.parquet"):
    '''
    Makes conversion of csv file to parquet file type.
    :param origin: Direction to the csv file to make conversion.
    :param dest: Direction to keep the parquet file, name must be included.
    '''
    if origin == "":
        return "ERROR: You must provide a csv file to make conversion."

    csv_version = pd.read_csv(origin, low_memory=False)
    csv_version.to_parquet(dest, engine='auto', compression='snappy')

    return "Conversion successful. File is available at: " + dest


# This method is created to check the dataset before making import
# This was created due to the dataset is very heavy to have it at
# the repository. So sometimes user can forget to download it.
def csv_import(origin=""):
    '''
    Import Canada Car Accidents dataset. If the dataset is not
    at data folder, will throw an error.
    :param origin: csv_file_to_read
    '''
    if os.path.isfile(origin):
        print('Reading file...')
        data = pd.read_csv(origin, low_memory=False)
        print('Reading ended.')
        return data

    print("ERROR: Archive don't available at data folder.")
    return -1

def csv_import_na(origin="", as_na=None):
    '''
    Import Canada Car Accidents dataset with na values.
    If the dataset is not at data folder, will throw an error.
    :param as_na: values to read as NaN
    :param origin: csv_file_to_read
    '''
    if as_na is None:
        return (print("ERROR: No NA values provided. Use csv_import if " +
                      "you want to import the data without NA treatment."))

    if os.path.isfile(origin):
        print('Reading file...')
        data = pd.read_csv(origin, na_values= as_na, low_memory=False)
        print('Reading ended.')
        return data

    print("ERROR: Archive don't available at data folder.")

    return -1