"""
Given a list of numbers and a number k, return whether any two
numbers from the list add up to k.

For example, given [10,15,3,7] and k of 17, return true
since 10 + 7 = 17
"""


#Used given list, but can be done by getting user input for list of numbers
#and number for k

numbs = [10,15,3,7]
k=17

for i in range (0, len(numbs)):

    for x in range (i+1, len(numbs)):

        if numbs[i] + numbs[x] == k:
            print ("True: " + str(numbs[i]) + " + " + str(numbs[x]) )









