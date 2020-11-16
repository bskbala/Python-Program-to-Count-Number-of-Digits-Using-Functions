# Python Program to Count Number of Digits in a Number #

def Counting(Number):
    count =0;
    while(Number >0):
        Number = Number//10
        count = count+1
    print("\n Number of Digits in a Given Number = %d" %count)

Counting(1252)