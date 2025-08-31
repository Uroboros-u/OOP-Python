"""TRY IT YOURSELF
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both meth-
ods for each user."""


# 9-1
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"This is {self.restaurant_name} restaurant. We have {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")


mamba = Restaurant("Mamba", "Ukrainian")

# mamba.open_restaurant()
# mamba.describe_restaurant()



#9-2
nika = Restaurant("Nika", "Italian")
protokol = Restaurant("Protokol", "Greek")

# mamba.describe_restaurant()
# nika.describe_restaurant()
# protokol.describe_restaurant()


class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex


    def describe_user(self):
        print(f"User name is {self.first_name} {self.last_name}.")
        print(f"Age: {self.age} years old.")
        print(f"Sex: {self.sex}.")


    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}.")

user1 = User('Ivan', 'Korba', 19, 'M')
user2 = User('Andrii', 'Manko', 25, 'M')
user3 = User('Anna', 'Lesiv', 20, 'W')


user1.describe_user()
user1.greet_user()
print('\n')
user2.describe_user()
user2.greet_user()
print('\n')
user3.describe_user()
user3.greet_user()
print('\n')