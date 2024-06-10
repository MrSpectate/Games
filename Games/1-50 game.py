import random

def play_game():

    print("In this game you guess the number if the number correct you won !")

# user choice ke kitne numbers ka game rakhna he

    numebr_of_game = random.randint(1,50)

    attempt = 0 

# using while True for looping

    while True:
      
# user area
      user = (input("Guess the number : "))

#  if user digit ni howa tho print()

      if not user.isdigit():
        print("Enter a numebers")
        continue
      
# user - int

      user =int(user)

# when you attempt 1 time it increase 1 or 2 or 3 ....


      attempt += 1

# if user ka number bara hoga tho wo higer ai ga agar chota hoga tho lower ayga agar equal aya tho won

      if user > numebr_of_game:
        print("It's High Try lower")
      elif(user < numebr_of_game):
         print("It's Lower Try higer")
      else:
         print("Congrate you won ! at " , attempt ,"attemps" )
         break
def main():
   while True:
      play_game()
      play_again = input("Do yo want to play again (yes/no)").strip().lower
      if play_again != "yes":
         print("Thank you for playing")
         break
      
if __name__  == "__main__":
   main()
   
      
      
         
         
     
    
