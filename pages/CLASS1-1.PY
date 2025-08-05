"""
這是多行註解
"""

# # 這是單行註解
# print("Hello, World!")  # 這是行尾註解
# # ctrl+? 可以快速註解/取消註解


# # 基本型態
# print(1)  # int這是整數, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
# print(1.1)  # float這是浮點數
# print(1.234)  # float這是浮點數
# print("apple")  # str這是字串 "sadasd123125557", '1'
# print(True)  # bool這是布林值 True/False
# print(False)  # bool這是布林值 True/False


# # 變數
# a = 10  # 新增一個儲存空間並命名為a，"="代表將右邊的值存入左邊的變數
# print(a)  # 印出變數a的值
# a = "apple"  # 將變數a的值改為"apple"
# print(a)  # 印出變數a的值

# # 運算子
# print(1 + 1)  # 加法
# print(1 - 1)  # 減法
# print(1 * 1)  # 乘法
# print(1 / 1)  # 除法
# print(1 % 1)  # 取餘數
# print(2**3)  # 乘方
# print(1 // 1)  # 整數除法

# # 優先順序
# # 1. () 括號
# # 2. ** 次方
# # 3. * / // % 乘 除 取商 取餘數
# # 4. + - 加 減


# # 字串運算，+、*
# print("apple" + " pen")  # 字串相加
# print("apple " * 3)  # 字串乘法


# print(len("apple"))  # len()是一個函式，可以計算字串的長度
# print(len("，"))  # len()是一個函式，可以計算字串的長度
# # type()  # 可以查看變數的型態
# print(type(1))  # <class 'int'>
# print(type(1.0))  # <class 'float'>
# print(type("apple"))  # <class 'str'>
# print(type(True))  # <class 'bool'>

# # 型態轉換
# print(int(1.0))  # float轉int
# print(float(1))  # int轉float
# print(str(1))  # int轉str
# print(bool(1))  # int轉bool
# print(int(1.234))  # float轉int
# print(float("1.234"))  # str轉float
# print(str(1.234))  # float轉str
# print(bool(1.234))  # float轉bool
# # print(int("hello"))  # 這行會報錯，因為字串裡面如果有非數字的字元，無法轉換成數字


# print("輸入開始")
# # input()是一個函式，可以讓使用者輸入文字
# # ()裡面的文字是提示訊息會先顯示在終端機才會等待使用者輸入
# a = input("請輸入一些文字:")
# print("輸入結束")
# print(int(a) + 10)
# print(type(a))  # 證明透過input()輸入內容都是字串


# a = int(input("請輸入數字:"))
# print(a * a * 3.14)

# 字串格式化
name = "apple"
age = 18
print(f"hello, my name is {name}, I am {age} years old")  # f-string格式化
# 可以將變數或其他形態的資料放到f字串裏面的{}，這樣就可以在字串中顯示
