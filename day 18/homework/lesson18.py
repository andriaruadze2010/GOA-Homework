list = ["andria", "gabrieli", "ilia", "luka", "nika"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])


name = ["andria", "gabrieli", "ilia", "luka", "nika"]

for name in name:
    print(name)



numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 == 0:
        print(number)





numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

sum = 0
multiple = 1

for num in numbers:
    sum = sum + num
    multiple = multiple * num
    print(numbers,sum)
    print(numbers,  multiple)
    





















numbers = [1,2,3,4,5,6,7,8,9,10]

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num
        print(num)
        


print(even_sum)














numbers = [1,2,3,4,5,6,7,8,9,10]

odd_sum = 0
odd_multiple = 1

for num in numbers:
    if num % 2 != 0:
        odd_sum = odd_sum + num
        odd_multiple = odd_multiple * num

print(odd_sum)
print(odd_multiple)





name = "gabrieli"

for char in name:
    print(char)
