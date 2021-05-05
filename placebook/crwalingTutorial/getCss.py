from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
# import chromedriver_binary
import pandas

driver = webdriver.Chrome()

df = pandas.read_csv('sample.csv')
df = df.head(100)
df['kakao_keyword'] = df['dong'] + "%20" + df['name']
df['kakao_url'] = ''

# kakao_search_url = "https://map.kakao.com/?q=혜화동%20커피빈"
# driver.get(kakao_search_url)
# print(driver.find_element_by_css_selector('#info\.search\.place\.list > li.PlaceItem.clickArea > div.rating.clickArea > span.score > a').get_attribute('href'))
wait = WebDriverWait(driver, 5)
for i, keyword in enumerate(df['kakao_keyword'].tolist()):
    print('키워드', i, df.shape[0], keyword)
    try:
        kakao_search_url = f"https://map.kakao.com/?q={keyword}"
        driver.get(kakao_search_url)
        element = wait.until(presence_of_element_located((By.CSS_SELECTOR, '#info\.search\.place\.list > li.PlaceItem.clickArea > div.rating.clickArea > span.score > a')))
        print(element.get_attribute('href'))
        df.loc[i,'kakao_url'] = element.get_attribute('href')
        if i // 1000 == 0:
            df.to_csv('sample_with_kakao.csv')
    except Exception as e1:
        pass 
df.to_csv('sample_with_kakao.csv')

##info\.search\.place\.list > li.PlaceItem.clickArea > div.rating.clickArea > span.score > a