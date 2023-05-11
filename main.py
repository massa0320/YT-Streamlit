import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバー表示')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'










st.write('Intaractive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')


# text = st.text_input('what is your hobby')
# condition = st.slider('調子は？', 0, 100, 50)
# 'My hobby is', text ,'.'
# '調子は', condition

#st.write('Display Image')
# st.write('Intaractive Widgets')

# text = st.text_input('what is your hobby')
# 'My hobby is', text ,'.'


# option = st.selectbox(
#     'あなたが好きな数字は？',
#     list(range(1,11))
# )

# 'number = ', option, '.'

# if st.checkbox('Show Image'):
#     img = Image.open('1.png')
#     st.image(img, caption='スクショ', use_column_width=True)