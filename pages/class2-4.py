import streamlit as st

st.title("數字金字塔")
number = st.number_input("請輸入一個number", step=1, min_value=1, max_value=9)
st.write("數字金字塔:")
for i in range(1, 9):
    print(" " * (9 - i), end="")  # 印出空格

for i in range(1, number + 1):

    st.write(str(i) * i)  # 印出數字金字塔的每一行
