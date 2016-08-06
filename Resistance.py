import random
class People:
    def __init__(self, name):
        self.name = name     
    def getName(self):
        return self.name
class cp:
    def __init__(self, name):
        self.name = name
        self.side = 'Resistance'
    def getName(self):
        return self.name
    def setSide(self,side):
        self.side=side
    def getSide(self):
        return self.side
    def equals(self, name):
        if(self.name == name):
            return true
        else:
            return false
def printSides(players):
    for comp in players:
        print(comp.getName() + ": " + comp.getSide())
spy1 = random.randint(0,8)
spy2 = random.randint(0,8)
while (spy2 == spy1):
    spy2 = random.randint(0,8)
spy3 = random.randint(0,8)
while (spy3 == spy1 or spy3 == spy2):
    spy3 = random.randint(0,8)
spy4 = random.randint(0,8)
while (spy4 == spy1 or spy4 == spy2 or spy4 == spy3):
    spy4 = random.randint(0,8)
cp1 = cp('cp1')
cp2 = cp('cp2')
cp3 = cp('cp3')
cp4 = cp('cp4')
cp5 = cp('cp5')
cp6 = cp('cp6')
cp7 = cp('cp7')
cp8 = cp('cp8')
cp9 = cp('cp9')
players = [cp1,cp2,cp3,cp4,cp5,cp6,cp7,cp8,cp9]
players[spy1].setSide('Spy')
players[spy2].setSide('Spy')
players[spy3].setSide('Spy')
players[spy4].setSide('Spy')
name=input("Welcome to Resistance! What is your name? ")
player = People(name)
choice1 = input("Hello " + player.getName() + "! Lets begin. Choose Two Players: cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9 ")
choice2 = input()
count = 0
wins = 0
loses = 0
for comp in players:
    if(comp.getName() == choice1):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice2):
        if(comp.getSide() == "Spy"):
            count = count + 1
if(count > 0):
    print("Mission Failed By: " + str(count) + " Spies")
    loses = loses + 1
else:
    print("Mission Successful!")
    wins = wins + 1
choice1 = input("Choose Three Players: cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9 ")
choice2 = input()
choice3 = input()
count = 0
for comp in players:
    if(comp.getName() == choice1):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice2):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice3):
        if(comp.getSide() == "Spy"):
            count = count + 1
if(count > 0):
    print("Mission Failed By: " + str(count) + " Spies")
    loses = loses + 1
else:
    print("Mission Successful!")
    wins = wins + 1
choice1 = input("Choose Three Players: cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9 ")
choice2 = input()
choice3 = input()
count = 0
for comp in players:
    if(comp.getName() == choice1):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice2):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice3):
        if(comp.getSide() == "Spy"):
            count = count + 1
if(count > 0):
    print("Mission Failed By: " + str(count) + " Spies")
    loses = loses + 1
else:
    print("Mission Successful!")
    wins = wins + 1
if(loses == 3):
    print("Three missions have failed. Spies Win!")
    printSides(players)
    input()
    sys.exit
elif(wins == 3):
    print("Three missions have passed. Resistance Wins!")
    printSides(players)
    input()
    sys.exit
choice1 = input("Choose Four Players: cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9 ")
choice2 = input()
choice3 = input()
choice4 = input()
count = 0
for comp in players:
    if(comp.getName() == choice1):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice2):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice3):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice4):
        if(comp.getSide() == "Spy"):
            count = count + 1        
if(count > 1):
    print("Mission Failed By: " + str(count) + " Spies")
    loses = loses + 1
elif(count == 1):
    print("Mission Successful! Although there was 1 spy in the previous mission.")
else:
    print("Mission Successful!")
    wins = wins + 1
if(loses == 3):
    print("Three missions have failed. Spies Win!")
    printSides(players)
    input()
    sys.exit
elif(wins == 3):
    print("Three missions have passed. Resistance Wins!")
    printSides(players)
    input()
    sys.exit
choice1 = input("Choose Four Players: cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9 ")
choice2 = input()
choice3 = input()
choice4 = input()
count = 0
for comp in players:
    if(comp.getName() == choice1):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice2):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice3):
        if(comp.getSide() == "Spy"):
            count = count + 1
    elif(comp.getName() == choice4):
        if(comp.getSide() == "Spy"):
            count = count + 1        
if(count > 0):
    print("Mission Failed By: " + str(count) + " Spies")
    loses = loses + 1
else:
    print("Mission Successful!")
    wins = wins + 1
if(loses == 3):
    print("Three missions have failed. Spies Win!")
    printSides(players)
    input()
    sys.exit
elif(wins == 3):
    print("Three missions have passed. Resistance Wins!")
    printSides(players)
    input()
    sys.exit
input()



    
