"""
這是多行註解
"""

# 這是單行註解
print("Hello, World!")  # 這是行尾註解
# ctrl+? 可以快速註解/取消註解


# 基本型態
print(1)  # int這是整數, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
print(1.1)  # float這是浮點數
print(1.234)  # float這是浮點數
print("apple")  # str這是字串 "sadasd123125557", '1'
print(True)  # bool這是布林值 True/False
print(False)  # bool這是布林值 True/False


# 變數
a = 10  # 新增一個儲存空間並命名為a，"="代表將右邊的值存入左邊的變數
print(a)  # 印出變數a的值
a = "apple"  # 將變數a的值改為"apple"
print(a)  # 印出變數a的值

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 % 1)  # 取餘數
print(2**3)  # 乘方
print(1 // 1)  # 整數除法

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減


# 字串運算，+、*
print("apple" + " pen")  # 字串相加
print("apple " * 3)  # 字串乘法


print(len("apple"))  # len()是一個函式，可以計算字串的長度
print(len("，"))  # len()是一個函式，可以計算字串的長度
# type()  # 可以查看變數的型態
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>

# 型態轉換
print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(bool(1))  # int轉bool
print(int(1.234))  # float轉int
print(float("1.234"))  # str轉float
print(str(1.234))  # float轉str
print(bool(1.234))  # float轉bool
# print(int("hello"))  # 這行會報錯，因為字串裡面如果有非數字的字元，無法轉換成數字


print("輸入開始")
# input()是一個函式，可以讓使用者輸入文字
# ()裡面的文字是提示訊息會先顯示在終端機才會等待使用者輸入
a = input("請輸入一些文字:")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明透過input()輸入內容都是字串
menu_list =[
{"id":1, "name":"1.漢堡","price":60,"colaries":294.9,"$":"元","kcal":"大卡"},
{"id":2, "name":"2.米漢堡","price":80,"colaries":217.7,"$":"元","kcal":"大卡"},
{"id":3, "name":"3.薯條","price":30,"colaries":311.9,"$":"元","kcal":"大卡"},
{"id":4, "name":"4.沙拉","price":45,"colaries":62,"$":"元","kcal":"大卡"},
{"id":5, "name":"5.可樂","price":20,"colaries":37.5,"$":"元","kcal":"大卡"},
{"id":6, "name":"6.紅茶","price":15,"colaries":1,"$":"元","kcal":"大卡"}]
order_list = []
print('==========歡迎光臨本餐廳,祝您用餐愉快==========')
print('今日菜單:')
for menu in menu_list:
print(menu.get('name'),menu.get('price'),menu.get('$'),menu.get('colaries'),menu.get('kcal'))
while True:
print('='*50)
print('1.點餐\n2.取消點餐\n3.確認菜單\n4.結帳')
serve = int(input("請選擇服務:"))
if serve == 1:
while True:
menu_add = input("請輸入菜名編號或者輸入X結束點餐:")
if menu_add != "X":
for i in menu_list:
if i.get('id')== int(menu_add):
order_list.append(i)
else:
print('==========已完成點餐=========')
bill = 0
for order in order_list:
print(order.get('name'),order.get('price'),order.get('$'),order.get('colaries'),order.get('kcal'))
bill += int(order.get('price'))
print(' 小計:{}元'.format(bill))
break
elif serve == 2:
menu_del = input("請輸入要取消之菜名:")
order_list.remove(order)
print('==========已完成點餐=========')
bill = 0
for order in order_list:
 print(order.get('name'),order.get('price'),order.get('$'),order.get('colaries'),order.get('kcal'))
bill += int(order.get('price'))
print(' 小計:{}元'.format(bill))
 elif serve == 3:
print('==========已完成點餐=========')
bill = 0
for order in order_list:
print(order.get('name'),order.get('price'),order.get('$'),order.get('colaries'),order.get('kcal'))
bill += int(order.get('price'))
print(' 小計:{}元'.format(bill))
elif serve == 4:
print('==========您的消費明細==========')
bill = 0
for order in order_list:
print(order.get('name'),order.get('price'),order.get('$'))
bill += int(order.get('price'))
print(' 總計:{}元'.format(bill))
print('==========謝謝光臨，歡迎再來==========')
break
輸入X依舊無法break
謝謝大家...