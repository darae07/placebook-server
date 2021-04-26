import pandas
import numpy

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#storeData = 소상공 csv 데이터
df = pandas.read_csv('storeData.csv', sep='|')
df = df.loc[df['상권업종대분류명'] == '음식']
df = df[['상호명', '상권업종중분류명', '상권업종소분류명', '표준산업분류명', '행정동명', '위도', '경도']]

df['category'] = df['상권업종중분류명'] + df['상권업종소분류명'] + df['표준산업분류명']
df['category'] = df['category'].str.replace("/", " ")
df.to_csv('sample.csv')

count_vect_category = CountVectorizer(min_df=0, ngram_range=(1,2))
place_category = count_vect_category.fit_transform(df['category'])
place_simi_categ = cosine_similarity(place_category, place_category)
place_simi_categ_sorted_ind = place_simi_categ.argsort()[:, ::-1]

#출처 : https://data101.oopy.io/recommendation-engine-cosine-similarity
# TODO: 데이터 클렌징, 사이킷런 오류 해결