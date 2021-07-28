# author:
# date:

from random import randint

# -------------------- Section 1 ------------------------- #
# ------------------ List Creation ----------------------- #

print('# -------------------- Section 1 ------------------------- #')
print('Creating an Empty List' '\n')
# 1. Creating an Empty List
# --------------------------------------------------------
# Instructions
#   1. Create empty lists using the following methods.
#       a. via List Displays
#       b. via the list() function.
#   2. Print the lists.
#
# WRITE CODE BELOW
list1 = []
list2 = list()

print(
    f'list1 / {list1}' '\n'
    f'list2 / {list2}'
)

print('\n' 'Creating a Pre-Populated List' '\n')
# 2. Creating a Pre-Populated List
# ------------------------------------------------------------
# Instructions
#   1. Create the following pre-populated lists:
#       a. A list filled with 5 integers.
#       b. A list filled with 5 floats.
#       c. A list filled with 3 boolean values (True / False)
#       d. A list of three animals
#       e. A list with of 3 objects, that are all different data types.
#       f. Convert the string of the name of a star to a list via the list() function.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers = [1, 15, -4, -26, 34]
floats = [2.4, -0.442, 4.93, 3.3224, 8.431]
booleans = [True, False, True]
animals = ['pangolin', 'red panda', 'bat-eared fox']
objects = ['seal', 45, False]
chars = list('this text will be converted to a list!')

print(
    f'integers / {integers}' '\n'
    f'floats   / {floats}' '\n'
    f'booleans / {booleans}' '\n'
    f'animals  / {animals}' '\n'
    f'objects  / {objects}' '\n'
    f'chars    / {chars}'
)

# -------------------- Section 2 ------------------------- #
# ---------------- List Modification --------------------- #
print('\n' '# -------------------- Section 2 ------------------------- #')
print('Accessing and Modifying a List' '\n')
# 1. Accessing and Modifying a List
# ------------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Replace the item at position 2 with a new number.
#       b. Floats --> Replace the item at position 4 with a new number.
#       c. Booleans --> Replace the item at position 0 with itself negated. (not)
#       d. Animals --> Replace one of the animals with a new animal.
#       e. Objects --> Replace one of the items within the list with a new one.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers[2] = 44
floats[4] = .543657
booleans[0] = not booleans[0]
animals[0] = 'ferrets'
objects[2] = 'cat'

print(
    f'integers / {integers}' '\n'
    f'floats   / {floats}' '\n'
    f'booleans / {booleans}' '\n'
    f'animals  / {animals}' '\n'
    f'objects  / {objects}'
)

print('\n' 'Append, Insert, and Remove' '\n')
# 2. Accessing and Modifying a List
# ------------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Append a new number to the list.
#       b. Floats --> Append a new float to the list.
#       c. Booleans --> Remove one of the items from the list
#       d. Animals --> Insert a new animal at the beginning of the list.
#       e. Objects --> Insert a new object at the middle of the list.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers.append(25)
floats.append(7.554431)
booleans.remove(False)
animals.insert(0, 'pangolin')
objects.insert((len(objects) - 1) // 2, False)

print(
    f'integers / {integers}' '\n'
    f'floats   / {floats}' '\n'
    f'booleans / {booleans}' '\n'
    f'animals  / {animals}' '\n'
    f'objects  / {objects}'
)

print('\n' 'List Concatenation' '\n')
# 3. List Concatenation
# ------------------------------------------------------------
#
# Lists like Strings can Concatenate with other Lists using the + operator. They can also be duplicated by
#   multiplying the list.
#
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Concatenate the lists holding the integers and floats together, and save the result to a new variable.
#       d. Duplicate the list holding animals 3 times, and save the result to a new variable.
#   2. Print the new lists.
#
#   Examples are below for reference
#
# WRITE CODE BELOW
example_concatenation = [1, 2, 3] + ['cat', 'dog']
example_duplication = ['cat'] * 5
print(
    '\n'
    f'example_concatenation | {example_concatenation}' '\n'
    f'example_duplication  | {example_duplication}' '\n'
)
nums = integers + floats
animals2 = animals * 3

print(
    f'nums    | {nums}' '\n'
    f'animals | {animals2}'
)


# -------------------- Section 3 ------------------------- #
# --------------------- Looping -------------------------- #
print('\n' '# -------------------- Section 3 ------------------------- #')
print('Looping' '\n')
# 1. Looping
# ------------------------------------------------------------
# Instructions
#   1. Create a loop that prints out the contents of the two of the lists you have already created, using the
#       methods below.
#       a. via in range()
#       b. via direct access
#
#   An example has been shown below:
#
# WRITE CODE BELOW
print('via in range(len(animals))')
for i in range(len(animals)):
    print(animals[i])

print()

print('for num in nums')
for num in nums:
    print(num)

# -------------------- Section 4 ------------------------- #
# ------------------ Comprehension ----------------------- #
print('\n' '# -------------------- Section 3 ------------------------- #')
print('Dice - Statistics' '\n')

# 1. Dice - Statistics
# ------------------------------------------------------------
# Preface
#   When we roll a dice, the side it lands on is random. However, since a dice has multiple sides that are equivalent
#       in chance of falling, then we say a side has a 1/6 chance of happening, or 16.7% chance. Lets test to see if
#       that's true!
#
# 1. Create multiple for loops to run 5, 10, 100, and 1000 times.
#   a. Within the loops, roll a dice and append the roll to a list that is keeping track of all the rolls.
# 2. After the loop has finished rolling, print the number of times each face appeared, as well as the rate of
#   rate of appearance.
#
# The beginning of the loop running 5 times has been done for you. Be sure to finish it.
#
# WRITE CODE BELOW


def print_rolls(rolls_, size_):
    print(f'rolls | {rolls_}')
    print(f'size  | {size_}')
    print(f'1     | total - {rolls_.count(1)}\t\t| rate of appearance - {"{:.2%}".format(rolls_.count(1) / size_)}')
    print(f'2     | total - {rolls_.count(2)}\t\t| rate of appearance - {"{:.2%}".format(rolls_.count(2) / size_)}')
    print(f'3     | total - {rolls_.count(3)}\t\t| rate of appearance - {"{:.2%}".format(rolls_.count(3) / size_)}')
    print(f'4     | total - {rolls_.count(4)}\t\t| rate of appearance - {"{:.2%}".format(rolls_.count(4) / size_)}')
    print(f'5     | total - {rolls_.count(5)}\t\t| rate of appearance - {"{:.2%}".format(rolls_.count(5) / size_)}')
    print(f'6     | total - {rolls_.count(6)}\t\t| rate of appearance - {"{:.2%}".format(rolls_.count(6) / size_)}')
    print()


def roll_dice(rolls_, num_rolls):
    for i in range(size):
        rolls.append(randint(1, 6))


for size in [5, 10, 100, 1000]:
    rolls = []
    roll_dice(rolls, size)
    print_rolls(rolls, size)
