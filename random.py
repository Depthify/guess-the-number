import random

print("Available levels: ")
print("1. Easy (1, 10)\n2. Medium (1, 25)\n3. Hard (1, 50)\n4. Mega (1, 75)\n5. Extreme (1, 100)")
print("Please choose a level from the options above (1/2/3/4/5)")
lvl_c = input(">>> ")
lvl_c = int(lvl_c)

def easy():
    pc_c = random.randint(1, 10)
    pc_c = int(pc_c)
    
    print("Can you guess the number between 1 & 10? 🤔")
    guess = input(">>> ")
    guess = int(guess)

    if guess == pc_c:
        print("Congratulations! You've guessed it correctly!")
        print("You:", guess,"Me:", pc_c)
    if guess != pc_c:
        print("You've guessed it incorrect")
        print("You:", guess,"Me:", pc_c)

def medium():
    pc_c = random.randint(1, 25)
    pc_c = int(pc_c)
    
    print("Can you guess the number between 1 & 25? 🤔")
    guess = input(">>> ")
    guess = int(guess)

    if guess == pc_c:
        print("Congratulations! You've guessed it correctly!")
        print("You:", guess,"Me:", pc_c)
    if guess != pc_c:
        print("You've guessed it incorrect")
        print("You:", guess,"Me:", pc_c)

def hard():
    pc_c = random.randint(1, 50)
    pc_c = int(pc_c)
    
    print("Can you guess the number between 1 & 50? 🤔")
    guess = input(">>> ")
    guess = int(guess)

    if guess == pc_c:
        print("Congratulations! You've guessed it correctly!")
        print("You:", guess,"Me:", pc_c)
    if guess != pc_c:
        print("You've guessed it incorrect")
        print("You:", guess,"Me:", pc_c)

def mega():
    pc_c = random.randint(1, 75)
    pc_c = int(pc_c)
    
    print("Can you guess the number between 1 & 75? 🤔")
    guess = input(">>> ")
    guess = int(guess)

    if guess == pc_c:
        print("Congratulations! You've guessed it correctly!")
        print("You:", guess,"Me:", pc_c)
    if guess != pc_c:
        print("You've guessed it incorrect")
        print("You:", guess,"Me:", pc_c)

def extreme():
    pc_c = random.randint(1, 100)
    pc_c = int(pc_c)
    
    print("Can you guess the number between 1 & 100? 🤔")
    guess = input(">>> ")
    guess = int(guess)

    if guess == pc_c:
        print("Congratulations! You've guessed it correctly!")
        print("You:", guess,"Me:", pc_c)
    if guess != pc_c:
        print("You've guessed it incorrect")
        print("You:", guess,"Me:", pc_c)

if lvl_c == 1:
    easy()
if lvl_c == 2:
    medium()
if lvl_c == 3:
    hard()
if lvl_c == 4:
    mega()
if lvl_c == 5:
    extreme()
else:
    print("Invalid Input")