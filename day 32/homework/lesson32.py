def manual_index(numbers_list, search_value):
   
   
    for index, value in enumerate(numbers_list): #გადავლა 
        if value == search_value:  #თუ ეს მნიშვნელობა არის
            return index  #დააბრუნე ინდექსი
    return -1  #თუ არ არის დააბრუნე -1


numbers = [1, 3, 7, 9, 6] 
search_value = 6 
print(manual_index(numbers, search_value)) 

#2

def manual_max(numbers_list):
   
    max_value = numbers_list[0]  # დავარქვათ მაქსიმუმი
    for number in numbers_list[1:]:  #გადავუართ ციკლით
        if number > max_value:  # თუ რიცხვი მეტია მაქსიმუმზე
            max_value = number  # მაქსიმუმი განახლდება

    return max_value  # დააბრუნე მაქსიმუმი

def manual_min(numbers_list):
   
    min_value = numbers_list[0] 
    for number in numbers_list[1:]:  
        if number < min_value:  
            min_value = number 

    return min_value  # დააბრუნე მინიმუმი

numbers = [5, 3, 9, 1, 7]
print("Max:", manual_max(numbers)) 
print("Min:", manual_min(numbers))
#3


def manual_pop(lst, index):
    
    # შევამოწმოთ, რომ index-ის მნიშვნელობა სწორია
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range")

    # წავშალოთ ელემენტი მითითებულ ინდექსზე
    popped_element = lst.pop(index)

    return lst  # დააბრუნებს ახალ სიას

# მაგალითის გასაშვებად
my_list = [1, 2, 3, 4, 5]
index_to_pop = 2
new_list = manual_pop(my_list, index_to_pop)
print("ახალი სია:", new_list)  

