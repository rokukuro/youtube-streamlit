from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = r'D:\MyPython\programs\Selenium\chromedriver.exe'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path,options=options)

url = 'https://search.yahoo.co.jp/image'
driver.get(url)

sleep(3)

query = '本田忠勝'

#どのclassで検索するか決めて、search_boxへ格納
search_box = driver.find_element_by_class_name('SearchBox__searchInput')

#search_boxにキーワードを送る
search_box.send_keys(query)

#queryのキーワードで検索
search_box.submit()

sleep(3)

driver.quit()