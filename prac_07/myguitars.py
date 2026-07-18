from guitar import Guitar

guitars = []


def main():
    guitars = open_file()
    add_guitar(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def open_file():
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars

def add_guitar(guitars):
    name = input("Guitar name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))

    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    out_file = open("guitars.csv", "a")
    out_file.write(f"\n{str(new_guitar.name)},{str(new_guitar.year)},{str(new_guitar.cost)}")
    out_file.close()

main()
