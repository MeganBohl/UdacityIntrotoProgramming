"""
What To Do
We first need to understand that we still need to loop through all of the elements in count_list and simply print out the index and the value of the count_list in a specific format.

Let's see if we can write an outline of what to do if we were to do this manually on pen and paper:

Print the header "number | occurrence"
Loop through each element in the randomly generated list
Print the number of necessary spaces to get the right alignment we want
Get the current index and its associated value in our list
Print index and value in this format: "index | value"
Are we at the end of the loop?
If not, we loop back up and go through steps 1 to 5 again while we are still going through the list
Translation
Let's step through these steps and translate these steps into computer code.

1. Print the header "number | occurrence"
This is straight forward:

 print "number | occurrence"
2. Loop through each element in the randomly generated list. We therefore setup our loop structure.
index = 0

while index < len(random_list):
  # Put other code here
  index = index + 1
Please keep in mind how we are already adding index = index + 1 to the loop. This code is crucial to guarantee that the computer not step into an infinite loop. For most loops, we want to always clearly define a stopping point. In this case, the stopping point is when the number index is greater than the length of our list.

3. Print the number of necessary spaces to get the right alignment we want.
To do this dynamically we need to realize that we can calculate the number of white spaces needed to print before we print our index. If we want to print the string "0", we need to realize that we need to print 5 spaces before we print "0" in order to line up with the letter r in "number" in the header.

What happens if we decide to print the string "10?" We need to print 4 spaces because the characters "10" takes up 2 spaces. Regardless of the number, the total amount of spaces and characters should add up to 6, the length of the string "number".

Therefore in every loop, we dynamically calculate the number of spaces we need to print out depending on the length of the characters for each index:

num_spaces = len("number") - len(str(index))
Since len("number") never changes for each loop iteration, let's calculate and store the length of the string "number" outside the loop:

num_len = len("number")
while index < len(count_list):
  num_spaces = num_len - len(str(index))
4-5. Get the current index and its associated value in our list and print it out in the format we want. We convert our integers into string and use the "+" operator to concatenate our strings.
print " " * num_spaces + str(index) + " | " + str(count_list[index])
5: Are we at the end of loop? If not, we loop back up and go through the while loop instructions all over again.
Our loop construct already takes care of this criteria because at the top of our loop, we are always checking whether our index number is still less than the length of the random list: index < len(random_list)

We use the logic: if the index number is less than the length of our list, then we can safely say that whenever we access the list with index, we will never create an error and will be able access elements in the list with the number index.
"""
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1

print "number | occurrence"
index = 0
num_len = len("number")

while index < len(count_list):
  num_spaces = num_len - len(str(index))
  print " " * num_spaces + str(index) + " | " + str(count_list[index])
  index = index + 1