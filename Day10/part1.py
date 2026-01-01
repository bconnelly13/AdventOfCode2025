with open("input.txt") as f:
    lines = f.readlines()

# Preprocess input
allLights = []
allButtons = []
for line in lines:
    endOfLights = line.index("]")
    lineLights = line[1:endOfLights]

    startOfVoltages = line.index("{")
    buttonsString = line[endOfLights+1:startOfVoltages].strip()
    lineButtons = [lineButton.strip("()") for lineButton in buttonsString.split(" ")]
    
    lightsBinary = ""
    for c in lineLights:
        if c == ".":
            lightsBinary += "0"
        else:
            lightsBinary += "1"
    
    allLights.append(lightsBinary)

    machineButtons = []
    for button in lineButtons:
        binaryButton = "0" * len(lightsBinary)
        binaryButtonList = list(binaryButton)
        buttonNums = button.split(",")
        for buttonNum in buttonNums:
            binaryButtonList[int(buttonNum)] = "1"
        binaryButtonStr = "".join(binaryButtonList)
        machineButtons.append(binaryButtonStr)
    allButtons.append(machineButtons)

# Calcuate min for each machine
total = 0
for i in range(len(allLights)):
    lights = allLights[i]
    buttons = allButtons[i]

    minButtonPresses = None
    for j in range(2 ** len(buttons)):
        binaryNum = bin(j)[2:]
        for k in range(len(buttons) - len(binaryNum)):
            binaryNum = "0" + binaryNum
        counts = [0 for _ in range(len(lights))]
        for k in range(len(binaryNum)):
            if binaryNum[k] == "1":
                buttonInfo = buttons[k]
                for l in range(len(buttonInfo)):
                    lightNum = int(buttonInfo[l])
                    counts[l] += lightNum
        
        # Apply mod 2 operator to counts
        for k in range(len(counts)):
            counts[k] = counts[k] % 2
        
        numButtonPresses = sum(1 for char in binaryNum if char == "1")
        resultLights = "".join([str(count) for count in counts])
        if resultLights == lights:
            if (not minButtonPresses) or (numButtonPresses < minButtonPresses):
                minButtonPresses = numButtonPresses
    
    total += minButtonPresses

print("Total:", total)


