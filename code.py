from bs4 import BeautifulSoup
import pandas as pd
df = pd.read_csv('patientData.csv')
print(df.head())

import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["patient_database"]
collection = db["patient_data"]

non_profit_providers = df[(df['Ownership Type'] == 'Non-Profit') & (df['Certification Date'] > pd.to_datetime('2011-10-01'))]
print(non_profit_providers)

birmingham_profit_providers = df[(df['City/Town'] == 'BIRMINGHAM') & (df['Ownership Type'] == 'Profit')]
print(birmingham_profit_providers)

zip_code_providers = df[(df['ZIP Code'].astype(str).astype(int) >= 85000) & (df['ZIP Code'].astype(str).astype(int) <= 90000)]
print(zip_code_providers)
