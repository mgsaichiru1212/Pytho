import pandas as pd
from sqlalchemy import create_engine

# 1. మైఎస్క్యుఎల్ కనెక్షన్ సెటప్ చేయండి
engine = create_engine('mysql+mysqlconnector://root:2266@localhost:3306/retail')

# 2. మీ CSV ఫైల్ పాత్ ఇవ్వండి
file_path = r'c:\Users\SAI CHIRU\Videos\Retail 40\RetailSales_CustomerProjectAnalysiss.csv'

# 3. CSV ఫైల్‌ని రీడ్ చేయడానికి read_csv ఉపయోగించండి
df = pd.read_csv(file_path)

# 4. డేటాని మైఎస్క్యుఎల్ టేబుల్ లోకి ఇన్సర్ట్ చేయండి
table_name = 'RetailSales_CustomerProjectAnalysis'
df.to_sql(table_name, con=engine, if_exists='append', index=False, chunksize=1000)

print("డేటా విజయవంతంగా మైఎస్క్యుఎల్ టేబుల్‌లోకి ఇన్సర్ట్ అయింది!")
