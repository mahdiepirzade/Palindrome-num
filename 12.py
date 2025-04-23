
#2
copy_num = num
original_num = num

count = 0
while num > 0:
    num = num // 10
    count = count + 1

count = count - 1
reversed_ = 0
while count >= 0:
    rem = copy_num % 10
    copy_num = copy_num // 10
    reversed_ = reversed_ + rem * (10 ** count)
    count = count - 1

if original_num == reversed_:
    print("they are palindrome. ")
else:
    print("they are not palindrome. ")


