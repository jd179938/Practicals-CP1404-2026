from random import randint

number_of_quick_picks = int(input("How many quick picks? "))
for j in range(number_of_quick_picks):
    quick_pick = []
    for i in range(6):
        quick_pick.append(randint(1, 45))
    quick_pick.sort()
    print(" ".join(f"{number:>2}" for number in quick_pick))
