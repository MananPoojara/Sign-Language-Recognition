n = int(input())

if (n % 2) == 1 :
    print("Weird")
elif (n % 2 == 0) and range(2,5):
    print("Not Weird")
elif (n % 2) == 0 or range(6,20):
    print("Weird")
elif (n<20 % 2) == 0:
    print("Not Weird")
else:
    print("invalid")