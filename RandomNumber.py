from random import randint

print ("Hello and Welcome to guess the random number")

question=input("Would you like to play a game now y/n")
number=randint(0,9)

if question.lower() =="n":
 print("oh...okay")


if question.lower() =="y":
  print("Please think of a number  between 1-9, you have 3 trials")
  trial=0
  while( trial!=3):
    guess=int(input("Please type your number guess"))
    trial+=1
    if(guess>number):
     print("Guess lower")
    elif (guess<number):
     print("Guess Higher")
    else :
     print ("You won")
     break
  else:
    print ("Your trials are exhausted" ) 

       