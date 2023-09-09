import sys

def DivExp(a,b):
    assert a>0,"a should be generated than 0"
    try:
        c=a/b
    except ZeroDivisionError:
        print("Value of b cannot be zero")
        sys.exit(0)
    else:
        return c
val1=int(input("Enter the value for a:"))
val2=int(input("Enter the value of b:"))
val3=DivExp(val1,val2)
print(val1,"/",val2,"=",val3)
