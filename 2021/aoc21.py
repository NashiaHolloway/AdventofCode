
def SonarSweep(day1input):
    increased = 1
    with open(day1input, "r") as file:
            lines = file.readlines()
            file.close()
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
    

def Dive(day2input):
    h = 0 # horizontal position
    d = 0 # depth
    with open(day2input, "r") as file:
        lines = file.readlines()
        file.close()
        for line in lines:
            instruction = line.split()
            if instruction[0] == "forward":
                h += int(instruction[1])
                print("forward", h)
            elif instruction[0] == "down":
                d += int(instruction[1])
                print("down", d)
            else:
                d -= int(instruction[1])
                print("up", d)
    print("Final Horizontal Position:", h)
    print("Final depth:", d)
    ans = h*d
    print("Answer:", ans)

def main():
    # day1input = "day1input.txt"
    # SonarSweep(day1input)

    day2input = "day2input.txt"
    Dive(day2input)

    day2_5input = "day2_5input.txt"
    Dive2(day2_5input)


if __name__ == '__main__':

    main()