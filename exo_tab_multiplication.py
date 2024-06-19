number = int(input("veuillez entrer un nombre"))

if number <= 0 : 
    print("veuillez entrer un nombre positif")

if number > 0: 
    for i in range(1, number+1):
        for j in range(1, number+1):
            print(i * j, sep="", end="")
        print("")