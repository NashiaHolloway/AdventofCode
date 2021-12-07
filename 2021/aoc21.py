
def day1(day1input):
    increased = 1
    with open(day1input, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                if i+1 < len(lines):
                    if lines[i] < lines[i+1]:
                        print(lines[i+1], " (INCREASED)")
                        i += 1
                        increased += 1
                    else:
                        print(lines[i+1], " (DECREASED)")
                else:
                    print("Number of increases: ", increased)
    file.close()

def main():
    day1input = "day1input.txt"
    day1(day1input)


if __name__ == '__main__':

    main()