from prac_06.programming_language import ProgrammingLanguage

def main():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)

    print(java)
    print(c_plus_plus)
    print(python)
    print(visual_basic)
    print(ruby)

main()