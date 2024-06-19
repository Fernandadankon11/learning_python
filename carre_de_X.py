x = int(input("Entrez le nombre de X"))
i = 0

while True: 
    i += 1 
    for j in range(x):
        print("X", sep="", end="")
    if i == x:
        break
    print("")