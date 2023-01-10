from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_path = r'D:\MyPython\programs\Selenium\chromedriver.exe'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path = chrome_path, options=options)

url = 'https://search.yahoo.co.jp/image'
driver.get(url)

sleep(3)

query = 'プログラミング'

#どのclassで検索するか決めて、search_boxへ格納
search_box = driver.find_element_by_class_name('SearchBox__searchInput')

#search_boxにキーワードを送る
search_box.send_keys(query)

#queryのキーワードで検索
search_box.submit()

sleep(3)

#スクロールする
height = 1000
while height < 3000:
  driver.execute_script("window.scrollTo(0,{});".format(height))
  height += 100
  print(height)

  sleep(1)

  #画像の要素を検索する
  elements = driver.find_elements_by_class_name('sw-Thumbnail')
  #print(len(elements))

  d_list = []

  #要素からURLと番号を取得
  for i, element in enumerate(elements, start=1):
    name = f'{query}_{i}'
    #元のURLを保存
    raw_url = element.find_element_by_class_name(
      'sw-ThumbnailGrid__details').get_attribute('href')

    yahoo_img_url = element.find_element_by_tag_name('img').get_attribute('src')

    title = element.find_element_by_tag_name('img').get_attribute('alt')

    d = {
      'filename': name,
      'raw_url': raw_url,
      'yahoo_img_url': yahoo_img_url,
      'title': title
    }

    d_list.append(d)

    sleep(2)

    #print('finished {}'.format(name))

df = pd.DataFrame(d_list)
df.to_csv('image_urls.csv',index=None,encoding='utf-8-sig')

driver.quit()