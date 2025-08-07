import streamlit as st
import os

floderpath = "markdown"  # 設定資料夾路徑
files = os.listdir(floderpath)  # 列出資料夾下所有檔案
# 這時資料夾可能包含其他檔案,我們只需要.md檔案
files_name = []  # 新增清單用來存放.md檔案
for f in files:  # 逐一追查所有檔案,看看是否以.md結尾
    if f.endswith(".md"):  # 看看是否以.md結尾
        # if".md" in f: #或是看看是否包含.md
        files_name.append(f)  # 將符合條件的檔案存入清單
files_name.sort()  # 將清單排序,預設是由小到大

for f in files_name:  # [class1.md, class2.md]逐一追查所有.md檔案
    # 用with open()讀取檔案內容並存到file變數裡面,模式為r,檔案編碼為utf-8
    # 這樣可以不用擔心檔案讀取後忘記關閉的問題
    # open參數格式為(檔案路徑,檔案模式,檔案編碼)
    # markdown\class2.md
    with open(f"{floderpath}/{f}", "r", encoding="utf-8") as file:
        # 開啟檔案後可以做很多事情,這裡我們只讀取檔案內容
        content = file.read()
    with st.expander(f):  # 使用streamlit的expander元件,讓使用者可以展開或收起內容
        st.markdown(content)  # 將檔案內容顯示在網頁上
