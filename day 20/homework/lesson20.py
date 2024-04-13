word = "andria"
reversed_word = ""

for index in range(len(word) - 1, -1, -1):
    reversed_word = reversed_word + word[index]

if word == reversed_word:
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")









numbers_list = []
repeat_value = []

for i in range(5):
    num = int(input("Please enter number: "))
    numbers_list.append(num)


for number in numbers_list:
    count = numbers_list.count(number)
    if count > 1 and number not in repeat_value:
        repeat_value.append(number)

print(repeat_value)

















words_list = []

for i in range(5):
    word = input("Please enter word: ")
    words_list.append(word)

result = ""

for word in words_list:
    result += word[0]

print(result)



list1 = [10,11,12,13,14,15,16,17,18,19,20]
list2 =[30,35,40,45,50]

print(list1 + list2)