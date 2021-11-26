
# Este fichero permite la conversión de csv a parquet
# Ref: https://stackoverflow.com/questions/26124417/how-to-convert-a-csv-file-to-parquet

import pandas as pd

csv_file = 'NCDB_1999_to_2014.csv'
parquet_file = 'NCDB_1999_to_2014.parquet'

csv_version = pd.read_csv(csv_file, low_memory=False)
csv_version.to_parquet(parquet_file, engine='auto', compression='snappy')