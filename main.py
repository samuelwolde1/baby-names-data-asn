# BABY NAMES DATA ASSIGNMENT START CODE

import json


def main():
    # Load Baby Data from File
    file = open("baby-names-data.json")
    baby_data = json.load(file)
    file.close()

    # Main Menu
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            displayAll(baby_data)
        elif selection == "2":
            searchGender(baby_data)
        elif selection == "3":
            searchRank(baby_data)
        elif selection == "4":
            searchStartLetter(baby_data)
        elif selection == "5":
            searchNameLength(baby_data)
        elif selection == "6":
            print("\nGOODBYE!\n")
            loop = False


def getMenuSelection():
    # Print Menu & Return User Selection
    print("\n*** BABY DATA - MAIN MENU ***")
    print("* 1: Display All")
    print("* 2: Search by Gender")
    print("* 3: Search by Rank")
    print("* 4: Search by Starting Letter")
    print("* 5: Search by Name Length")
    print("* 6: Exit")

    return input("* Enter Option #: ")


def displayAll(baby_data):
    # Display All Baby Data
    print("\nDISPLAY ALL")
    for baby in baby_data:
        print(baby["name"] + " (Rank: " + str(baby["rank"]) + ", Gender: " + baby["gender"] + ")")



def searchGender(baby_data):
    # Dislay All Baby Names based on Gender
    print("\nSEARCH BY GENDER")
    gender = input("Enter a gender (Boy/Girl): ")
    print('\n')
    for baby in baby_data:
        if baby["gender"] == gender:
            print(baby["name"] + " (Rank: " + str(baby["rank"]) + ", Gender: " + baby["gender"] + ")")


def searchRank(baby_data):
    # Display All Baby Names based on Rank
    print("\nSEARCH BY RANK")
    min_rank = input('Enter a minimum rank: ')
    max_rank = input('Enter a maximum rank: ')
    rank_num = 0
    print('\n')
    for baby in baby_data:
        if baby["rank"] <= int(max_rank) and baby["rank"] >= int(min_rank):
            rank_num+=1
            print(baby["name"] + " (Rank: " + str(baby["rank"]) + ", Gender: " + baby["gender"] + ")")
    print("Number of names found: " + str(rank_num))


def searchStartLetter(baby_data):
    # Insert User Item into a Position
    print("\nSEARCH BY START LETTER")
    letter = input("Enter a starting letter: ")
    name_count = 0
    print('\n')
    for baby in baby_data:
        if baby["name"][0] == letter:
            name_count+=1
            print(baby["name"] + " (Rank: " + str(baby["rank"]) + ", Gender: " + baby["gender"] + ")")
    print("Number of names found: " + str(name_count))


def searchNameLength(baby_data):
    # Remove item from position
    print("\nSEARCH BY NAME LENGTH")
    name_len = input("Enter a name length: ")
    name_count = 0
    print("\n")
    for baby in baby_data:
        if len(baby["name"]) == int(name_len):
            name_count+=1
            print(baby["name"] + " (Rank: " + str(baby["rank"]) + ", Gender: " + baby["gender"] + ")")
    print("Number of names found: " + str(name_count))

# Invoke main to begin program
main()
