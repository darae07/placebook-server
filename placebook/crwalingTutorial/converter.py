import pandas
import numpy

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#storeData = 소상공 csv 데이터
def data_converter():
    df = pandas.read_csv('storeData.csv', sep='|')
    df = df.loc[df['상권업종대분류명'] == '음식']
    df = df[['상호명', '상권업종중분류명', '상권업종소분류명', '표준산업분류명', '행정동명', '위도', '경도']]

    df['category'] = df['상권업종중분류명'] + df['상권업종소분류명'] + df['표준산업분류명']
    df['category'] = df['category'].str.replace("/", " ")
    df.rename(columns = {'상호명': 'name', '상권업종중분류명': 'cate_1', '상권업종소분류명': 'cate_2', '표준산업분류명': 'cate_3', '행정동명': 'dong', '위도': 'lon', '경도': 'lan'}, inplace = True)
    df.to_csv('sample.csv')

def data_calculer(name):
    # null 처리
    df = pandas.read_csv('sample.csv')
    df = df.head(20000)
    
    dong = df.loc[df['name'] == name].values[0][5]
    print(dong, type(dong))
    # df = df.loc[df['dong'] == dong]
    df['category'] = df['category'].fillna('')
    print(df['category'].isnull().sum())
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['category'])
    print(tfidf_matrix.shape)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pandas.Series(df.index, index=df['name']).drop_duplicates()

    cosine_sim=cosine_sim
    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    store_indices = [i[0] for i in sim_scores]
    return df['name'].iloc[store_indices]
    # def get_recommendations(name, cosine_sim=cosine_sim):
        

    # print(get_recommendations('호랑이가만든족발'))


print(data_calculer('든든한우家'))
# count_vect_category = CountVectorizer(min_df=0, ngram_range=(1,2))
# place_category = count_vect_category.fit_transform(df['category'])
# place_simi_categ = cosine_similarity(place_category, place_category)
# place_simi_categ_sorted_ind = place_simi_categ.argsort()[:, ::-1]

#출처 : https://data101.oopy.io/recommendation-engine-cosine-similarity
# TODO: 데이터 클렌징, 사이킷런 오류 해결