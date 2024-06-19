import random

number_to_guess = random.randint(0, 100)
number_of_tries = 0
limit_of_attemps = 5

for i in range (limit_of_attemps):
    user_answer = int(input("devinez le nombre"))
    number_of_tries += 1
    i += 1
    if user_answer == number_to_guess:
        print("bravo ! vous avez réussi en ", number_of_tries, " essais.") 
        break
    elif user_answer > number_to_guess:
        print("Trop grand")
    elif user_answer < number_to_guess:
        print("Trop petit")
    if i == limit_of_attemps:
        print("perdu, le secret était : ", number_to_guess)
    
