import pandas as pd
df = pd.read_parquet('/home/q639524/data/Export_LLP/722cfeae-6396-4094-afac-018c80c3a1ac/merged_file.snappy.parquet')
df.to_csv('/home/q639524/data/Export_LLP/finaltrajectory.csv')
