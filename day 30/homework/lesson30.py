
#1

name = "andria ruadze"

reversed_word = name[::-1]
print(reversed_word.upper())

#2
def odd_even(strings):
    odd = []
    even = []

    for string in strings:
        odd_letters = ""
        even_letters = ""
        
        for i, letter in enumerate(string):
            if i % 2 == 0:
                even_letters += letter.upper()
            else:
                odd_letters += letter.upper()
        
        if len(string) % 2 == 0:
            even.append(even_letters)
            odd.append(odd_letters)
        else:
            even.append(odd_letters)
            odd.append(even_letters)
    
    print("Odd List:", odd)
    print("Even List:", even)

strings = ["vano", "nika", "bubazi", "zauri"]


odd_even(strings)

#3

def process_strings(strings):
    new_list = []
    small_list = []

    for string in strings:
        even_count = 0
        for char in string:
            if char.isalpha() and strings.index(string) % 2 == 0:
                even_count += 1

        if even_count % 2 == 0:
            new_list.append(string.upper())
        else:
            small_list.append(string[0].upper() + string[1:])
    
    print("Processed List:", new_list)
    print("Small List:", small_list)


strings = ["andria", "luka", "vano", "nika"]


process_strings(strings)


#4


def string_string(strings):
    new_list = []
    for string in strings:
        if string.isupper():
            new_list.append(string.lower())
        elif string.islower():
            new_list.append(string.upper())
    return new_list


strings = ["vano", "LUKA", "nika", "bubazi"]


string_string = string_string(strings)


print(string_string)

#5

def prc_string(input_string):
    index = input_string.find(' ')
    if index != -1:
        if index % 2 == 0:
            return input_string.upper()
        else:
            return input_string.capitalize()
    else:
        return "Space not found in the string."

input_string = "zdarova zma"

print(prc_string(input_string))

