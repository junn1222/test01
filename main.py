import time
import streamlit as st
import numpy as np 
import pandas as pd
from PIL import Image

st.title('Juns Streamlit')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar =st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.001)

'Done!!!'

st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button =left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1=st.expander('問い合わせ')
expander1.write('a')
expander2=st.expander('問い合わせ')
expander2.write('a')
expander3=st.expander('問い合わせ')
expander3.write('a')

text =st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味：',text

option=st.sidebar.selectbox(
    'Tell your favorite number',
    list(range(1,11))
)
'あなたの好きな数字は', option,'です。'

condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'コンディション：',condition

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img,caption='激うまチャーライ',use_column_width=True)


st.write('DataFrame')

df1 = pd.DataFrame({
    ' 1列目':[1,2,3,4],
    ' 2列目':[10,20,30,40]
})

df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [34.3172,135.191],
    columns=['lat','lon']
)

st.map(df2)
st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)


#静的表
st.table(df1.style.highlight_max(axis=1))
#動的表
st.dataframe(df1.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np 
# import pandas as pd
# ```

# """
