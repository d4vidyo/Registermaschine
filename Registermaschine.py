import sys
import time

class Instruction:
    def __init__(self, txt):
        self.befehl = txt[:3]
        self.modifikator = int(txt[3:])

freq = -1
if __name__ == "__main__":
    if(len(sys.argv)>1  ):
        clock = sys.argv[1]
        freq = 1/int(clock)
        print("Running at: ", clock, "Hz (Max)")

programmspeicher = [Instruction("HLT99")]

with open('text.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        if len(line)<1: continue
        programmspeicher.append(Instruction(line))

PC = 1
def increment():
    global PC
    PC += 1
datenspeicher = [0]

while True:
    befehl = programmspeicher[PC].befehl
    modifikator = programmspeicher[PC].modifikator
    print(PC, befehl)

    match befehl:
        case "ADD":
            datenspeicher[0] = datenspeicher[0] + datenspeicher[modifikator]
            increment()
        case "SUB":
            datenspeicher[0] = datenspeicher[0] - datenspeicher[modifikator]
            increment()
        case "MUL":
            datenspeicher[0] = datenspeicher[0] * datenspeicher[modifikator]
            increment()
        case "DIV":
            datenspeicher[0] = datenspeicher[0] / datenspeicher[modifikator]
            increment()
        case "LDA":
            datenspeicher[0] = datenspeicher[modifikator]
            increment()
        case "LDK":
            datenspeicher[0] = int(modifikator)
            increment()
        case "STA":
            if len(datenspeicher) < modifikator + 1:
                count = modifikator + 1 - len(datenspeicher)
                datenspeicher.extend([0] * count)
            datenspeicher[modifikator] = datenspeicher[0]
            increment()
        case "INP":
            if len(datenspeicher) < modifikator + 1:
                count = modifikator + 1 - len(datenspeicher)
                datenspeicher.extend([0] * count)
            datenspeicher[modifikator] = int(input("Eingabe: "))
            increment()
        case "OUT":
            print("Output: ", datenspeicher[modifikator])
            increment()
        case "HLT":
            break;
        case "JMP":
            PC = modifikator
        case "JEZ":
            if datenspeicher[0] == 0: PC = modifikator
            else: increment()
        case "JNE":
            if datenspeicher[0] != 0: PC = modifikator
            else: increment()
        case "JLZ":
            if datenspeicher[0] < 0: PC = modifikator
            else: increment()
        case "JLE":
            if datenspeicher[0] <= 0: PC = modifikator
            else: increment()
        case "JGZ":
            if datenspeicher[0] > 0: PC = modifikator
            else: increment()
        case "JGE":
            if datenspeicher[0] >= 0: PC = modifikator
            else: increment()
    if freq > 0 : time.sleep(freq)


input("\nPress enter to continue...")