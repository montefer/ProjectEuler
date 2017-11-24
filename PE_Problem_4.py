#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

n = 100
largest_palindrome = 0

while n<1000:
    m = 100
    while m<1000:
        if  str(n*m)==str(n*m)[::-1]:
            if n*m > largest_palindrome:
                largest_palindrome = n*m
                m = m+1
                #print(largest_palindrome)
            m = m+1
        else:
            m = m+1
    n = n+1

print(largest_palindrome)