#Score average prgram with while loop
average = 0
total = 0
howManyEntered = 0
howMany = int(input("How many test scores would you like to average?"))
while howManyEntered < howMany:
    testscore = int(input("Enter test score:"))
    total = total + testscore
    howManyEntered = howManyEntered + 1
average = total / howMany
print ("The average for the test scores you entered is:",average)









