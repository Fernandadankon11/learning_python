n = int(input("entrez un nombre"))
i = 0

while n > 0 : 
    print(" " * i, end = "")

    for j in range(n):
        print("X", sep = "", end = "")

    print("")
    n -= 1 
    i += 1

