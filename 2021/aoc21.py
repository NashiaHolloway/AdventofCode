########################################################
#                   ADVENT OF CODE 2021                #
########################################################

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
            if instruction[0] == "forward": # increase horizontal position by x
                h += int(instruction[1])
                print("forward", h)
            elif instruction[0] == "down":  # increase depth by x
                d += int(instruction[1])
                print("down", d)
            else:                           # (up) decrease depth by x
                d -= int(instruction[1])
                print("up", d)
    print("Final Horizontal Position:", h)
    print("Final depth:", d)
    ans = h*d
    print("Answer:", ans)

def Dive2(day2_5input):
    h = 0 # horizontal position
    d = 0 # depth
    a = 0 # aim
    with open(day2_5input, "r") as file:
        lines = file.readlines()
        file.close()
        for line in lines:
            instruction = line.split()
            if instruction[0] == "forward": # increase horizontal position by x
                h += int(instruction[1])
                if a != 0:                    
                    d += int(instruction[1]) * a
                    print("forward", h)
                    print("new depth", d)
            elif instruction[0] == "down":  # increase aim by x
                a += int(instruction[1])
                print("down", d)
            else:                           # (up) decrease aim by x
                a -= int(instruction[1])
                print("up", d)
    print("Final Horizontal Position:", h)
    print("Final depth:", d)
    ans = h*d
    print("Answer:", ans)

def BinaryDiagnostic(day3input):
    # power consumption = gamma rate * epsilon rate
    # gamma rate = most common bit in the corresponding position (convert binary to decimal)
    # epsilon rate = least common bit in the corresponding position (convert binary to decimal)
    pc = 0 # power consumption
    gr = 0 # gamma rate
    er = 0 # epsilon rate

    count_zero0 = 0
    count_one0 = 0

    count_zero1 = 0
    count_one1 = 0

    count_zero2 = 0
    count_one2 = 0

    count_zero3 = 0
    count_one3 = 0

    count_zero4 = 0
    count_one4 = 0

    count_zero5 = 0
    count_one5 = 0

    count_zero6 = 0
    count_one6 = 0

    count_zero7 = 0
    count_one7 = 0

    count_zero8 = 0
    count_one8 = 0

    count_zero9 = 0
    count_one9 = 0

    count_zero10 = 0
    count_one10 = 0

    count_zero11 = 0
    count_one11 = 0
    
    gr0 = 0
    gr1 = 0
    gr2 = 0
    gr3 = 0
    gr4 = 0
    gr5 = 0
    gr6 = 0
    gr7 = 0
    gr8 = 0
    gr9 = 0
    gr10 = 0
    gr11 = 0

    er0 = 0
    er1 = 0
    er2 = 0
    er3 = 0
    er4 = 0
    er5 = 0
    er6 = 0
    er7 = 0
    er8 = 0
    er9 = 0
    er10 = 0
    er11 = 0

    with open(day3input, "r") as file:
        lines = file.readlines()
        file.close()

    for line in lines:
        numbers = list(line.strip())
        for index, bit in enumerate(numbers):
            if int(bit) == 0:
                # 0 was found
                if index == 0:
                    count_zero0 += 1
                elif index == 1:
                    count_zero1 += 1
                elif index == 2:
                    count_zero2 += 1
                elif index == 3:
                    count_zero3 += 1
                elif index == 4:
                    count_zero4 += 1
                elif index == 5:
                    count_zero5 += 1
                elif index == 6:
                    count_zero6 += 1
                elif index == 7:
                    count_zero7 += 1
                elif index == 8:
                    count_zero8 += 1
                elif index == 9:
                    count_zero9 += 1
                elif index == 10:
                    count_zero10 += 1
                elif index == 11:
                    count_zero11 += 1
                print(f"0 is found at index {index}")
            else:
                # 1 was found
                if index == 0:
                    count_one0 += 1
                elif index == 1:
                    count_one1 += 1
                elif index == 2:
                    count_one2 += 1
                elif index == 3:
                    count_one3 += 1
                elif index == 4:
                    count_one4 += 1
                elif index == 5:
                    count_one5 += 1
                elif index == 6:
                    count_one6 += 1
                elif index == 7:
                    count_one7 += 1
                elif index == 8:
                    count_one8 += 1
                elif index == 9:
                    count_one9 += 1
                elif index == 10:
                    count_one10 += 1
                elif index == 11:
                    count_one11 += 1
                print(f"1 is found at index {index}")
    

    if count_zero0 > count_one0:
        gr0 = 0
        er0 = 1
    else: 
        gr0 = 1
        er0 = 0

    print("count_zero0", count_zero0)
    print("count_one0", count_one0)

    if count_zero1 > count_one1:
        gr1 = 0
        er1 = 1
    else: 
        gr1 = 1
        er1 = 0

    print("count_zero1", count_zero1)
    print("count_one1", count_one1)
        
    if count_zero2 > count_one2:
        gr2 = 0
        er2 = 1
    else:
        gr2 = 1
        er2 = 0

    print("count_zero2", count_zero2)
    print("count_one2", count_one2)

    if count_zero3 > count_one3:
        gr3 = 0
        er3 = 1
    else:
        gr3 = 1
        er3 = 0

    print("count_zero3", count_zero3)
    print("count_one3", count_one3)

    if count_zero4 > count_one4:
        gr4 = 0
        er4 = 1
    else:
        gr4 = 1
        er4 = 0

    print("count_zero4", count_zero4)
    print("count_one4", count_one4)

    if count_zero5 > count_one5:
        gr5 = 0
        er5 = 1
    else:
        gr5 = 1
        er5 = 0

    print("count_zero5", count_zero5)
    print("count_one5", count_one5)

    if count_zero6 > count_one6:
        gr6 = 0
        er6 = 1
    else:
        gr6 = 1
        er6 = 0

    print("count_zero6", count_zero6)
    print("count_one6", count_one6)

    if count_zero7 > count_one7:
        gr7 = 0
        er7 = 1
    else:
        gr7 = 1
        er7 = 0

    print("count_zero7", count_zero7)
    print("count_one7", count_one7)

    if count_zero8 > count_one8:
        gr8 = 0
        er8 = 1
    else:
        gr8 = 1
        er8 = 0

    print("count_zero8", count_zero8)
    print("count_one8", count_one8)

    if count_zero9 > count_one9:
        gr9 = 0
        er9 = 1
    else:
        gr9 = 1
        er9 = 0

    print("count_zero9", count_zero9)
    print("count_one9", count_one9)

    if count_zero10 > count_one10:
        gr10 = 0
        er10 = 1
    else:
        gr10 = 1
        er10 = 0

    print("count_zero10", count_zero10)
    print("count_one10", count_one10)

    if count_zero11 > count_one11:
        gr11 = 0
        er11 = 1
    else:
        gr11 = 1
        er11 = 0

    print("count_zero11", count_zero11)
    print("count_one11", count_one11)

    gr = str(gr0) + str(gr1) + str(gr2) + str(gr3) + str(gr4) + str(gr5) + str(gr6) + str(gr7) + str(gr8) + str(gr9) + str(gr10) + str(gr11)
    er = str(er0) + str(er1) + str(er2) + str(er3) + str(er4) + str(er5) + str(er6) + str(er7) + str(er8) + str(er9) + str(er10) + str(er11)

    print("gamma", gr)
    print("epsilon", er)

    gr = int(gr,2)
    er = int(er,2)

    print("gamma", gr)
    print("epsilon", er)

    pc = gr * er

    print("power consumption", pc)


def main():
    # day1input = "day1input.txt"
    # SonarSweep(day1input)

    # day2input = "day2input.txt"
    # Dive(day2input)

    # day2_5input = "day2input.txt"
    # Dive2(day2_5input)

    day3input = "day3input.txt"
    BinaryDiagnostic(day3input)


if __name__ == '__main__':

    main()