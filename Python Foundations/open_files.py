'''
Longer way to open file

file = open('mytextfile.txt')
try:
    # Do stuff here
    pass
finally:
    file.close()
'''
def find_player():
    position = input("What Position player are you looking for?\n")

    #This method ensures file is awlways closed.
    with open(r'c:\code\learningPython\Python Foundations\TextFiles\mytextfile.txt') as file:
        #file.read() = returns the whole file as string, or return specfied number of bytes
        #file.readline() returns the next line of the fail as a string
        #file.readlines() returns a list of strings of all of the lines in the file , normally used then to print lines
        for line in file:
            if position in line:
                found = True
                print(line)
        if not found:
            print("Unable to find a player in that posistion")

def add_player():
    position = input("What posistion do you want to add?")
    player_name = input("What is the players name?")
    with open(r'c:\code\learningPython\Python Foundations\TextFiles\mytextfile.txt', 'a') as file:
        file.write(position + " - " + player_name + '\n')

def main():
    decision = input("What do you want to add or find a player?")
    if(decision == "add"):
        add_player()
    else:
        find_player()

main()