#This program is a conditon program
temp = 0
temp = int(input("Please enter the current temperature:"))

if temp > 90:
    print ("Wear Shorts!")
elif 70 <= temp:
    print ("Short sleeves are fine.")
elif 50 <= temp:
    print ("Wear a jacket")
elif 32 <= temp:
    print ("Wear a heavy coat")
elif 32 >= temp:
    print ("Stay inside")


    
