#exit code 1 = invalid units entered
#exit code 2 = unrecognised gender
#exit code 3 = invalid licence entered
#exit code 4 = non-number mass
#exit code 5 = non-number time

#function for calculating BAC
def calcBAC(A, r, W, t):
    #error doing algorithm unless float cast first
    A = float(A)
    r = float(r)
    W = float(W)
    t = float(t)
    ans = A/(r*W)*100 -(0.00015*t)
    return ans

#test = calcBAC(5, 0.68, 60000, 1)

#print(test)

#main code starts
#taking input from users
#try blocks to dected invalid input for number values
gender = input("What gender are you (m/f)? ")
mass = input("Mass (Kg or lb): ")
try:
    mass = float(mass)
except ValueError:
    print("None number input")
    exit(4)
status = input("Status (FL?P?L): ")
time = input("Time (hours): ")
try:
    time = float(time)
except ValueError:
    print("None number time")
    exit(5)
drinks = input("Drinks (standard): ")
try:
    drinks = float(drinks)
except ValueError:
    print("None number drinks")
    exit(6)
units = input("Units (Kg or lb): ")

#converting entered mass value to grams
if(units == "Kg"):
    W = mass * 1000
elif(units == "lb"):
    W = mass * 453.592
else:
    print("Invalid units entered")
    exit(1)

#determing conversion factor for gender
if (gender == "m" or gender == "M"):
    r = 0.68
elif(gender == "f" or gender == "F"):
    r = 0.55
else:
    print("Unrecognised gender entered")
    exit(2)

#calculating A based on standard drinks entered
A = drinks * 10
#BAC calculated by calcBAC function from start of this file
BAC = calcBAC(A, r, W, time)

#print out BAC for user to see and for debugging
print("Estimated BAC", BAC)
if(status == "L" or status == "P"):
    if(BAC > 0):
        print("Licence cancelled, interlock device")
        exit(0)
    else:
        print("Safe to drive")
        exit(0)

#Inform the user if they are on an L or P licence what will happen if they drive
if(status == "FL"):
    if(BAC < 0.7):
        print("Licence cancelled, interlock device")
        exit(0)
    elif(BAC < 0.5 and BAC < 0.7):
        print("Fine and 10 demerit points")
        exit(0)
    else:
        print("OK to drive")
        exit(0)

#if not correct information the licence is invalid
print("Invalid licence") 
