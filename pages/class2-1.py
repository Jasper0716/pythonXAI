# 比較運算子
print(1 == 1)  # true
print(1 != 1)  # false
print(1 > 1)  # false
print(1 < 1)  # false
print(1 >= 1)  # true


##邏輯運算子
##and運算子
print(True and True)  # true
print(True and False)  # false
print(False and True)  # false
print(False and False)  # false

##or運算子
print(True or True)  # true
print(True or False)  # true
print(False or True)  # true
print(False or False)  # false


## not運算子
print(not True)  # false
print(not False)  # true

# 優先順序
# 1. ()括號
# 2. **次方
# 3. * / // %乘除取商取餘數
# 4. + - 加減
# 5. == !=><>=<=較運算子
# 6. not
# 7. and
# 8. or

rain = True
wind = False
# 密碼門檢查
password = input("請輸入密碼：")
if password == "1234":
    print("welcome Jeffery")
elif password == "5678":
    print("歡迎 Jeffery")
elif password == "0000":
    print("歡迎 Tom")
else:
    print("密碼錯誤")
# 連續使用if跟使用if elif else的差別
# elif可以排除前面有判斷過的條件，所以縮短判斷條件的複雜度，也節省了時間
# 但是如果是使用多個if來做獨立判斷，則每個if都會被執行，所以效率較低
