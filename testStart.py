#0
# n = 5
# for a in range(1,n+1):
#     k = a
#     if():
#
#  for j in range(0,a+2):
#      print("*" , end=" ")
#      print()


for i in range(1,6,2):
    for j in range(0,i):
        print("*",end=""
                      " ")
    print()
for i in range(1,6,2):
    print("*",end=" ")

n = 5  # Maximum number of stars in the middle (must be an odd number)

# Top half of the diamond (including the middle line)
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2  # Calculate the number of leading spaces
    print(" " * spaces + "* " * i)

# Bottom half of the diamond (excluding the middle line)
for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2  # Calculate the number of leading spaces
    print(" " * spaces + "* " * i)