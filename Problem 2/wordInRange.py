def wordInRange():
    filename = input()
    upper_bound = input()
    lower_bound = input()
    #Type your code here
    with open(filename,"r") as file:
        for line in file.readlines():
            line = line.strip()
            if upper_bound <=  line and line <= lower_bound:
                print(line + " - in range")
            else:
                print(line + " - not in range")
    return
if __name__ == '__main__':
    wordInRange()