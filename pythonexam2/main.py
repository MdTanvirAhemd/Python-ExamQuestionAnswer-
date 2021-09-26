# a)
# function which return palindrome
# def isPalindrome(s):
#     # function which return reverse of a string
#     def revSt(s):
#         return s == s[::-1]
#
#     # Driver code
#     ans = revSt(s)
#     if ans:
#         print("Yes.This is a palindrome.")
#     else:
#         print("No.This is not a palindrome.")
#
# isPalindrome("MADAM")
# b)
# def printRightTringle(num):
#     space = 0
#     for value in range(num, 0, -1):
#         for i in range(space):
#             print(" ", end="")
#         for star in range(value):
#             print("*", end="")
#         print()
#         space += 1
#
# printRightTringle(6)



# c)
def countup(N, n=1):
    print(n)
    if n < N:
        countup(N, n + 1)

countup(20)