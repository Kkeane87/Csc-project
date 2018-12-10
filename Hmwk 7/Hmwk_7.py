class Restaurant():

    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):

        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('good eats pizza','pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


class Restaurant():

    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):

        msg = self.name + " is open. Come on in!"
        print("\n" + msg)


mean_queen = Restaurant('mcdonalds', 'burgers')
mean_queen.describe_restaurant()

ludvigs = Restaurant("dominoes", 'pizza')
ludvigs.describe_restaurant()

mango_thai = Restaurant('wendys', 'fast food')
mango_thai.describe_restaurant()


class User():

    def __init__(self, first_name, last_name, username, email, location):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):

        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):

        print("\nWelcome back, " + self.username + "!")

kevin = User('kevin', 'keane', 'k keane', 'kkeane87@example.com', 'illinois')
kevin.describe_user()
kevin.greet_user()

eric = User('eric', 'keane', 'e keane', 'erickeane30@example.com', 'illinois')
eric.describe_user()
eric.greet_user()


class Restaurant():

    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):

        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):

        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):

        self.number_served = number_served

    def increment_number_served(self, additional_served):

        self.number_served += additional_served


restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 13
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(41)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(58)
print("Number served: " + str(restaurant.number_served))


class User():

    def __init__(self, first_name, last_name, username, email, location):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):

        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):

        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0


kevin = User('kevin', 'keane', 'k keane', 'kkeane01@example.com', 'illinois')
kevin.describe_user()
kevin.greet_user()

print("\nMaking 3 login attempts...")
kevin.increment_login_attempts()
kevin.increment_login_attempts()
kevin.increment_login_attempts()
print("  Login attempts: " + str(kevin.login_attempts))

print("Resetting login attempts...")
kevin.reset_login_attempts()
print("  Login attempts: " + str(kevin.login_attempts))


class Restaurant():

    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):

        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):

        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):

        self.number_served = number_served

    def increment_number_served(self, additional_served):

        self.number_served += additional_served


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):

        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):

        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('Better Ice Cream')
big_one.flavors = ['vanilla', 'chocolate', 'strawberry']

big_one.describe_restaurant()
big_one.show_flavors()


class User():

    def __init__(self, first_name, last_name, username, email, location):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):

        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):

        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):

        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):

        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)


kevin = Admin('kevin', 'keane', 'k keane', 'kkeane@example.com', 'illinois')
kevin.describe_user()

kevin.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

kevin.show_privileges()


class User():

    def __init__(self, first_name, last_name, username, email, location):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):

        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):

        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):

        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()

class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


kevin = Admin('kevin', 'keane', 'kkeane17', 'kkeane@example.com', 'illinois')
kevin.describe_user()

kevin.privileges.show_privileges()

print("\nAdding privileges...")
kevin_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
kevin.privileges.privileges = kevin_privileges
kevin.privileges.show_privileges()


class Car():

    def __init__(self, manufacturer, model, year):

        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):

        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):

        self.odometer_reading += miles


class Battery():

    def __init__(self, battery_size=60):

        self.battery_size = battery_size

    def describe_battery(self):

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):

        if self.battery_size == 50:
            range = 140
        elif self.battery_size == 75:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):

        if self.battery_size == 50:
            self.battery_size = 75
            print("Upgraded the battery to 75 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):

        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2018)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()


class Restaurant():

    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):

        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served

        channel_club = Restaurant('mcdonalds', 'burgers')
        channel_club.describe_restaurant()
        channel_club.open_restaurant()


"""A collection of classes for modeling users."""


class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges([])


class Privileges():
    """Stores privileges associated with an Admin account."""

    def __init__(self, privileges):
        """Initialize the privileges object."""
        self.privilege = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        for privilege in self.privileges:
            print("- " + privilege)


kevin = Admin('kevin', 'keane', 'kkeane', 'kkeane@example.com', 'illinois')
kevin.describe_user()

frank_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
kevin.privileges.privileges = kevin_privileges

print("\nThe admin " + kevin.username + " has these privileges: ")
kevin.privileges.show_privileges()


class User():

    def __init__(self, first_name, last_name, username, email, location):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0



"""A collection of classes for modeling an admin user account."""



class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges([])


class Privileges():
    """Stores privileges associated with an Admin account."""

    def __init__(self, privileges):
        """Initialize the privileges object."""
        self.privilege = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        for privilege in self.privileges:
            print("- " + privilege)

kevin = Admin('kevin', 'keane', 'kkeane', 'kkeane@example.com', 'illinois')
kevin.describe_user()

kevin_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
kevin.privileges.show_privileges

print("\nThe admin " + kevin.username + " has these privileges: ")
kevin.privileges = kevin_privileges

from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

from random import randint


class Die():

    def __init__(self, sides=6):

        self.sides = sides

    def roll_die(self):

        return randint(1, self.sides)


d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)