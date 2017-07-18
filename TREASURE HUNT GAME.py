#Nathan Jones
#TREASURE HUNT GAME
#2016

import sys
import random

#global varibles
Glo_Xsize=8                 #defines the standard X size for the grid
Glo_Ysize=8                 #defines the standard Y size for the grid
Glo_BADcount=5              #defines the standard bandit count
Glo_TRECHcount=10           #defines the standard treasure chest count
Glo_COINcount=0             #sets the coin count to 0 each time
Glo_PLAYERx=0               #defines the players X starting position
Glo_PLAYERy=7               #defines the players Y starting position
Glo_Grid=[]                 #defines the empty array
Glo_DEBUG=False             #sets the 


#defines the function that will generate the grid
def Funct_GridMaker():
    global Glo_Xsize
    global Glo_Ysize
    global Glo_BADcount
    global Glo_TRECHcount
    global Glo_PLAYERx
    global Glo_PLAYERy
    global Glo_Grid
    Glo_Grid=[]

    for Y in range(1,Glo_Ysize +1):
        GridROW=[]

        for X in range(1,Glo_Xsize +1):
            GridROW.append("| ")

        Glo_Grid.append(GridROW)

    
#puts the treasure chests into the grid    
    for TC in range(0,Glo_TRECHcount):
        used=True
        while used:
            Xloc=random.randrange(0,Glo_Ysize)
            Yloc=random.randrange(0,Glo_Xsize)
#checks each square 
            if Xloc!=Glo_PLAYERx and Yloc!=Glo_PLAYERy:
                if Glo_Grid[Xloc][Yloc]== "| ":
                    Glo_Grid[Xloc][Yloc]="|1"
                    used=False

#puts the bandits into the grid
    for B in range(0,Glo_BADcount):
        used=True
        while used:
            Xloc=random.randrange(0,Glo_Ysize)
            Yloc=random.randrange(0,Glo_Xsize)
#checks each square 
            if Xloc!=Glo_PLAYERx and Yloc!=Glo_PLAYERy:
                if Glo_Grid[Xloc][Yloc]== "| ":
                    Glo_Grid[Xloc][Yloc]="|B"
                    used=False


#this function displys the grid for the player to see
def Funct_DispGrid():
    global Glo_Grid
    global Glo_Xsize
    global Glo_Ysize
    global Glo_BADcount
    global Glo_TRECHcount
    global Glo_COINcount
    global Glo_PLAYERx
    global Glo_PLAYERy
                   

#creates the borders inbetween each row and down the sides of the grid 
    BORDER=" "
    for X in range(0,Glo_Xsize):
        BORDER=BORDER+"--"
    BORDER=BORDER+"-"    
#this creates each row and the horizontal partion inbetween each  
    for Y in range(0,Glo_Ysize):
        ROW=" "

        for X in range(0,Glo_Xsize):
            if X==Glo_PLAYERx and Y==Glo_PLAYERy:
                ROW=ROW+"|P"
            else:
                if Glo_DEBUG==True:
                    ROW=ROW+Glo_Grid[X][Y]     
                else:
                    ROW=ROW+"| "
#this will disply the border and each row for the player to see
                    
        print(BORDER)
        print(ROW+"|")


    
    
    
    print(BORDER)
    print("COIN TOTAL: "+str(Glo_COINcount))
    print(" ")
    if Glo_DEBUG==True:
        print("******************")
        print("****DEBUG VEIW****")
        print("******************")
        print("Treasure Chests: "+str(Glo_TRECHcount))
        print("Bandit Count: "+str(Glo_BADcount))        
        print("Player X Position: "+str(Glo_PLAYERx))       
        print("Player Y Position: "+str(Glo_PLAYERy))
        print("******************")

    
       

#this function checks each square for a Bandit 
def FunctCHECK():
    global Glo_Grid
    global Glo_Xsize
    global Glo_Ysize
    global Glo_PLAYERx
    global Glo_PLAYERy
    global Glo_BADcount
    global Glo_TRECHcount
    global Glo_COINcount


    if Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]=="|B":
        Glo_COINcount=0
        print("A BANDIT HAS JUST TAKEN ALL OF YOUR COINS! ")

    if Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]=="|1":
        Glo_COINcount=Glo_COINcount+10
        Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]="|2"
        print("YOU FOUND A TREASURE CHEST! +10 COINS ")

    elif Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]=="|2":
        Glo_COINcount=Glo_COINcount+10
        Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]="|3"
        print("YOU FOUND A TREASURE CHEST! +10 COINS ")

    elif Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]=="|3":
        Glo_COINcount=Glo_COINcount+10
        Glo_Grid[Glo_PLAYERx][Glo_PLAYERy]="|B"
        print("YOU FOUND A TREASURE CHEST! +10 COINS ")

    if Glo_COINcount >99:
        Funct_Scroll()
        print("YOU HAVE WON! ")
        print("YOUR COIN TOTAL:")
        print(Glo_COINcount)
        print("YOUR BANDIT TOTAL:")
        print(Glo_BADcount)
        print("YOUR TREASURE CHEST COUNT:")
        print(Glo_TRECHcount)
        print("")

        answer=input("DO YOU WANT TO PLAY AGAIN? Y/N: ")

        if answer == "Y":
            Funct_Scroll()
            print("Here we go again!")
            Funct_ADVmenu()

        elif answer == "N":
            print("Good Bye!")
            sys.exit() #ends the program 

        else:
            Funct_menu()
            print("++++++++++++++++++++++++++++++++++++")
            print("""   THAT IS NOT A VALID ANSWER   """)
            print("++++++++++++++++++++++++++++++++++++")
        

    elif Glo_COINcount <100 and Glo_TRECHcount <1:
        Funct_Scroll()
        print("YOU HAVE LOST UNLUCKY! ")
        print("YOUR COIN TOTAL:")
        print(Glo_COINcount)
        print("YOUR BANDIT TOTAL:")
        print(Glo_BADcount)
        print("YOUR TREASURE CHEST COUNT:")
        print(Glo_TRECHcount)
    def Funt_PlayAgain():
        
        answer=input("DO YOU WANT TO PLAY AGAIN? Y/N: ")

        if answer == "Y":
            Funct_Scroll()
            print("Here we go again!")
            Funct_ADVmenu()

        elif answer == "N":
            print("Good Bye!")
            sys.exit() #ends the program 

        else:
            Funt_PlayAgain()
            print("++++++++++++++++++++++++++++++++++++")
            print("""   THAT IS NOT A VALID ANSWER   """)
            print("++++++++++++++++++++++++++++++++++++")
        
        
            

        
        
         
        
    

def Funct_xMOVE():
    global Glo_Grid
    global Glo_Xsize
    global Glo_Ysize
    global Glo_PLAYERx
    global Glo_PLAYERy
    global Glo_BADcount
    global Glo_TRECHcount

    Xmove=input("""How many spaces would you like to Right or Left?

R3 = RIGHT 3 Spaces
or
L3 = LEFT 3 Spaces
                 :""")
    if len(Xmove)==2:
        if Xmove[:1].upper()=="R":
            distance=int(Xmove[-1:])

        elif Xmove[:1].upper()=="L":
            distance=0-int(Xmove[-1:])

        else:
            print("ILLEGAL MOVE!")
            Funct_xMOVE()
        if Glo_PLAYERx+distance>Glo_Xsize-1 or Glo_PLAYERx+distance<0:
            print("ILLEGAL MOVE!")
            Funct_xMOVE()

        Glo_PLAYERx=Glo_PLAYERx+distance
        Funct_yMOVE()




def Funct_yMOVE():
    global Glo_Grid
    global Glo_Xsize
    global Glo_Ysize
    global Glo_PLAYERx
    global Glo_PLAYERy
    global Glo_BADcount
    global Glo_TRECHcount

    
    Ymove=input("""How many spaces would you like to Up or Down?

U3 = UP 3 Spaces
or
D3 = Down 3 Spaces
                 :""")
    if len(Ymove)==2:
        
        if Ymove[:1].upper()=="D":
            distance=int(Ymove[-1:])

        elif Ymove[:1].upper()=="U":
            distance=0-int(Ymove[-1:])

        else:
            print("ILLEGAL MOVE!")
            Funct_yMOVE()
        if Glo_PLAYERy+distance>Glo_Ysize-1 or Glo_PLAYERy+distance<0:
            print("ILLEGAL MOVE!")
            Funct_yMOVE()

        Glo_PLAYERy=Glo_PLAYERy+distance
        Funct_Scroll()
        FunctCHECK()
        Funct_DispGrid()
        Funct_xMOVE()
        Funct_yMOVE()
        
    

        
#this function displys the menu for the player and if they want to play or quit
def Funct_menu():

    Funct_Scroll()
    print("**************************************************")

    print("********Welcome to the Treasure Hunt GAME!********")

    print("""**************************************************
    Please select one of the following:

    1.Continue

    2.Quit

**************************************************""")
#asking the player if they want to play the game or not
    answer=input("*********Would you like to Play the game?********* ")
    print(answer)

    if answer == "1":
        Funct_Scroll()
        print("Enjoy the game!")
        Funct_ADVmenu()
            

    elif answer == "2":
        print("Good Bye!")
        sys.exit() #ends the program 

    else:
        Funct_menu()
        print("++++++++++++++++++++++++++++++++++++")
        print("""   THAT IS NOT A VALID ANSWER   """)
        print("++++++++++++++++++++++++++++++++++++")
#if the answer is invalid it will repeat the menu 
        


#defines the function
def Funct_Scroll():

#Scrolls the screen 70 lines down so the player can not see the other grid
    Scroll="\n"*70

    print(Scroll)   




def Funct_ADVmenu():
    global Glo_DEBUG
    Funct_Scroll()
    

    print("**************************************************")

    print("********Welcome to the Advanced menu!********")

    print("""**************************************************
    Please select one of the following:

1.Normal
2.Debug
3.Change Settings


**************************************************""")
    answer=input("What option do you choose? ")
    print(answer)

    if answer == "1":
        Funct_Scroll()
        print(" ++ Normal Mode ++ ")
        Funct_GridMaker()
        Funct_DispGrid()
        Funct_xMOVE()
        Funct_yMOVE()

    elif answer == "2":
        Funct_Scroll()
        print("++ DEBUG MODE ON ++")
        Glo_DEBUG=True
        Funct_GridMaker()
        Funct_DispGrid()
        Funct_xMOVE()
        Funct_yMOVE()

    elif answer == "3":
        Funct_Scroll()
        print("  ++ Change Settings Menu ++")
        Funct_SETmenu()
        
    else:
        Funct_Scroll()
        print("++++++++++++++++++++++++++++++++++++")
        print("""   THAT IS NOT A VALID ANSWER   """)
        print("++++++++++++++++++++++++++++++++++++")
#if the answer is invalid it will repeat the menu 
        Funct_ADVmenu() 


        
        

#menu that allows the player to changer each and every setting    
def Funct_SETmenu():
    global Glo_Xsize
    global Glo_Ysize
    global Glo_BADcount
    global Glo_TRECHcount
    global Glo_PLAYERx
    global Glo_PLAYERy
    global Glo_Grid
    global Glo_DEBUG
    

    print("**************************************************")

    print("**********Welcome to the Settings menu!***********")

    print("""**************************************************
    Please select one of the following:

1.Grid size 
2.Bandit Count
3.Treasure Chest Count
4.Debug
5.Change ALL


**************************************************""")
    answer=input("What option do you choose? ")
    print(answer)

    if answer == "1":
#allows them to change indiviual settings
        Funct_Scroll()
        Funct_Xsize()
        Funct_Ysize()
        Funct_DEBUG()
        Funct_PlaySETmenu() 

    elif answer == "2":
#allows them to change indiviual settings
        Funct_Scroll()
        Funct_BADcount()
        Funct_DEBUG()
        Funct_PlaySETmenu()

    elif answer == "3":
#allows them to change indiviual settings
        Funct_Scroll()
        Funct_TRECHcount()
        Funct_DEBUG()
        Funct_PlaySETmenu()


   
    elif answer == "4":
#allows them to change indiviual settings
        Funct_Scroll()
        Funct_DEBUG()
        Funct_PlaySETmenu()


    elif answer == "5":
#allows the player to change all 5 options
        Funct_Scroll()
        Funct_Xsize()
        Funct_Ysize()
        Funct_BADcount()
        Funct_TRECHcount()
        Funct_DEBUG()
        Funct_PlaySETmenu()
            
    else:
        Funct_Scroll()
        print("++++++++++++++++++++++++++++++++++++")
        print("""   THAT IS NOT A VALID ANSWER   """)
        print("++++++++++++++++++++++++++++++++++++")
#if the answer is invalid it will repeat the menu 
        Funct_SETmenu() 

def Funct_Xsize():
    global Glo_Xsize
    
    Glo_Xsize=input("""
+++++++Maximum X size of the grid is 15 or lower++++++++

     What X size of the grid do you want? """)
#asking the player the width of the grid
    Glo_Xsize=int(Glo_Xsize)
    if Glo_Xsize <1 or Glo_Xsize >15:
#repeats the question if an invalid answer is given
        Funct_Scroll()
        print("NOT A VALID ANSWER! ")
        Funct_Xsize()
        
    

def Funct_Ysize():
    global Glo_Ysize
    global Glo_PLAYERy


    
    Glo_Ysize=input("""
+++++++Maximum Y size of the grid is 15 or lower++++++++

     What Y size of the grid do you want? """)
#Asking the player the height of the grid
    Glo_Ysize=int(Glo_Ysize)
    if Glo_Ysize <16 and Glo_Ysize >1:
        Glo_PLAYERy=Glo_Ysize-1
   
#repeats the question if an invalid answer is given
        
    else:
        print("NOT A VALID ANSWER! ")
        Funct_Ysize()
          
        
def Funct_BADcount():
    global Glo_BADcount

    Glo_BADcount=input("""
+++++++Maximum amount of Bandits is 15 or lower++++++++

     How many Bandits do you want? """)
#asking the player how many bandits they want
    Glo_BADcount=int(Glo_BADcount)
    if Glo_BADcount <(Glo_Xsize*Glo_Ysize)-1 and Glo_BADcount >0:
        print("")
#repeats the question if an invalid answer is given
    else:
        Funct_Scroll()
        print("NOT A VALID ANSWER! ")
        Funct_BADcount()
    
    
def Funct_TRECHcount():
    global Glo_TRECHcount

    Glo_TRECHcount=input("""
+++Maximum amount of Treausre Chest's is 15 or lower+++

     How many Treausre Chest's do you want? """)
#asking the player how many Treasure Chests they want
    Glo_TRECHcount=int(Glo_TRECHcount)
    if Glo_TRECHcount <(Glo_Xsize*Glo_Ysize)-1-Glo_BADcount and Glo_TRECHcount >0:
        print("")
#repeats the question if an invalid answer is given 
    else:
        Funct_Scroll()
        print("NOT A VALID ANSWER! ")
        Funct_TRECHcount()



def Funct_DEBUG():
    global Glo_DEBUG

    Glo_DEBUG=input("""

+++++++++++++++++++++DEBUG MODE+++++++++++++++++++++

1.Debug mode: ON
2.Debug mode: OFF


""")
    if Glo_DEBUG == "1":
        print("\n"*44) 
        print("++++ DEBUG MODE ON ++++")
        Glo_DEBUG=True

    elif Glo_DEBUG == "2":
        print("\n"*44)
        print("++++ DEBUG MODE OFF ++++")
        Glo_DEBUG=False

    #Repeats the question 
    else:
        Funct_Scroll()
        print("NOT A VALID ANSWER! ")
        Funct_DEBUG()


def Funct_PlaySETmenu():
    print("\n"*42)
        

    print("**************************************************")

    print("*******Welcome to YOUR Treasure Hunt GAME!********")

    print("""**************************************************
    Please select one of the following:

    1.Play

    2.Back

**************************************************""")
#asking the player if they want to play the game or not
    answer=input("******Would you like to YOUR Play the game?****** ")
    print(answer)

    if answer == "1":
        Funct_Scroll()
        print("                 Enjoy YOUR game!                          ")
        Funct_GridMaker()
        Funct_DispGrid()
        Funct_xMOVE()
        Funct_yMOVE()
              

    elif answer == "2":
        print("                     Good Bye!                          ")
        Funct_Scroll()
        Funct_ADVmenu()

    else:
        Funct_Scroll()
        print("++++++++++++++++++++++++++++++++++++")
        print("""   THAT IS NOT A VALID ANSWER   """)
        print("++++++++++++++++++++++++++++++++++++")
#if the answer is invalid it will repeat the menu 
        
        Funct_PlaySETmenu()
Funct_menu()        
