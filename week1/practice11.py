# Create a dictionary with five key-value pairs representing different cities and their
# populations.
# Use the get method to access the population of a specific city.
# Use the pop method to remove a city from the dictionary.
# Print the final dictionary.
my_cities={
    "mumbai":12_691,
    "Delhi":10_972,
    "kolkata":4_631,
    "Hyderabad":3_719,
    "pune":2_935,


}
print(my_cities)

dic2=my_cities.get('Mumbai')
print(dic2)
my_cities.pop("delhi")
print(my_cities)
