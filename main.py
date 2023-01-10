import streamlit as st
import time

st.title('streamlit 超入門')
st.write('プレグレスバー')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(0,100):
  latest_iteration.text(f'Itertion {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
