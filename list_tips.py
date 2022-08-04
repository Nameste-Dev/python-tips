#Get all the elements in the middle of the list
first_element , *elements_in_the_middle, last_element = [1, 2, 3, 4, 5, 6, 7, 8]
print(i)  # [2, 3, 4, 5, 6, 7]


#Merge dictionaries in a single readable line
#This is available as of Python 3.9:

first_dictionary = {'name': 'Fatos', 'location': 'Munich'}
second_dictionary = {'name': 'Fatos', 'surname': 'Morina',
                     'location': 'Bavaria, Munich'}
result = first_dictionary | second_dictionary
print(result)  
# {'name': 'Fatos', 'location': 'Bavaria, Munich', 'surname': 'Morina'}

#merge dict
dictionary_one = {"a": 1, "b": 2}
dictionary_two = {"c": 3, "d": 4}

merged = {**dictionary_one, **dictionary_two}

print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


#22. You can separate big numbers with the underscore
print(1_000_000_000)  # 1000000000
print(1_234_567)  # 1234567

#30. Check whether a string is larger than another string
first = "abc"
second = "def"
print(first < second)  # True
second = "ab"
print(first < second)  # False


https://book.pythontips.com/en/latest/global_&_return.html#global-return

