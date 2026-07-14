from prac_06 import guitar
from prac_06.guitar import Guitar

def main():
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another guitar", 2005, 14999.99)

    print(guitar_2)
    print(guitar_1)

    print(f"{guitar_1.name} get_age() - Expected 104. Got {guitar_1.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected 21. Got {guitar_2.get_age()}")

main()