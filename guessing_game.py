#! /usr/bin/python3

# The  random  package  is  needed  to  choose a random  number
import  random
def compt():
    global compteur
    compteur +=1

compteur=0
# Define  the  game in a function
name = input("Enter your name:  ")
def  guess_loop ():
    # This is the  number  the  user  will  have to guess , chosen  
    # randomlyin  between 1 and  100number_to_guess = random.randint(1, 100)
    number_to_guess = random.randint(1, 100)
    print("I have in mind a number  in  between 1 and 100, can  you  findit?")
    # Replay  the  question  until  the  user  finds  the  correct  number
    while  True:
        try:
           # Read  the  number  the  user  inputs
           guess = int(input()) 
        

           # Compare  it to the  number  to  guess
           if guess  > number_to_guess:
               print("Lower !!")
               compt()
           elif  guess < number_to_guess:
               print("Higher !!")
               compt()
           else:
               # The  user  found  the  number  to guess , let’s exit
                print("Congrats",name,"!,","the number was",guess,",","Nb of trials",compteur)
                return
            # A ValueError  is  raised  by the  int()  function  
            # if the  userinputs  something  else  than a number
        except  ValueError  as err:
            print("Just an integer")
# Launch  the game
guess_loop ()