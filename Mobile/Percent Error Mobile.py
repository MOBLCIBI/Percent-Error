def menu():
    choice = input("Type and Enter 'd' for a data analysis or 'p' for a single calculation: ")
    places = 0
    badInput = True
    while badInput:
        try:
            places = "{0:."+str(int(input("\nType and Enter the number of decimal places (1-14) would you like displayed: ")))+"f}"
            badInput = False
        except ValueError:
            badInput = True
    if choice.lower() == "d":
        dataFile = open("/storage/emulated/0/Download/Data.txt", "r")
        resultsFile = open("/storage/emulated/0/Download/Results.txt", "w+")
        output = ""
        dataList = []
        print("\n###################### START RESULTS #######################\n")
        for line in dataFile:
            dataList.append(line)
        while dataList:
            text = False
            while not text:
                try:
                    float(dataList[0])
                    text = True
                except ValueError:
                    if dataList[0] != "\n":
                        output += dataList[0]+"\n"
                        print(dataList.pop(0))
                    else:
                        del dataList[0]
                    if not dataList:
                        text = True
            if dataList:
                result = str("Percent Error:\n"+str(places.format((100*((float(dataList[0]))-(float(dataList[1]))))/(float(dataList[1]))))+" %\n")
                output += result+"\n"
                print(result)
                dataList = dataList[2:]
        print("\n####################### END RESULTS ########################\n")
        resultsFile.write(output)
        resultsFile.close()
        menu()
    else:
        measured = 0
        theoretical = 0
        badInput = True
        while badInput:
            try:
                measured = float(input("\nMeasured Value: "))
                badInput = False
            except ValueError:
                badInput = True
        badInput = True
        while badInput:
            try:
                theoretical = float(input("Theoretical Value: "))
                badInput = False
            except ValueError:
                badInput = True
        print("Percent Error: "+str(places.format(((100*(measured-theoretical))/theoretical))),"%\n")
        menu()
    
menu()
