# s1
a=583

h=a//100
t=(a//10)%10
u=a%10

print(h,t,u)

# s2
b=3434

print(*str(b))

#s3
a=583
digits = []

while a > 0:
    digits.append(a % 10)
    a = a // 10

print(digits)
print(*digits[::-1])
