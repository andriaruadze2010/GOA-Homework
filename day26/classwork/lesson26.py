def numbers(start, end):
    for i in range(start, end):
        print(i)


numbers(1,8)
numbers(5, 10)

def calculate_sum(start, end):
    result = 0
    for i in range(start, end):
        result = result + i
    print(result)


calculate_sum(2,5)


def calculate_arithmetic(start, end):
    numbers = []

    for i in range(start, end):
        numbers.append(i)
    
    result = sum(numbers) / len(numbers)

    print(result)

calculate_arithmetic(5, 11)




def print_char(name, index):
    print(name[index])

print_char("Luka", 3)

#დავალება6: შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვი. საბოლოოდ ფუნქციამ უნდა დააბრუნოს ამ ორი რიცხვის ჯამი, ფუნქციის გარეთ დაბეჭდეთ ეს შედეგ
def sum_of_numbers(numbers_list):
    total = 0
    
    for i in numbers_list:
        total = total + i
        
    return total
    
var1 = sum_of_numbers([1, 2, 3, 4, 5])
print(var1)

var2 = sum_of_numbers([6, 7, 8, 9, 10])
print(var2)