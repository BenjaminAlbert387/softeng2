def maths_module_function():
    with open('ethicsmodule.txt') as file5:
        lines_5 = file5.readlines()
        lns_5 = [line.strip() for line in lines_5]
        lns_5 = list(map(int, lns_5))