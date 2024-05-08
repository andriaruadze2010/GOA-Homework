

def basic_oper(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
       
        if value2 == 0:
            return "Error: Division by zero"
        else:
            return value1 / value2
    else:
        return "Error: Invalid operator"


print(basic_oper('-', 15, 18))  
print(basic_oper('*', 5, 5))   
print(basic_oper('/', 49, 7))


#2

def find_smallest_integer(arr):
    return min(arr)

print(find_smallest_integer([34, 15, 88, 2]))  
print(find_smallest_integer([34, -345, -1, 100]))


#3
def to_jaden_case(string):
    words = string.split()
    jaden_case_words = [word.capitalize() for word in words]
    return ' '.join(jaden_case_words)


quote = "How can  be real if our eyes aren't real"
print(to_jaden_case(quote))




#4


def solution(string, ending):
    return string.endswith(ending)

print(solution('abc', 'bc')) 
print(solution('abc', 'd'))  




#5
def solution(number):
    if number < 0:
        return 0
    
    sum_multiples = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
    
    return sum_multiples


print(solution(10))  
