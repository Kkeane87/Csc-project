names = ['kevin', 'eric', 'vin']

print(names[0])
print(names[1])
print(names[2])

names = ['kevin', 'eric', 'vin']

msg = "Hello, " + names[0].title() + "!"
print(msg)

msg = "Hello, " + names[1].title() + "!"
print(msg)

msg = "Hello, " + names[2].title() + "!"
print(msg)


guests = ['big tom', 'small fred', 'that man matt']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")


guests = ['big tom', 'small fred', 'that man matt']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[1])
guests.insert(1, 'Dane')

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")


guests = ['big tom', 'small fred', 'that man matt']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[1])
guests.insert(1, 'Dane')

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'vin')
guests.insert(2, 'eric')
guests.append('spike')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")


guests = ['big tom', 'small fred', 'that man matt']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[1])
guests.insert(1, 'Dane')


name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'jim')
guests.insert(2, 'dez')
guests.append('emily')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)


locations = ['himalaya', 'china', 'mexico', 'labrador', 'guam']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)


# Chapter 4

favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

for pizza in favorite_pizzas:
    print(pizza)

print("\n")

for pizza in favorite_pizzas:
    print("I really love " + pizza + " pizza!")

print("\nI really love pizza!")


numbers = list(range(1, 20))

for number in numbers:
    print(number)

numbers = list(range(1, 1000))

print(min(numbers))
print(max(numbers))
print(sum(numbers))


threes = list(range(3, 35, 3))

for number in threes:
    print(number)


cubes = []
for number in range(1, 21):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)


cubes = [number**3 for number in range(1,21)]

for cube in cubes:
    print(cube)


favorite_pizzas = ['pepperoni', 'cheese', 'sausage']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('cheese')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)


menu_items = (
    'ham sandwich', 'chicken nuggets', 'smoked salmon',
    'burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print("- " + item)

menu_items = (
    'ham sandwich', 'chicken nuggets', 'smoked salmon',
    'burger', ' crab cakes',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print("- " + item)

#Chapter 5

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")


alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")


alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")


age = 20

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")


favorite_fruits = ['blueberries', 'strawberries', 'peaches']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'cherry' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")


usernames = ['eric', 'kevin', 'vin', 'dan', 'tom']

for username in usernames:
    if username == 'kevin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")


usernames = []

if usernames:
    for username in usernames:
        if username == 'kevin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("create an account!")


current_users = ['eric', 'kevin', 'vin', 'dan', 'tom']
new_users = ['sarah', 'james', 'jim', 'john', 'bill']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")


numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")