"""
Developer: Isaac Neace
Program: Binary Search

Description:
Program imports patient data into a list and prompts the user to search through the list.
The user enters the patient name and the program performs a binary search to find the
Patient name and where they are located in the file.

Date: 9/6/18
"""

#defines classes for list
class Patient():
    def __init__(self, name, contact, age, days, balance):
        self.name=name
        self.contact=contact
        self.age=age
        self.days=days
        self.balance=balance
    def getName(self):
        return self.name
    def getContact(self):
        return self.contact
    def getAge(self):
        return self.age
    def getDays(self):
        return self.days
    def getBalance(self):
        return self.balance

    def updateName(self, name):
        self.name=name
    def updateContact(self, contact):
        self.contact=contact
    def updateAge(self, age):
        self.age=age
    def updateDays(self, days):
        self.days = days
    def updateBalance(self, balance):
        self.balance = balance



PatientList = []

#Pulls values from .dat file and puts them into list
fp=open("Patient_Info-sorted.dat", "r")
fp.readline()
while True:
    line = fp.readline()
    if line =="":
        break
    line=line.strip() #strips all blank spaces in .dat file
    word=line=line.split()
    s=Patient (str(word[0]), str(word[1]), int(word[2]), int(word[3]), float(word[4]))
    PatientList.append(s) #adds edited values to new list

    
#Variables for binary search
found = False
value = raw_input("Enter a Patient name to search: ")
first = 0 #defines begining of list
last = len(PatientList) - 1 #defines end of list
count = 0 #Number of iterations


#Do a binary search to find the value that the user inputs
while first <= last:
    count = count + 1
    mid = (first + last)/2

    if value > (Patient.getName(PatientList[mid])):
        first = mid + 1
    elif value < (Patient.getName(PatientList[mid])):
        last = mid - 1
    elif value == (Patient.getName(PatientList[mid])):
        #Print result if found in the index
        found = True
        print(found)
        print "found at index", mid
        print "number of iterations: ", count
        print "Patient contact: ", Patient.getContact(PatientList[mid])
        print "Patient Age: ", Patient.getAge(PatientList[mid])
        print "Patient Days: ", Patient.getDays(PatientList[mid])
        print "Patient Balance: ", Patient.getBalance(PatientList[mid])
        break
    else:
        print(found)
        print "Value not found"
        break

