import os
import random
from time import sleep


import pandas as pd
import requests

#定数定義
IMAGE_DIR = './images/'

#CSV読み込み
df = pd.read_csv('image_urls.csv')

#フォルダの存在確認
if os.path.isdir(IMAGE_DIR):
  print('すでにあります！')
else:
  os.makedirs(IMAGE_DIR)

#画像の保存
for file_name, yahoo_img_url in zip(df.filename[:5], df.yahoo_img_url):
  image = requests.get(yahoo_img_url)
  with open(IMAGE_DIR + file_name + '.jpg', 'wb') as f:
    f.write(image.content)

#sleep時間をランダム調整して機械的な動きをなくす
  sleep(random.randint(1,10))