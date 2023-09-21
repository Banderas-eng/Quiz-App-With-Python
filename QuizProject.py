#title
print("Mathematics Quiz")

# loop to verify if person has input their name
while True:
    name = input("Enter your name: ")
    if name != '':
        print(f'{name}')
        break    

# check if person wants to start the quiz
quiz = input("Do you want to start quiz? (y/n): ")
if quiz != "y":
    quit()
print("Start quiz")

score = 0

# quiz questions
question1 = input(
    "Clara bought a necklace for $5 and a bracelet for $7 at a clearance sale. How much money did she spend in all? "
)
if question1.lower() == "$12":
    print("Correct")
    score += 1 #score increases by 1 when question aswered correctly
else:
    print("Try again")

question2 = input(
    "Anna bought two buckets. One bucket can hold 6 gallons of water, and the other can hold 8 gallons. How many gallons of water can both the buckets hold together? "
)
if question2.lower() == "14 gallons":
    print("Correct")
    score += 1
else:
    print("Try again")

question3 = input(
    "Megan picked two cabbages and three cauli!owers from her kitchen garden. How many vegetablesdid she pick in all? "
)
if question3.lower() == "5 vegetables":
    print("Correct")
    score += 1
else:
    print("Try again")

question4 = input(
    "Six Blue Jays are perched on an Oak tree. Moments later, 5 more Blue Jays !y in. How many birds are perched on the tree altogether? "
)
if question4.lower() == "11 blue jays":
    print("Correct")
    score += 1
else:
    print("Try again")

question5 = input(
    "A box contains 9 bars of white chocolate and 9 bars of dark chocolate. How many bars of chocolate does the box have in total? "
)
if question5.lower() == "18 bars of chocolate":
    print("Correct")
    score += 1
else:
    print("Try again")

question6 = input(
    "What is the area of a rectangle with side lengths 3 inches by 5 inches? "
)
if question6.lower() == "15 square inches":
    print("Correct")
    score += 1
else:
    print("Try again")

question7 = input(
    "Area of triangle of height 7cm and base 8cm? "
)
if question7.lower() == "28cm^2":
    print("Correct")
    score += 1
else:
    print("Try again")    

question8 = input(
    "A CD contains 4 music tracks. How many music tracks would 8 such CDs contain? "
)
if question8.lower() == "32 music tracks":
    print("Correct")
    score += 1
else:
    print("Try again")

question9 = input(
    "Cheryl, a grade 1 teacher, distributes 36 pencils equally among nine children in her class. How many pencils will each child receive? "
)
if question9.lower() == "4 pencils":
    print("Correct")
    score += 1
else:
    print("Try again")

question10 = input(
    "Juliet has 38 candy bars which she splits equally among 3 of her cousins. How many candy bars does each of Juliet’s cousins get? "
)
if question10.lower() == "12 candy bars":
    print("Correct")
    score += 1
else:
    print("Try again")

print("Final score " + str(score) + "/10")
if score < 5:
    print("CAN DO BETTER")
elif score == 5 or score == 6:
    print("Courage")
elif score == 7 or score == 8:
    print("Very Good")
else:
    print("Excellent Keep Up")                    