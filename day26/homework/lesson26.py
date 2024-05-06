def sum(nums):
    total = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            total += nums[i]
    return total
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum(numbers)
print(result)

                







def check_even_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

number = int(input("please enter a number: "))
result = check_even_odd(number)
print(f"{number} {result}.")





def capitalize_names(names):
    capitalized_names = [name.capitalize() for name in names]
    return capitalized_names


names =["andria", "gabrieli","elene","eto","ilia"]
updated_names = capitalize_names(names)
print("updated names:", updated_names)










def list(numbers):
    updated_list = []
    for num in numbers:
        if num % 2 == 0:
            updated_list.append(num * 2)
        else:
            updated_list.append(num ** 2)
    return updated_list

numbers = [1, 2, 3, 4, 5]
modified_numbers = list(numbers)
print("updated list:", modified_numbers)