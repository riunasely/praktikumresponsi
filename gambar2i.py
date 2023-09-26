with open("config.txt") as file:
    listKu = file.read().splitlines()
    print(listKu)

with open("config.txt", "r") as file:
    listKu = file.readlines()
    print(listKu)

with open("config.txt", "r") as file:
    listKu = file.readline()
    print(file.readline())

with open("config.txt", "r") as file:
    for line in file:
        print(line, end = '')
