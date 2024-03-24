budget = int(input("What is your budget: "))
cost = int(input("Please enter cost: "))

if budget >= cost:
    print("You have enough money")
else:
    print("You dont have enough money")






    
registered_password = "avtobusi"

password = input("Please enter your password: ")

while password != registered_password:
    password = input("Please enter your password again: ")
    if password == registered_password:
        print("You have accses on your account")
    else:
        print("wrong password, please try again")






        
start = int(input("Please enter starting value: "))
end = int(input("Please enter ending value: "))
step = int(input("Please enter step value: "))

for i in range(start,end,step):
    print(i)



    s1 = int(input("Please enter first side: "))
s2 = int(input("Please enter second side: "))
s3 = int(input("Please enter third side: "))


is_valid = (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)

while is_valid != True:
    s1 = int(input("Please enter first side: "))
    s2 = int(input("Please enter second side: "))
    s3 = int(input("Please enter third side: "))

    is_valid = s1 + s2 > s3






    operation = input("Please enter operation (+,-,*,/): ")
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("operation is not valid")