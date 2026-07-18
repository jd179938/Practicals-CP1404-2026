class Guitar:
    CURRENT_YEAR = 2026
    VINTAGE_AGE = 50

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        return Guitar.CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >=  Guitar.VINTAGE_AGE

    def __lt__(self, other_guitar):
        return self.year < other_guitar.year
