# s1
a=1234
th=(a//1000)%10 # Extract 4th digit from right
h=(a//100)%10 # Extract 3rd digit from right
t=(a//10)%10 # Extract 2nd digit from right
u=a%10# Extract 1st digit from right

reverse= u*1000 + t*100+h*10+th
print(reverse)


# s2
# palindrome


def Palindrome(num):
    
    h=(num//100)%10 # Extract 3rd digit from right
    t=(num//10)%10 # Extract 2nd digit from right
    u=num%10# Extract 1st digit from right

    reverse= u*100+ t*10 + h
    
    return num == reverse
    

print(Palindrome(121))