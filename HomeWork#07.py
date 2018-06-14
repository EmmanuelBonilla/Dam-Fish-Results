#-------------------------------------------------------------------
# Emmanuel Bonilla
# Washington State University, Tri-Cities
# CptS111: Introduction to Algorithmic Problem Solving
# Summer 2016: Homework 07
# System: Python v3.5.1 IDLE (MS Windows OS)
#-------------------------------------------------------------------

from math import *
from os import getcwd


#Purpose: Read lines from input file, remove the carriage return thru rawline loop
#Parameters: Has to be an existing file
#Return: Read lines from the opened file
def readLinesFromFile(filename):
    inFile = open(filename,'r')
    RawLines = inFile.readlines()
    inFile.close()
    Lines = []
    
    for rawline in RawLines:
        Lines.append(rawline[:-1])
        
    return Lines

#purpose: Receive a passed-in list of strings
#parameters: only excecute program when valid integer is entered
#return: Integer, from a valid user entry
def userListMenu(itemList,zeroFlag = True):
    userNum = 0
    
    if zeroFlag:
        print("\n0: Quit/Nothing")
    totalItems = len(itemList)
    
    if totalItems:
        for i in range(totalItems):
            print("{0}: {1}".format(i + 1, itemList[i]))

    badEntry = True
    while badEntry:
        try:
            userNum = (int(eval(input("\nPlease pick an option: "))))
            if (userNum >= 1 and userNum <= totalItems) or (zeroFlag and userNum ==0):
                badEntry = False
            else:
                print("\nPlease select a valid choice")
        except:
            print("\nInvalid Entry")
            
    return userNum

#purpose: Find the average of two data points
#parameters: integers only > 0 
#return: the average of integers given
def myAvg(sumData,numData):
    theAvg = None
    
    if numData > 0:
        theAvg = sumData / numData
        
    return theAvg

#purpose: Find the Standard Deveation of 3 different inputs
#parameters: positive integers only
#return: Standard Deveation
def myStdDev(sumData,sqrData,numData):
    theStdDev = None
    
    if numData > 1:
        theStdDev = sqrt((sqrData - sumData ** 2 / numData) / (numData - 1))
        
    return theStdDev

#purpose: Find the statisical data of the total list
#parameters: Postitive integers only
#return: total numbers, average, standard deviation, max #, min #
def statData(numList):
    numx = len(numlist)
    sumX, sqrX, minX, MaxX = 0, 0, None, None
    
    if numX:
        for X in numList:
            sumX = sumX + X
            sqrX = sqrX + X ** 2
            if minX == None or X < minX: minX = X
            if maxX == None or X > maxX: maxX = X
            
    avgX = myAvg(sumX,numX)
    StdDevX = myStdDev(sumX,sqrX,numX)
    results = [numX,avgX,stdDevX,maxX,minX]
    
    return results
                
def main():
    myPath = getcwd() + "\\"
    fileExt = ".txt" #  Text file extension
    
    theFishList = readLinesFromFile (myPath + "fishInfo" + fileExt)# process the fish info file
    totalFish = len(theFishList)
    
    fileRecords = readLinesFromFile (myPath + "damInfo" + fileExt)# process the Dam info file
    theDamList = []
    
    for iRec in fileRecords:
        theDamList.append(iRec.split(','))
    totalDams = len(theDamList)

    menuChoices =["Dam Statistics:","Fish Statistics:","Load a Data File:"]
    menuSelect = 3
   
    #loop until user has completed task
    while menuSelect:
        if menuSelect == 1:#This will give you a list of all the fish in a specific dam.
            tmpList = []
            for Dam in theDamList:
                tmpList.append(Dam[0])
                
            damSelect = userListMenu(tmpList, False)
            numZ, sumZ, sqrZ, minZ, maxZ = [],[],[],[],[]
            totalFish = len(theFishList)
            
            for iFish in range (totalFish):
                numZ.append(0)
                sumZ.append(0)
                sqrZ.append(0)
                minZ.append(None)
                maxZ.append(None)
            
            for iRec in theDataList:
                if iRec[0] == damSelect:
                    for iFish in range(totalFish):
                        if type(iRec[2 + iFish]) == type(0):
                            numZ[iFish] = numZ[iFish] + 1
                            sumZ[iFish] = sumZ[iFish] + iRec[2+iFish]
                            sqrZ[iFish] = sqrZ[iFish] + iRec[2+iFish]**2
                            if minZ[iFish] == None or iRec[2+iFish] < minZ[iFish]:
                                minZ[iFish] = iRec[2 + iFish]
                            if maxZ[iFish] == None or iRec[2 + iFish] > maxZ[iFish]:
                                maxZ[iFish] = iRec[2+iFish]

            #open and label filename and print data to file
            fileName = myPath + "D{0:#02}F{1:#02}W{2:#02}_results.txt".format(iFish + 1, damSelect, weekNum)
            outFile = open(fileName, 'w')
            print("The Dam you selected is ", theDamList[damSelect-1][0],file=outFile )
            print("\nFish Species,       # of days,  Average, Standard Deviation, Max Amount, Min Amount ",file=outFile)
            print("-" * 84,file=outFile)
            
            for iFish in range(totalFish):
                avgZ = myAvg(sumZ[iFish],numZ[iFish])
                stdDevZ = myStdDev(sumZ[iFish],sqrZ[iFish],numZ[iFish])
                                   
                if numZ[iFish]:
                    strLine = "{0:21}{1:4}{2:14.1f}{3:14.2f}{4:15}{5:12}".format(theFishList[iFish],numZ[iFish],avgZ,stdDevZ,maxZ[iFish],minZ[iFish])
                    print(strLine,file=outFile)
                    
            outFile.close()

        elif menuSelect == 2:#This will give you a list of all the dams and the specific fish.
            tmpList = []
            
            for Fish in theFishList:
                tmpList.append(Fish)
                
            fishSelect = userListMenu(tmpList, False)
            numZ,sumZ, sqrZ, minZ, maxZ = [],[],[],[],[]
            totalDam = len(theDamList)
            fishDataOffset = fishSelect + 1

            for iDam in range (totalDam):#initialize calculated lists 
                numZ.append(0)
                sumZ.append(0)
                sqrZ.append(0)
                minZ.append(None)
                maxZ.append(None)
                
            for iRec in theDataList:#process data file
                iDam = iRec[0]-1
                if type(iRec[fishDataOffset]) == type(0):
                    numZ[iDam] = numZ[iDam] + 1
                    sumZ[iDam] = sumZ[iDam] + iRec[fishDataOffset]
                    sqrZ[iDam] = sqrZ[iDam] + iRec[fishDataOffset]**2
                    if minZ[iDam] == None or iRec[fishDataOffset] < minZ[iDam]:
                        minZ[iDam] = iRec [fishDataOffset]
                    if maxZ[iDam] == None or iRec[fishDataOffset] > maxZ[iDam]:
                        maxZ[iDam] = iRec[fishDataOffset]

            #calculate and display data in new txt file
            fileName = myPath + "D{0:#02}F{1:#02}W{2:#02}_results.txt".format(iDam + 1, fishSelect, weekNum)
            outFile = open(fileName, 'w')
            print("The fish you selected is: ", theFishList[fishSelect-1],file=outFile )
            print("\nDam Name:           # of days,   Average, Standard Deviation, Max Amount, Min Amount ",file=outFile)
            print("-" * 84,file=outFile)


            for iDam in range(totalDam):
                avgZ = myAvg(sumZ[iDam],numZ[iDam])
                stdDevZ = myStdDev(sumZ[iDam],sqrZ[iDam],numZ[iDam])

                if numZ[iDam]:
                    strLine = "{0:21}{1:4}{2:14.1f}{3:14.2f}{4:15}{5:12}".format(theDamList[iDam][0],numZ[iDam],avgZ,stdDevZ,maxZ[iDam],minZ[iDam])
                    print(strLine,file=outFile)

            outFile.close()

        elif menuSelect == 3:#This will input client file
            badFile = True
            
            while badFile:
                ueFileName = input("\nPlease enter a data file name (example:week##data): ")
                
                try:
                    weekNum = int(ueFileName[4:-4])
                    pgnFile = open(myPath + ueFileName + fileExt, 'r')
                    badFile = False
                except:
                    print('\n"Invalid File Name, Please Try Again."')
                
            fileRecords = pgnFile.readlines()
            pgnFile.close()
            theDataList = []
            
            for iRec in fileRecords:
                tmpList = []
                iCOl = 0
                
                for iFld in iRec [:-1].split(','):
                    if iFld.isnumeric():
                        dataX = eval(iFld)
                    else:
                        dataX = iFld
                        
                    tmpList.append(dataX)
                theDataList.append(tmpList)
        menuSelect = userListMenu(menuChoices)
    return

main()
