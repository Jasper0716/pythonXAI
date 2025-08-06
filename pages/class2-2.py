import streamlit as st  # 匯入streamlit模組並重新命名st

# st.number_input()可以讓使用者輸入數字,設定step=1可以讓使用者只能輸入整數
# min_value=0設定最小值為0, max_value=100設定最大值為100
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100)
# st.markdown()可以讓使用者輸入Markdown格式的文字
st.markdown(f"你輸入的數字是：{number}")

st.title("練習")
score = st.number_input("請輸入一個score", step=1, min_value=0, max_value=100)
if score >= 90:
    st.markdown("A")
elif score >= 80:
    st.markdown("B")
elif score >= 70:
    st.markdown("C")
elif score >= 60:
    st.markdown("D")
elif score < 59:
    st.markdown("f")

st.markdown("---")
st.markdown("###案鈕練習")
# st.button()可以讓使用者點擊按鈕
# key是按鈕的識別名稱,可以用來區分不同的按鈕
# 如果使用者點擊按鈕,st.button()會回傳True,否則回傳False
st.button("點我", key="button1")
if st.button("點我", key="ballons"):
    st.balloons()
if st.button("點我", key="snow"):
    st.snow()
st.markdown("---")
