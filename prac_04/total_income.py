"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
from typing import Any


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for number_of_months in range(1, months + 1):
        income = float(input(f"Enter income for month {number_of_months}: "))
        incomes.append(income)

    print_report(incomes, months)


def print_report(incomes: list[Any], months: int):
    print("\nIncome Report\n-------------")
    total = 0
    for number_of_months in range(1, months + 1):
        income = incomes[number_of_months - 1]
        total += income
        print(f"Month {number_of_months:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()