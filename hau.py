#!/usr/bin/python3
#Written By SchorchedVenom
#Date 10/14/2019
#www.github.com/SchorchedVenom/
#Hashcat Automation Utility

#Library Imports
import os
import sys
import subprocess
import platform
import time

#Platform Detection
operating = platform.system()

#Variables
hashCat = "hashcat"
clearValue = "clear"
linuxCat = "/usr/bin/hashcat"
hashCommand = ""

#Windows Hashcat Install location
if operating == "Windows":
    clearValue = "cls"
    os.system(str(clearValue))
    print("Windows Detected")
    print("In order to run the Hashcat Automation Utility we need to determine, ")
    print("where you have hashcat installed.")
    hashCat = input("Please enter the file path to your hashcat64.exe: ")
    time.sleep(5)
elif operating == "Linux":
    clearValue = "clear"
    os.system(str(clearValue))
    linuxCat = os.system("which hashcat")
    print("Linux Distro Detected")
    print(str(linuxCat) + " is the detected location of your hashcat installation")
    print("If you do not see a filepath then please reinstall hashcat.")
    time.sleep(5)
elif operating == "Darwin":
    clearValue = "clear"
    os.system(str(clearValue))
    print("OSx Detected")
    print("In order to run the Hashcat Automation Utility we need to determine, ")
    print("where you have hashcat installed.")
    hashCat = input("Please enter the file path to your hashcat executable: ")

#Hashcat Variables
deviceType = "1"
attackType = "0"
hashType = "0"
hashValue = ""
fileOutput = "output.txt"
outputType = "3"
workloadProfile = "2"
ruleType = "0"
rules = ""
wordList_1 = ""
wordList_2 = ""
attackMask = ""

#Hashcat Option Selection
#Device Choice
os.system(str(clearValue))
print("Before we begin we need to clear up a few things.")
fileOutput = input("Please enter the name you would like to call the file output: ")
print("Would you like to use your cpu, gpu or both to crack your hashes?")
deviceType = input("1.CPU \n2.GPU \n3.Both \nPlease respond with just the numerical value: ")
if deviceType == "1":
    deviceType = "1"
elif deviceType == "2":
    deviceType = "2"
elif deviceType == "3":
    deviceType = "1,2"
else:
    deviceType = "1"
#Workload Profile Choice
os.system(str(clearValue))
response = input("Would you like to change the default workload profile? (Y/N)")
if response == "Y" or response == "y":
    print("Changing the default profile will have effects on your system performance")
    directoryFile = [line.rstrip('\n') for line in open("./workloadprofiles.txt")]
    for i in directoryFile:
        print(str(i))
    workloadResponse = input("Please enter the numerical value associated with your desired profile: ")
    if workloadResponse == "1":
        workloadProfile = "1"
    elif workloadResponse == "2":
        workloadProfile = "2"
    elif workloadResponse == "3":
        workloadProfile = "3"
    elif workloadResponse == "4":
        workloadProfile = "4"
    else:
        workloadProfile = "2"
else:
    workloadProfile = "2"
#Attack Type Choice
os.system(str(clearValue))
x = 0
while x == 0:
    print("Now we need to determine the attack type hashcat will use.")
    response = input("1.Wordlist \n2.Wordlist + Rules \n3.Combination \n4.Brute Force \n5.Hybrid Wordlist + Mask \n6.Hybrid Mask + Wordlist \n Please enter your choice: ")
    if response == "1":
        os.system(str(clearValue))
        attackType = "0"
        print("For a Wordlist attack we need a wordlist.")
        wordList_1 = input("Please input the file path for your wordlist")
        x = 1
    elif response == "2":
        os.system(str(clearValue))
        attackType = "0"
        ruleType = "1"
        print("For a Wordlist + Rules attack we need a wordlist and a Rules list.")
        wordList_1 = input("Please input the file path for your wordlist: ")
        print("Rule lists are located in the hashcat rules folder your. ex: rules/best64.rule")
        rules = input("Please enter your desired rule list: ")
        x = 1
    elif response == "3":
        os.system(str(clearValue))
        attackType = "1"
        print("For a Combination attack we need two wordlists.")
        wordList_1 = input("Please enter the file path to your first wordlist: ")
        wordList_2 = input("Please enter the file path to your second wordlist: ")
        x = 1
    elif response == "4":
        os.system(str(clearValue))
        attackType = "3"
        print("For a Brute Force attack we need a Mask pattern for the attack to follow.")
        directoryFile = [line.rstrip('\n') for line in open("./charset.txt")]
        for i in directoryFile:
            print(str(i))
        print("To create a mask you use a ? followed by one of the letters seen above.")
        print("ex: ?u?l?l?l?l?l?d?s  this will produce a 8 character password starting with one Capital letter followed by \n5 Lower Case letters, then 1 digit and 1 symbol.")
        print("You can use a file containing multiple masks or enter your own mask.")
        attackMask = input("Please enter your attack mask: ")
        x = 1
    elif response == "5":
        os.system(str(clearValue))
        attackType = "6"
        print("For a Hybrid Wordlist + Mask attack you need a wordlist and a mask.")
        wordList_1 = input("Please enter the file path to your wordlist of choice: ")
        directoryFile = [line.rstrip('\n') for line in open("./charset.txt")]
        for i in directoryFile:
            print(str(i))
        print("To create a mask you use a ? followed by one of the letters seen above.")
        print("ex: ?u?l?l?l?l?l?d?s  this will produce a 8 character password starting with one Capital letter followed by \n5 Lower Case letters, then 1 digit and 1 symbol.")
        print("You can use a file containing multiple masks or enter your own mask.")
        attackMask = input("Please enter your attack mask: ")
        x = 1
    elif response == "6":
        os.system(str(clearValue))
        attackType = "7"
        print("For a Hybrid Mask + Wordlist attack you need a wordlist and a mask.")
        wordList_1 = input("Please enter the file path to your wordlist of choice: ")
        directoryFile = [line.rstrip('\n') for line in open("./charset.txt")]
        for i in directoryFile:
            print(str(i))
        print("To create a mask you use a ? followed by one of the letters seen above.")
        print("ex: ?u?l?l?l?l?l?d?s  this will produce a 8 character password starting with one Capital letter followed by \n5 Lower Case letters, then 1 digit and 1 symbol.")
        print("You can use a file containing multiple masks or enter your own mask.")
        attackMask = input("Please enter your attack mask: ")
        x = 1
    else:
        os.system(str(clearValue))
        print("You entered an unrecognized value of " + str(response))
        input("Press Enter to try again.")

#Hash Choice
os.system(str(clearValue))
print("We're almost done now its time to select your hash type you're trying to crack.")
print("To select the hash you are gonne be shown a list of every type of hash along with")
print("it's associated number.")
print("You are going to need to remember the number of your hash type then enter it when prompted.")
input("Press enter when you are ready.")
os.system(str(clearValue))
directoryFile = [line.rstrip('\n') for line in open("./hashtypes.txt")]
x = 1
y = 0
while y != 1:
    for i in directoryFile:
        if x != 10:
            print(str(i))
            x += 1
        else:
            x = 1
            input("Press Enter to Continue to next page.")
            os.system(str(clearValue))
    y = 1
print("In a second you will be prompted for your hash type value.")
time.sleep(3)
hashType = input("Please enter your hash type value: ")

#Hash File
os.system(str(clearValue))
print("Time for the last step")
print("We now need the hash(es) you mean to crack.")
print("Your input can either be an Individual hash or")
print("You can enter a file path to a file containing multiple hashes")
hashValue = input("Please Enter your Hash: ")

#Generate Hashcat command
os.system(str(clearValue))
print("Generating Hashcat Command Please Wait")
unfinishedCommand = str(hashCat) + " --quiet -o " + str(fileOutput) + " --outfile-format " + str(outputType) + " -w " + str(workloadProfile) + " -D " + str(deviceType) + " -a " + str(attackType) + " -m " + str(hashType) + str(hashValue)
if attackType == 0 and ruleType == 0:
    hashCommand = str(unfinishedCommand) + " " + str(wordList_1)
elif attackType == 0 and ruleType == 1:
    hashCommand = str(unfinishedCommand) + " " + str(wordList_1) + " -r " + str(rules)
elif attackType == 1:
    hashCommand = str(unfinishedCommand) + " " + str(wordList_1) + " " + str(wordList_2)
elif attackType == 3:
    hashCommand = str(unfinishedCommand) + " " + str(attackMask)
elif attackType == 6:
    hashCommand = str(unfinishedCommand) + " " + str(wordList_1) + " " + str(attackMask)
elif attackType == 7:
    hashCommand = str(unfinishedCommand) + " " + str(attackMask) + " " + str(wordList_1)
time.sleep(3)
print("Hashcat command generated!")
print("Command to be run: ")
print(str(hashCommand))
check = input("Would you like to run the command? (Y/N): ")
runCommand = 0
if check == "y" or check == "Y":
    runCommand = 1
else:
    print("Thank you for using this utility")
    time.sleep(2)
    print("Exiting in 3 seconds")
    time.sleep(3)
    SystemExit

#Run the Hashcat Command
os.system(str(clearValue))
print("Thank you for using this utility")
input("Press Enter to run the generated hashcat command: ")
os.system(str(hashCommand))