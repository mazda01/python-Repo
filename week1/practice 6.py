# 1. Create a tuple that contains two nested tuples, each with three elements.
# 2. Access the second element of the first nested tuple.
# 3. Access the first element of the second nested tuple.
# 4. Print both elements.

nested_tuple = (("bed",44,5.5),("bag",88,9.9))
print(nested_tuple)

second_element_first_nested=nested_tuple[0][1]
print(second_element_first_nested)

first_element_second_nested=nested_tuple[1][0]
print(first_element_second_nested)