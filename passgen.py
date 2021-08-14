import os

os.system('pip3 install more-itertools')
os.system('pip3 install colorama')
os.system('cls||clear')

import time
import colorama
from colorama import Fore
from itertools import permutations

colorama.init()

print("\n")
print(Fore.WHITE +                  "+---------------------------------------+")
print(Fore.WHITE + "+" + Fore.RED + " ###  ###  ###  ###   ###   ###  #   # " + Fore.WHITE + "+")
print(Fore.WHITE + "+" + Fore.RED + " # #  # #  #    #    #   #  #    ##  # " + Fore.WHITE + "+")
print(Fore.WHITE + "+" + Fore.RED + " ###  ###  ###  ###  #      ###  # # # " + Fore.WHITE + "+")
print(Fore.WHITE + "+" + Fore.RED + " #    # #    #    #  #  ##  #    #  ## " + Fore.WHITE + "+")
print(Fore.WHITE + "+" + Fore.RED + " #    # #  ###  ###   ###   ###  #   # " + Fore.WHITE + "+")
print(                              "+---------------------------------------+")
print(Fore.WHITE + "+" + Fore.YELLOW + " by 3ix                                " + Fore.WHITE + "+")
print(Fore.WHITE + "+" + Fore.YELLOW + " V 1.0                                 " + Fore.WHITE + "+")
print(                              "+---------------------------------------+")
print("\n")

def itterate(words):
    for x in range(1, len(words)+1):
        yield from map(''.join, permutations(words, x))

print("+ Choose your language:\n+ Languages:" + Fore.YELLOW + "Rus" + Fore.WHITE + "," + Fore.YELLOW + "Eng")
language = str(input(Fore.RED + ">>" + Fore.WHITE))

if language.lower() == "rus":

    print(" ")
    print("+ Выберите словарь:")
    file_proto = input(Fore.RED + ">>" + Fore.WHITE)
    file = open(file_proto, 'r')

    dictionary = []
    for x in file:
        dictionary.append(x)
    dictionary = [line.rstrip() for line in dictionary]
    print(" ")
    print("+ Ваш словарь:" + Fore.YELLOW)
    print(dictionary)

    print(" " + Fore.WHITE)
    print("+ Начать процесс генерации? [" + Fore.YELLOW + "Y" + Fore.WHITE + "/" + Fore.RED + "n" + Fore.WHITE + "]")
    answer = str(input(Fore.RED + ">>" + Fore.WHITE))

    if answer.lower() == "y" or answer.lower() == "yes" or answer.lower() == "да":

        print("\n+ Весь результат будет записан в файл через 5 секунд\n")
        time.sleep(5)
        file_out = open('Passgen_Output.txt', 'w')

        for words in itterate(dictionary):
            file_out.write(words + "\n")
            print(words)
        file_out.close()

        print(Fore.YELLOW + "\n+ Операция заверешена успешно!\n" + Fore.WHITE)

    else:
        print(Fore.RED + "\n+ Операция прервана")
elif language.lower() == "eng":

    print(" ")
    print("+ Select a dictionary:")
    file_proto = input(Fore.RED + ">>" + Fore.WHITE)
    file = open(file_proto, 'r')

    dictionary = []
    for x in file:
        dictionary.append(x)
    dictionary = [line.rstrip() for line in dictionary]
    print(" ")
    print("+ Your a dictionary:" + Fore.YELLOW)
    print(dictionary)

    print(" " + Fore.WHITE)
    print("+ Start the generation process? [" + Fore.YELLOW + "Y" + Fore.WHITE + "/" + Fore.RED + "n" + Fore.WHITE + "]")
    answer = str(input(Fore.RED + ">>" + Fore.WHITE))

    if answer.lower() == "y" or answer.lower() == "yes" or answer.lower() == "да":

        print("\n+ The entire result will be written to a file in 5 seconds\n")
        time.sleep(5)
        file_out = open('Passgen_Output.txt', 'w')

        for words in itterate(dictionary):
            file_out.write(words + "\n")
            print(words)
        file_out.close()

        print(Fore.YELLOW + "\n+ Operation completed successfully!\n" + Fore.WHITE)

    else:
        print(Fore.RED + "\n+ Operation aborted")
