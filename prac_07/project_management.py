"""
Estimated time: 2 hours
Actual time:
"""
from project import Project
import datetime

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")

def main():
    print("Welcome to Pythonic Management")
    print(MENU)
    projects = []
    project_count = 0
    in_file = open("projects.txt", "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split()
        name = " ".join(parts[:-4])
        start_date = convert_date(parts[-4])
        project = Project(name, start_date, int(parts[-3]), float(parts[-2]), int(parts[-1]))
        projects.append(project)
    in_file.close()

    for project in projects:
        print(project)

def convert_date(date_string):
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    return date.strftime("%d/%m/%Y")


main()