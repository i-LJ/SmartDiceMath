import random
from itertools import product
from decimal import Decimal, getcontext 
getcontext().prec = 40 # This only comes up when converting our large numbers
# more useful smaller numbers to avoid loss of accuracy.

def roll(dice):
    for j in range(quantity): # For as many times as we wanna roll dice
        dice.append(random.SystemRandom().randint(1,size)) # "Roll" a number between 1 and our die size
    for i in range (dtd): # After rolling our numbers
        dice.remove(min(dice)) # Remove as many of the lowest as specified
    return dice

def peel_and_drop(combo):
    sorted_combo = sorted(combo) # By sorting in an ascending order we can
    final_combo = sorted_combo[dtd:] # select the last elements after DTD 
    return final_combo # a.k.a. returning the highest quantity-dtd
    
size = 6 # Die size, or sides
quantity = 4 # How many dice we'll roll total
dtd = 1 # Dice to drop, we'll find the lowest and drop it from the list
###
po = pow(size,quantity) # Possible Outcomes counter
expectedAverage = 0
probability_Table = {}
###
temp = [list(range(1, size+1)) for _ in range(quantity)]

# Lets go over this as simply as possible
for combination in product(*temp): # We go through all possible combinations WITHOUT storing them
    fc = peel_and_drop(combination) # For the current combination being examined, drop the lowest DTD-amount of dice
    try: # If the sum of the combination exists in our dictionary, increment it by 1
        probability_Table[sum(fc)] += 1
    except KeyError: # If it doesn't exist in our dictionary, insert it in.
        probability_Table[sum(fc)] = 1 # Equals one means the first entry counts as an entry too

# For each of the possible outcomes in our table
for key in probability_Table:
    probability_Table[key] /= Decimal(po) # We convert the number of occurences into percent of occurences
    #print(str(key) + " * " + str(probability_Table[key]))    #Debugging
    expectedAverage += Decimal(key) * Decimal(probability_Table[key]) # This one is a statistics classic
    # The *expected outcome* is equal to the sum of the values multiplied by their probability to show up
    # i.e. if a key equaled to 10, and it had a 0.1 (10%) to occur, it'd add +1 to the expected total

print("# of dice:           " + str(quantity))
print("# of sides of dice:  " + str(size))
print("# of dice dropped:   " + str(dtd))
print("Statistical average: " + str(expectedAverage))
# print("1.0 means perfect accuracy, deviation is inaccuracy percentage: ", sum(probability_Table.values()))
###
"""
# Optional dice roller
reps = 10000 # Number of repetitions. More = Slower, but closer to statistical average
total = 0 # Initializing sum variable
i = 0 # Initializing iterators
j = 1
dice = [] # Temporary for each repetition

while i < reps:
    i += 1
    total += Decimal(sum(roll(dice))) # Roll our numbers, sum them up, and store them in our variable
    dice.clear() # We need to empty the "dice" array after each repetition

    # Optional in-line progress tracker
    #if i % 500000 == 0:
    #    print("Update: At " + str(i/1000) + "k")

average = Decimal(total)/reps
print("# of repetitions:    " + str(reps/1000000) + " mil")
print("Average of rolls:    " + str(average))
"""
