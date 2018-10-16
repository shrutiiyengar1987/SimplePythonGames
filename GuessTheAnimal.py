import os
import random
import collections


def main():
   
    quizHint1={"Dog":"One which wags its tails",
               "Goat":"Name Starts with G , gives milk too",
               "Pig" :"Pink in color",
               "Sheep":"Found in the mountains, gives us wool",
               "Cat":"Milk is its favourite,Dog's favourite"}


    quizHint2={"Lion":"Known as the King of Forest",
               "Fox":"The Cunning one which loves grapes" ,
               "Elephant" :"Largest Land Animals on Earth",
               "Zebra":"What type of animal is very big and has black and white stripes",
               "Bear":"Loves Sugarcane , Bulky and Heavy"}

 

    print("Hello Kids! Welcome to guess the animal!!!")

    choice=input(("Please tell me which one would you like to play "+os.linesep+"1.Domestic Animals"+os.linesep+
                  "2.Wild Animals"+os.linesep ))
    points=0
        
    if choice=='1':
        dictVar=quizHint1
    else:
        dictVar=quizHint2
 
        points=0    

    for key in list(dictVar.keys()):   
       guess=input("Please guess the  animal "+os.linesep+ "Hint:"+dictVar[key]+os.linesep)
       if(guess.lower()==key.lower()):
           points+=10
           print("You are correct!!!!!!You win 10 points ")
       else:
           print("Ah-oh..That is wrong") 
     
    if(points==50):
        print("YOU WIN!!!lEVEL 1 DONE ")
    else: 
        print("Your score this time :"+str(points))
 
if __name__ == '__main__':
    main()