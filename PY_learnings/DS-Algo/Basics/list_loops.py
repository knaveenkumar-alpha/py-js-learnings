from random import randint

ls = [randint(i) for i in range(10)]
total = 0
for i in ls:
    print(i)
    total += i
    if i % 2 == 0:
        print(f"The number {i}: even or odd: True")











