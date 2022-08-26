a = int(input("enter a number: "))
print(f"prime numbers from 0 to {a}")
for i in range(2, a+1):
    control = 0
    for j in range(2, i):
        if (i % j) == 0:
            control = 1
    if control == 0:
        print(i)
