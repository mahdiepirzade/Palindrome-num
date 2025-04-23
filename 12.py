
num = int(input("plz enter a num: "))

copy_num = num
original_num = num

temp = num
count = 0
while temp > 0:
    temp = temp // 10
    count = count + 1

count = count - 1
reversed_ = 0
while count >= 0:
    rem = copy_num % 10
    copy_num = copy_num // 10
    reversed_ = reversed_ + rem * (10 ** count)
    count = count - 1



print("Reveresd num is: ", reversed_)
if original_num == reversed_:
    print("they are palindrome. ")
else:
    print("they are not palindrome. ")


