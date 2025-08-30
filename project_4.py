import random

num = random.randint(1 ,50)

print()

attempts=0

while True:
    n = int(input("Guess the number between 1 and 50 :"))
    attempts+=1
    if num==n:
        print(f"Congratulations! You guessed it in", attempts, "attempts")
        break

    elif n>num:
      print("too high! try again")

    else:
       print("too low! try agian")

    


