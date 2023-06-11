"""
Jogue o Dado Simulação

Trata-se apenas de um pequeno execícip para treinar python, caso queira melhorar o código ou coisa
do tipo, fique a vontade!
"""
import random

dice = {
    1: ["___________", "|         |", "|         |", "|    ●    |", "|         |", "|_________|"],
    2: ["___________", "|         |", "|  ●      |", "|         |", "|      ●  |", "|_________|"],
    3: ["___________", "|         |", "|  ●      |", "|    ●    |", "|      ●  |", "|_________|"],
    4: ["___________", "|         |", "| ●     ● |", "|         |", "| ●     ● |", "|_________|"],
    5: ["___________", "|         |", "| ●     ● |", "|    ●    |", "| ●     ● |", "|_________|"],
    6: ["___________", "|         |", "| ●     ● |", "| ●     ● |", "| ●     ● |", "|_________|"],
}


def print_dice(dice):
    def dice_number(key):
        for value in dice[key]:
            print(value)

    return dice_number


dice = print_dice(dice)

while True:
    option = input("Deseja rolar o dado?: ")

    if option.lower() == "sim" or option.lower() == "s":
        number = random.randint(1, 6)
        dice(number)
    else:
        print("Ok! saindo...")
        break
