import random
import time

answers = ["Yes", "No"]
while True:
    print("----------------------------------------------------------------------------------------")
    question = input("Which question do you want to prove with science? : ")
    if question == "":
        pass
    elif question == "d":
        print ("This 'random generator' is a scientific proofed answer.\nComputer Science is a science and this machine is build by computer science so it's a science")
    else:
        print ("Checking your question...")
        time.sleep(random.randint(0, 3))
        print()
        print ("The answer is: " + random.choice(answers))
