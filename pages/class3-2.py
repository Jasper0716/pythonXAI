import streamlit as st

# --- 新的點餐功能區 ---
st.write("---")
st.title("📝 點餐機 - 手動輸入餐點")

# 初始化購物車
if "cart" not in st.session_state:
    st.session_state.cart = []

# 餐點輸入欄位
food = st.text_input("請輸入想要點的餐點名稱：", value="")

# 加入餐點按鈕
if st.button("加入餐點", key="add_food"):
    if food.strip() != "":
        st.session_state.cart.append(food.strip())
        st.rerun()  # 加入後自動清除輸入框

# 顯示購物車內容
st.write("## 🛒 購物車內容：")

if len(st.session_state.cart) == 0:
    st.write("目前購物車是空的。")
else:
    for i, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{i+1}. {item}")
        with col2:
            if st.button("刪除", key=f"delete_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()

# 重新整理整個畫面
st.write("---")
if st.button("🔄 重新整理整個畫面", key="refresh_all"):
    st.rerun()
