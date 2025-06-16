first = int(input("enter 1st number: "))
second = int(input("enter 2nd number: "))

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b


def output():

    print("sum: ", sum(first,second))
    print("sum: ", sub(first,second))
    print("sum: ", multi(first,second))
    print("sum: ", div(first,second))