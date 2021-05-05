from django.db import models
import pandas

# Create your models here.
df = pandas.read_csv('sample.csv')
df = df[['dong']]
# df.duplicated(['dong'])
converted = df.drop_duplicates(subset=['dong'], ignore_index = True, keep='first')
converted.to_csv('dong_unique.csv')

