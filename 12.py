#Argument Unpacking with * and
def describe_pet(name, species, age):
    print(f"{name} is a {age}-year-old {species}.")

# Unpacking a dictionary into the function
pet_data = {"name": "Luna", "species": "Cat", "age": 3}
describe_pet(**pet_data) 

# Unpacking a list
more_data = ["Rex", "Dog", 5]
describe_pet(*more_data)