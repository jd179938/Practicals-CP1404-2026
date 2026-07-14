from prac_06 import guitar
from prac_06.guitar import Guitar

def main():
    guitars = []
    name = input("name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input('Cost: '))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

        name = input("Name: ")
    print(guitars)

main()