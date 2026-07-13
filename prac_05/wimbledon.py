"""
Wimbledon
Estimate: 30 minutes
Actual: 60 minutes
"""


def main():
    """Print the winners and there total number of wins and countries total number of wins."""
    wimbledon_winners = []
    player_to_win_count = {}
    wimbledon_country_wins = {}

    print("Wimbledon Champions:")

    wimbledon_winners = open_file("wimbledon.csv")
    player_to_win_count = count_winners_total_wins(wimbledon_winners)
    wimbledon_country_wins = count_country_wins(wimbledon_winners)

    for wining_player, total_wins in player_to_win_count.items():
        print(f"{wining_player} {total_wins}")

    print()

    print(f"These {len(wimbledon_country_wins)} countries have won Wimbledon:")
    for winning_country in wimbledon_country_wins:
        print(winning_country)


def count_country_wins(country_list):
    """Count the total number of wins of countries."""
    winning_countries = {}
    for country in country_list:
        try:
            winning_countries[country[1]] += 1
        except KeyError:
            winning_countries[country[1]] = 1
    return winning_countries


def count_winners_total_wins(winner_list):
    """Count the total number of wins of each Wimbledon winner."""
    winner_count = {}
    for winner in winner_list:
        try:
            winner_count[winner[2]] += 1
        except KeyError:
            winner_count[winner[2]] = 1
    return winner_count


def open_file(file_name):
    """Open file and load data into a list of lists."""
    file_lines = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data = line.strip().split(",")
            file_lines.append(data)
    return file_lines


main()
