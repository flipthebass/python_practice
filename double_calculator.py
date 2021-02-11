"""Task:
Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.

"""

def task():
    mil=1000000*(2**30)
    pen=0.01*(2**30)
    print(mil)
    print(pen)


    if mil>pen:
        print("A million is larger")
    else:
        print("A penny is larger")



if __name__ == '__main__':
    task()