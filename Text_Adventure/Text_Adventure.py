import random
import time
import math
from pprint import pprint


class hero:
    def __init__(self, Hhealth, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hname):
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defence = Hdefence
        self.magic = Hmagic
        self.name = Hname

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getLuck(self):
        return self.luck
    def getRanged(self):
        return self.ranged
    def getDefence(self):
        return self.defence
    def getMagic(self):
        return self.magic
    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack    
    def setLuck(self, newLuck):
        self.luck = newLuck
    def setRanged(self, newRanged):
        self.ranged = newRanged
    def setDefence(self, newDefence):
        self.defence = newDefence   
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setName(self, newName):
        self.name = newName

class enemy:
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename):
        self.health = Ehealth
        self.attack = Eattack
        self.special = Especial
        self.chance = Echance
        self.name = Ename

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getSpecial(self):
        return self.special
    def getChance(self):
        return self.chance
    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setSpecial(self, newSpecial):
        self.special = newSpecial
    def setChance(self, newChance):
        self.chance = newChance
    def setName(self, newName):
        self.name = newName

class boss (enemy):
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename, EsuperMove):
        super().__init__(Ehealth, Eattack, Especial, Echance, Ename)

        self.superMove = EsuperMove

    def getSuper(self):
        return self.superMove

    def setSuper(self, newSuperMove):
        self.superMove = newSuperMove

def createClass():
    a = input('Are you more of a stratagist (1) or a warrior (2)? ')
    while a != "1" and a != "2":
        print("Invalid Selection")
        a = input('Are you more of a stratagist (1) or a warrior (2)? ')

    if a == '1':
        heroAttack = 10
        heroDefence = 20

    elif a == '2':
        heroAttack = 20
        heroDefence = 10

    b = input("Press enter to roll the dice to test your luck...")
    time.sleep(0.2)
    print('Rolling dice....')
    heroLuck = random.randint(1,10)
    print(f'Your hero has {heroLuck} out of 10 luck.')

    c = input("Are you more an archer (1) or a magic user (2)? ")
    while c != '1' and c != '2':
        print("Invalid Selection")
        c = input("Are you more an archer (1) or a magic user (2)? ")

    if c == "1":
        heroRanged = 20
        heroMagic = 10

    elif c == "2":
        heroRanged = 10
        heroMagic = 20

    heroName = input("What is your name hero? ")
    print(f"Welcome {heroName}!")

    return(heroAttack, heroLuck, heroRanged, heroDefence, heroMagic, heroName)

def enemyGen(levelBoss):
    temp = []
    file = open("Adjectives.txt","r")
    lines = file.readlines()
    adjective = lines[random.randint(0,len(lines)-1)][:-2]
    file.close
    file = open("Animals.txt","r")
    lines = file.readlines()
    animal = lines[random.randint(0,len(lines)-1)][:-2]
    file.close

    if levelBoss == False:
        health = random.randint(50,100)
        attack = random.randint(10,15)
        special = random.randint(10,20)
        chance = random.randint(1,10)
    
        return enemy(health, attack, special, chance, adjective+" "+animal)

    else:
        health = random.randint(200,250)
        attack = random.randint(20,40)
        special = random.randint(50,60)
        chance = random.randint(1,8)
        superMove = random.randint(100,200)

        return boss(health, attack, special, chance, adjective+" "+animal, superMove)

def enemyAttack(hitChance, attackValue, name, defence):
    print(f"{name} is preparing to attack...")
    hit = random.randint(0,10)
    if hitChance >= hit:
        print('They strike the hero!')
        loss = attackValue - defence
        loss = abs(loss)
        print(f"You stagger back, losing {loss} health.")
        return math.ceil(loss)
    else:
        print('The enemy missed!')
        return 0

def hitChance(luck):
    hit = random.randint(0,4)
    if luck < hit:
        # print("Your attack missed!")
        return False

    else:
        # print('Your attack hit!')
        return True

def isDead(health):
    if health < 1:
        return True
    else:
        return False 

def loot(luck, genCharacter):
    lootChance = random.randint(0,4)
    if luck < lootChance:
        print("The enemy didn't drop any loot...")
    
    else:
        tableNum = random.randint(0,4)
        lootTableList =  ['items','ranged','defence','magic','attack']
        itemType = lootTableList[tableNum]
        file = open(itemType+'.txt','r')
        lines = file.readlines()

        print('The enemy dropped a...')

        item = random.randint(0,len(lines)-1)

        itemLine = lines[item]
        splitItemLine = itemLine.split(',')

        name = splitItemLine[0]
        value = int(splitItemLine[1])

        print(name)

        if itemType == 'attack':
            genCharacter.setAttack(genCharacter.getAttack()+value)
            print('Your new Attack stat is...')
            print(genCharacter.getAttack())

        elif itemType == 'ranged':
            genCharacter.setRanged(genCharacter.getRanged()+value)
            print('Your new Ranged stat is...')
            print(genCharacter.getRanged())

        elif itemType == 'defence':
            genCharacter.setDefence(genCharacter.getDefence()+value)
            print('Your new Defence stat is...')
            print(genCharacter.getDefence())

        elif itemType == 'magic':
            genCharacter.setMagic(genCharacter.getMagic()+value)
            print('Your new Magic stat is...')
            print(genCharacter.getMagic())

        else:
            if splitItemLine[2] == 'luck':
                genCharacter.setLuck(genCharacter.getLuck()+value)
                print('Your new Luck stat is...')
                print(genCharacter.getLuck())

            elif splitItemLine[2] == 'health':
                genCharacter.setHealth(genCharacter.getHealth()+value)
                print('Your new Health stat is...')
                print(genCharacter.getHealth())

def gameOver(enemyDead):
    if enemyDead == True:
        print("The battle continues...")

    else:
        print('You ran out of healtH!')
        print('The world fades to black. Better luck next time!')
        exit()

def battle(genEnemy, genCharacter):
    print("You have stumbled upon an enemy!")
    print(f'Its a {genEnemy.getName()}! They are looking for a fight!')
    print('You use your appraisal skill to check their stats...')
    pprint(vars(genEnemy))

    battle = True

    while battle == True:
        print('Choose your attack...')
        print('1. Sword Attack\n2. Ranged Attack\n3. Magic Attack')
        choice = input()

        while choice != '1' and choice != '2' and choice != '3':
            print('What are you doing? Choose 1, 2, or 3 to attack!') 
            print('1. Sword Attack\n2. Ranged Attack\n3. Magic Attack')
            choice = input()

        if choice == '1':
            damage = genCharacter.getAttack()
        
        elif choice == '2':
            damage = genCharacter.getRanged()

        else:
            damage = genCharacter.getMagic()

        print("You prepare to attack!")
        hit = hitChance(genCharacter.getLuck())

        if hit == True:
            genEnemy.setHealth(genEnemy.getHealth() - damage)
            print('Your attack hits!')
            print(f'The Enemy takes {damage} damage!')
            print(f'The Enemy has {genEnemy.getHealth()} remaining.')

        else:
            print("Your attack misses!")


        enemyDead = isDead(genEnemy.getHealth())

        if enemyDead == False:
            genCharacter.setHealth(genCharacter.getHealth() - enemyAttack(genEnemy.getChance(), genEnemy.getAttack(), genEnemy.getName(), genCharacter.getDefence()))
            
            characterDead = isDead(genCharacter.getHealth())

            if characterDead == True:
                battle = False
                return False

            else:
                print(f'You have {genCharacter.getHealth()} health remaining.')

        else:
            battle = False
            print('You have defeated the enemey!')
            print('You search the enemy for loot...')
            loot(genCharacter.getLuck(), genCharacter)

            return True

def levelGenerator(character, level):
    
    maxNumberOfEnemies = math.ceil(level*5)
    for x in range(0, maxNumberOfEnemies):
        bossChance = random.randint(1,10)
        if bossChance > 7:
            levelBoss = True
        else:
            levelBoss = False

        characterDead = battle(enemyGen(levelBoss), character)
        gameOver(characterDead)

def main():
    classData = createClass()
    character = hero(100, classData[0], classData[1],classData[2],classData[3],classData[4],classData[5])
    pprint(vars(character))
    print('Level 1')
    levelGenerator(character, 1)
    print('level 2')
    levelGenerator(character, 2)
    print('level 3')
    levelGenerator(character, 3)
    print('level 4')
    levelGenerator(character, 4)
    print("You have vanquished all your foes! Peace returns to the kingdom...for now...")
    pprint(vars(character))

main()




