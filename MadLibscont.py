import random

# We then print a random integer using the random.randint(start, end) function
print "Random number generated: " + str(random.randint(0,10))

# Remember that if we want to concatenate a string and a number, we need to convert the 
# integer into a string using the str() function

# We now want to create a list filled with random numbers. The list should be 
# of length 20



# Write code here and use a while loop to populate this list of random integers. A crucial
# function that will help you is to use the append() method to add elements to a list.

random_list = []
list_length = 20
count = 0

while count < list_length: #3
   random_list.append(random.randint(0,10)) #1, #2
   count += 1
print random_list

#1. Generate a random integer between 0 and 10
#2. Add this random integer to our list
#3. Do we have a list of length 20 yet?
#4. If not, we loop back up and go through steps 1 to 3 again while length of the list is less than 20

# Write code here to loop through the list and count all occurrences
# of the number 9. Note that `if` statements and `while` loops will help you solve
# this problem.

index = 0
count = 0

while index < len(random_list):
    count index == 9
index = index + 1


#1. Loop through each element in the list
#2. If the element is 9, we increase our count by 1
#3. Are we at the end of the list yet?
#4. If not, we loop back up and go through steps 1 to 3 again while we are still going through the list

while index < len(random_list):
      if random_list[index] == 9:
    count = count + 1
  index = index + 1

        




# Test: If the `while` loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
print random_list
print count
