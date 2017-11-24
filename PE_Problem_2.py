upper_limit = 4000000
first_fibonacci = 1
second_fibonacci = 1
temp = 0
sum = 0
while first_fibonacci<upper_limit:
    if first_fibonacci%2 == 0:
        sum = sum+first_fibonacci
        print(sum)
        #print(first_fibonacci)
        temp = first_fibonacci
        first_fibonacci = first_fibonacci+second_fibonacci
        second_fibonacci = temp

    else:
        temp = first_fibonacci
        first_fibonacci = first_fibonacci+second_fibonacci
        second_fibonacci = temp


