import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:2266@localhost:3306/retail')

file_path = r'c:\Users\SAI CHIRU\Videos\Netflix_400000.csv'

df = pd.read_csv(file_path)

table_name = 'netflix'
df.to_sql(table_name, con=engine, if_exists='append', index=False, chunksize=1000)

print("sucessfully uploaded!")
