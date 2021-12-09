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
    
    gr0 = 0
    gr1 = 0
    gr2 = 0
    gr3 = 0
    gr4 = 0

    er0 = 0
    er1 = 0
    er2 = 0
    er3 = 0
    er4 = 0

    with open(day3input, "r") as file:
        lines = file.readlines()
        file.close()
    for line in lines:
        index = list(line)
        if int(index[0]) == 0:
            count_zero0 += 1
        else:
            count_one0 += 1

        if int(index[1]) == 0:
            count_zero1 += 1
        else: 
            count_one1 += 1

        if int(index[2]) == 0:
            count_zero2 += 1
        else:
            count_one2 += 1

        if int(index[3]) == 0:
            count_zero3 += 1
        else:
            count_one3 += 1

        if int(index[4]) == 0:
            count_zero4 += 1
        else:
            count_one4 += 1

    if count_zero0 > count_one0:
        gr0 = 0
        er0 = 1
    else: 
        gr0 = 1
        er0 = 0
    
    if count_zero1 > count_one1:
        gr1 = 0
        er1 = 1
    else: 
        gr1 = 1
        er1 = 0

    if count_zero2 > count_one2:
        gr2 = 0
        er2 = 1
    else: 
        gr2 = 1
        er2 = 0

    if count_zero3 > count_one3:
        gr3 = 0
        er3 = 1
    else: 
        gr3 = 1
        er3 = 0

    if count_zero4 > count_one4:
        gr4 = 0
        er4 = 1
    else: 
        gr4 = 1
        er4 = 0

    gr = str(gr0) + str(gr1) + str(gr2) + str(gr3) + str(gr4)
    er = str(er0) + str(er1) + str(er2) + str(er3) + str(er4)

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

    day3input = "testday3input.txt"
    BinaryDiagnostic(day3input)


if __name__ == '__main__':

    main()