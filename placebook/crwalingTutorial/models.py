from django.db import models
import pandas
from psycopg2 import connect

# Create your models here.
df = pandas.read_csv('sample.csv')
df = df[['dong']]
# df.duplicated(['dong'])
converted = df.drop_duplicates(subset=['dong'], ignore_index = True, keep='first')
converted.to_csv('dong_unique.csv')

# engine = create_engine('postgresql://root:12341234@localhost:5432/placebook')
# converted.to_sql('dong', engine)

conn = connect(host='localhost', port=5432, database='placebook', user='root', password='12341234')
cur = conn.cursor()
cur.execute(""" 
    DROP TABLE IF EXISTS dong;
    CREATE TABLE dong(
        index SMALLINT,
        dong varchar(100)
        );
""")
conn.commit()
query = """ 
    COPY dong FROM STDIN DELIMITER ',' CSV;
"""
with open('./dong_unique.csv', 'r') as f:
    cur.copy_expert(query, f)
conn.commit()

conn.close()