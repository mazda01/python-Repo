# 1. Create a list of the first 10 square numbers.
            # Example: square number means [1,4,9,……..]
# 2. Replace the third element with 50.
# 3. Insert a new element 25 at the fifth position.
# 4. Remove the last element from the list.
# 5. Print the final list.

Square_numbers=[a**2 for a in range(1,11)]
print(Square_numbers)


#Replace the third element with 50
Square_numbers[2]=50
print(Square_numbers)


#insert a new element 25 at the fifth position.
Square_numbers.insert(4,25)
print(Square_numbers)


#Remove the last element from the list
Square_numbers.pop()
print(Square_numbers)