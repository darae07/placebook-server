import pandas
import numpy

#storeData = 소상공 csv 데이터
df = pandas.read_csv('storeData.csv', sep='|')
df = df.loc[df['상권업종대분류명'] == '음식']
df = df[['상호명', '상권업종중분류명', '상권업종소분류명', '표준산업분류명', '행정동명', '위도', '경도']]
df.colums = ['name', 'categ_1', 'categ_2', 'categ_3', 'loc', 'lon', 'lat']
df.to_csv('sample.csv')