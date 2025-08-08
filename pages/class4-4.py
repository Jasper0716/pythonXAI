import random

d = []


def hello():
    d.append(random.randrange(1, 6))

    a = int(input())
    for i in range(a):
        hello()
    print(d)
