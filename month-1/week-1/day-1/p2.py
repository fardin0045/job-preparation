# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))

# print(num1,num2)
# temp=num1
# num1=num2
# num2=temp

# print(num1,num2)

# if(num1%2==0):
#     print("even")
# else:
#     print("odd")

def convert(seconds):
    days= seconds//86400
    hour = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds %= 60
    
    print(f"{days} days, {hour} hour, {minutes} minutes, {seconds} seconds")

# Driver program
n = 1234522
print(convert(n))
print(17 / 4)
print(17 // 4)
print(17 % 4) 
print(-17 // 4)


def convert_time(seconds):
    days = seconds // 86400
    seconds %= 86400

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60

    return days, hours, minutes, seconds


total_seconds = int(input("Enter total seconds: "))

if total_seconds >= 0:
    days, hours, minutes, seconds = convert_time(total_seconds)

    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
else:
    print("Please enter a nonnegative integer.")
