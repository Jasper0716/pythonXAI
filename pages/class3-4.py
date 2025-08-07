import random

a = random.randrange(1, 101)  #
print(a)
while True:
    input_value = int(input("請輸入數字(1-100)："))

    if a == input_value:
        print("恭喜答對了！")
        break
    elif a > input_value:
        print("猜錯了，答案比你猜的數字大！")
    elif a < input_value:
        print("猜錯了，答案比你猜的數字小！")
