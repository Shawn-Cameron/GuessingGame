"""
Name: Shawn Cameron
Date: Feb.28,2018
Course Code:ICS3UO

"""
def space(): 
  print ("-"*15) # function for separating to make reading easier

def guessing_game(): 
  name = input("What is your name?: ")
  start = input("Would you like to play a guessing game " +name+ "(y/n): ")

  runs = 0    #Defined both variables to allow usage
  guess_amount = 0
  while start == "y":
    runs +=  1 #Increases every round of guesses
    min = 1 #minium value for game should be 1 
    max = int(input("What do you want your Highest value guessing number to be?")) #To allow the user to pick their range
    import random
    number = random.randint(min,max) #Command to pick a random int. from range
    print("The Mystery number has been stored")
    print("You have 10 guesses have fun!!!")
    space()
    guess_right = 0 #Defined for later usage
  
    for guesses in range(1,11): #Gives the player 10 guesses 
      if guess_right == 0:
        guess = int(input("Guess a number"))
        if guess == number:
          guess_right +=  1 #when the player guess is correct loop stops
          print("That is Correct")
        elif (max + 1) > guess > number:
          guess_right = 0 
          print("The Mystery number is lower than your guess")
        elif (min - 1) < guess < number:
          guess_right = 0 
          print("The Mystery number is higher than your guess")
        else:
          print("That number is not in the range you assinged")
    
    
      elif guess_right == 1:
        guess_amount += (guesses - 1) #The value for guesses is added to the value of guess_amount after each run 
        print(name,"it took you",guesses - 1,"tries to guess",number,".")
        space()
        start_again = input("Would you like to play again?")
        if start_again == "y":
          break
        elif start_again == "n":
          start = start_again #stops while loop 
          break
        else:
          print("That is not a valid choice")
      
    if guesses == 10: #when for-loop runs after the 10th time this runs
      space()
      print("AWW you are out of guesses the mystery number was ",number)
      start_again = input("Would you like to play again " + name + "?")
      if start_again == "y":
        guessing_game() # runs when the user want to start over
      else:
        print("Have a nice day",name,"!")
        break


  if (start != "y") and (runs == 0): #Runs when the user replies no at start
    print("Aww I really wanted to play with you and see you struggle. Good Bye ",name)
  
  else: #Runs when start returns False
    average_guesses = guess_amount / runs 
    space()
    print (name,",your average guesses were",average_guesses,"per run or",guess_amount,"guesses /",runs," runs")
    print("Have a nice day")
    space()
  
  

guessing_game() #Allows program to run
  
  
  
  
  
  
  
