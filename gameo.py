import random
import time
# The main goal of this little project was to play a bit with functions, classes and flow
#lvl list defines after how many killes hero gets lvl points
lvllst = [0,2,4,8,12]
class hero(object):
    
    def __init__(self, name,lvl = 0,atc =3,dfn=3,hp=21,gobkill=0,lvlpnt=0):
        self.name = name
        self.lvl = lvl
        self.atc = atc
        self.dfn = dfn
        self.hp = hp
        self.gobkill = gobkill
        self.lvlpnt = lvlpnt

#next snippet is used to spread lvl points acros attac, deffence and hp
    def lvlUp (self, y):
        y=3
        while y !=0:
           x = input("you got %i lvl points! Plz type in atc to + atack, dfn to + deffence, hp to + hit points.\n"%y)
           if x.lower() == "atc":
              self.atc +=1
              y-=1
           if x.lower() == "dfn":
              self.dfn +=1
              y-=1
           if x.lower() == "hp":
              self.hp += 5
              y=1
           print(game1.name,"\n", "your lvl is:", game1.lvl,"\n","your atack is:", game1.atc,"\n","your deffence is:", game1.dfn,"\n","your hp is:",game1.hp)
        
#the main and only mob themeplate
                 
class gbln(object):
    def __init__(self, atc, dfn, hp):
        self.atc = atc
        self.dfn = dfn
        self.hp = hp

        
def fight(game1, goblin):
    #here I am  creating two variables, the first one is needed mostly to represent game1.hp without changing it globaly
    #so with evry new fight hero's hp goes back to whatever max vale is
    #h just makes further code shorter, since goblins are generated for every single fight anyway
    z = game1.hp
    h = goblin.hp
    while z>0 and h>0:
        #those two var are actual dammage done by and to hero
           x = game1.atc - goblin.dfn
           y = goblin.atc - game1.dfn
           
            
           if x > 0:
              time.sleep(2)
              print ('-%i \n'%x)
              h-=x
              print("the goblin has %i hp left"%h)
              #the next snippet saves player from the situation when a goblin is undeafitable due to high armor lvl
           if x<=0:
              time.sleep(2)
              print(" NO DAMAGE TO THE GOBLIN, TIME TO RUN!!!")
              game(game1,goblinIncubator())
           if y > 0 and h > 0:
              time.sleep(2)
              print ('-%i \n'%y)
              z-=y
              print( game1.name +" has %i hp left" %z)
           if y<=0 and h>0:
              time.sleep(2)
              print(" NO DAMAGE TO YOU!!!")
    if h <= 0:
           game1.gobkill +=1
           print("The goblin was defited!")
           if game1.gobkill in lvllst:
               game1.lvl+=1
               game1.lvlpnt+=3
               game1.lvlUp(game1.lvlpnt)
               print(game1.name,"\n", "your lvl is:", game1.lvl,"\n","your atack is:", game1.atc,"\n","your deffence is:", game1.dfn,"\n","your hp is:",game1.hp)
               game(game1,goblinIncubator())
           elif game1.gobkill == 21:
               endGame()
           else:
               game(game1,goblinIncubator())
    if z <= 0:
           death()
   

def game(game1,goblin):
    a = input("Wondering through the forest you see a goblin.Enter R to run and A to attack.\n" + "The Goblin has:\n %i atc"%goblin.atc + "\n %i dfn"%goblin.dfn + "\n %i hp \n"%goblin.hp) 
    if a.lower() == "r":
       game(game1,goblinIncubator())
    #at first I thoght to create a specific command for goblin fight, but then I thought if player is not paying enought attantion to press R to run
    #then they deserve to fight watever gobin they are facing. So bacicaly every button is attack now
    else:
       fight(game1,goblin)

def death():
    return(print ("YOU ARE DEAD!GAME OVER!"))
    quit()


def endGame():
    
        print("""NOW YOU ARE SUPERIOR CREATURE AT THE FOREST! NO GOBLIN CAN DEFEAT YOU! THANKS FOR PLAYING!!!""")
        quit()
#the goblin incubator
def goblinIncubator():
    goblin = gbln(random.randint(1,10),random.randint(1,10),random.randint(10,40))
    return(goblin)




game1 = hero(input("""Welcome to The Goblin Forest!
Tell me what is your name brave hero?\n"""))
print(game1.name,"\n", "your lvl is:", game1.lvl,"\n","your atack is:", game1.atc,"\n","your deffence is:", game1.dfn,"\n","your hp is:",game1.hp)

if game1.gobkill in lvllst:
      game1.lvlUp(game1.lvlpnt)
game(game1, goblinIncubator())








   
       
       


