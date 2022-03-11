import sqlite3
import pandas as pd

conn = sqlite3.connect('D:\Development\django\django_graphql\db.sqlite3')

df = pd.read_csv('D:\Development\django\django_graphql\pradeep.csv')

df['id'] =df.index
# print(df.columns)
df = df[['Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold', 'id']]

df.to_sql('gqapp_productmodel', conn, if_exists='replace', index=False)