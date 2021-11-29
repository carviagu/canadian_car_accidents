
import pandas as pd
import os 


def csv_parquet_converter(origin = "", dest = "output.parquet"):
    '''
    Makes conversion of csv file to parquet file type.
    Params:
    :origin: Direction to the csv file to make conversion.
    :dest: Direction to keep the parquet file, name must be included.
    '''
    if (origin == ""):
        return("ERROR: You must provide a csv file to make conversion.")
    
    csv_version = pd.read_csv(origin, low_memory=False)
    csv_version.to_parquet(dest, engine='auto', compression='snappy')

    return("Conversion succesfull. File is available at: " + dest)


def canadian_car_accidents_import():
    '''
    Import Canada Car Accidents dataset.
    '''
    if (os.path.isfile("../data/NCDB_1999_to_2014.csv")):
        return(pd.read_csv("../data/NCDB_1999_to_2014.csv", low_memory=False))

    return(print("ERROR: Canada Car Accidents don't available at data folder. " + 
    "Please download the dataset from: https://www.kaggle.com/tbsteal/canadian-car-accidents-19942014"))