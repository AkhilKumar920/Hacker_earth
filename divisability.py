total = int(input())
numbers = input().split(" ")
x = str(numbers[-1])[-1]
if int(x)%10 == 0:
    print("Yes")
else:
    print("No")