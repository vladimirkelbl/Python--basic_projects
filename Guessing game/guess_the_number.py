#from random import seed
#from random import random
#seed(1)
import random
import numpy
import math

print("HELLO\nThis is Guess the Number game!\nType a value and pass it by pressing Enter.\nStart with inserting your interval in which you want to guess the number :-)")
down_border = int(input("Down border: "))
high_border = int(input("High border: "))

number_for_guessing = random.randrange(down_border, high_border, 1)
print("\nFriendly help: " + str(number_for_guessing))
number_of_tryies = 1
minimum_number_of_tryies = int(math.log2(high_border - down_border + 1))        #mathematics: bisection method
if high_border-down_border+1 > 21:
    print("Minimum rounds to guess correctly: " + str(minimum_number_of_tryies))

if high_border-down_border+1 < 21:
    flag = 0
    possibilities = [int(x) for x in list(numpy.linspace(down_border, high_border, high_border - down_border + 1))]
    print("\nYour posibilities:")
    for c in possibilities:
        print(c, end= " ")
    print()
    guessed_number = int(input(f"ROUND {number_of_tryies}: Guess the number!\n\t"))

    while number_for_guessing != guessed_number:
        print("\twrong :-(\ttry again")
        
        if int(guessed_number) >= down_border and int(guessed_number) <= high_border:
            possibilities[int(guessed_number)-down_border] = "-"
        else: print("You choosed out of range of possibilities!")
        
        print("\nYour posibilities:")
        for c in possibilities:
            print(c, end= " ")
        print()
        number_of_tryies += 1
        guessed_number = int(input(f"ROUND {number_of_tryies}: Guess the number!\n\t"))
else:
    flag = 1
    print(f"\nInterval of your possibilities is: <{down_border}, {high_border}>")
    guessed_number = int(input(f"ROUND {number_of_tryies}: Guess the number!\n\t"))
    
    while number_for_guessing != guessed_number:
        print("\twrong :-(\ttry again")
        if guessed_number >= down_border and guessed_number <= high_border:
            if guessed_number > number_for_guessing:
                print("You guessed too HIGH.\n")
                high_border = guessed_number-1
            else:
                print("You guessed too LOW.\n")
                down_border = guessed_number+1
            print(f"New interval of your possibilities is: <{down_border}, {high_border}>")
        else:
            print("You choosed out of range of possibilities!")
            print(f"Interval of your possibilities is still: <{down_border}, {high_border}>")
        number_of_tryies += 1
        guessed_number = int(input(f"ROUND {number_of_tryies}: Guess the number!\n\t"))
 

print(f"Jáj, you are correct! The number is {number_for_guessing}! You needed {number_of_tryies} " + ("round" if number_of_tryies == 1 else "rounds") + "." + (f" Mathematically minimum rounds was {minimum_number_of_tryies} to guess the correct number so you are really good!" if (flag == 1 and minimum_number_of_tryies >= number_of_tryies) else "") + (f" Mathematically minimum rounds was {minimum_number_of_tryies} to guess the correct number so next time you will be better ;-)" if (flag == 1 and minimum_number_of_tryies < number_of_tryies) else ""))
