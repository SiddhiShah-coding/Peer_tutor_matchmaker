n = int(input("Enter the value of n: "))
for i in range(n + 1, 1, -2):
    if n % 2 == 1:
        print("Please Enter the even number")
        break
    pass  # or some other code to execute in the loop
    print(i)

