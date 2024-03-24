for i in range(0, 21):
 print(i)
 num1 = int(input("Enter number here: "))
 num2 = int(input("Enter number here: ")) 

 if num1>num2:
    for i  in range(num2 , num1):
        print(i)
if num2>num1:
    for i in range(num1 , num2): 
        print(i) 
else:
    print(num1, "=", num2)

for i in range(50 , 101):
    print(i)
for i in range(100, 49, -1):
    print(i)
sum=0
for i in range(0 ,51):
    print(i)
    sum= sum + i
    print(sum)

sum=0
for i in range(1, 6):
    print(i)
    sum+1
    print(sum)




    user_num = int(input("Enter number: "))
    for i in range(0, user_num):
        print(i)
user_age = int(input("Enter your age: "))
second_age = user_age + 10

for i in range(user_age+1, second_age):

    print(i)

