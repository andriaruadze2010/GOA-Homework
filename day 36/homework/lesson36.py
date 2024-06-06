def initials(name):
   
    first_name, last_name = name.split()
    
    
    initial1 = first_name[0].upper()
    initial2 = last_name[0].upper()
    

    return initial1 + '.' + initial2


print(initials("andria ruadze"))
 


def sum_array_values(arr):
    total = 0
    for element in arr:
        total += float(element)
    return total


array = ['1', 2, '3', '3.5', '4.5']
result = sum_array_values(array)
print(result)  




def find_smallest_integer(arr):
    
    if not arr:
        return None
    
    
    smallest = arr[0]
    
    
    for num in arr:
        if num < smallest:
            smallest = num
    
    return smallest


array1 = [12, 15, 78, 2]
array2 = [34, -333, -10, 100]

print(find_smallest_integer(array1))  
print(find_smallest_integer(array2))  






def count_sheep(num):
    murmur = ""
    for i in range(1, num + 1):
        murmur += str(i) + " sheep..."
    return murmur


print(count_sheep(5))





def sum_of_arrays(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    total_sum = sum1 + sum2
    return total_sum


array1 = [2, 3, 4]
array2 = [5, 6, 7]
result = sum_of_arrays(array1, array2)
print(result)  
