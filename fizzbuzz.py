#FizzBuzz task
n = int(input())

for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 2 == 0:
        continue
    elif x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0:
        print("Buzz")
        continue
    
    else:
        print(x)
        continue