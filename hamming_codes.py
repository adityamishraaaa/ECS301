#Aditya Mishra - 21013

import random
from typing import List

# Using Hamming codes to detect and correct errors

# Function for calculating the number of redundant bits in the given binary string
# using the formula 2^r >= m + r + 1
def RedundantBits(m:int):
    # Loop through possible values of r to find the smallest value satisfying the formula
    for r in range(m):
        if (2**r >= m + r + 1):
            return r  # Returns the number of redundant bits

# Finding a modified string with the number of bits = n + r + 1
def PositionRedundantBits(givenString , r):
    j = 0
    k = 1
    m = len(givenString)
    par = 
    # Iterate through the positions to determine where to place the parity bits
    for i in range(1, m + r + 1):
        if (2**j == i):
            par = par + 0
            j += 1
        else:
            # Append the data backwards because the 0th position in binary is the last in the string
            par = par + givenString[-1 * k]
            k += 1
    # Reverse the modified string to get the correct order of parity bits
    return par[::-1]

# Calculating and adding parity bits to their specified positions
def CalculateParityBits(modifiedString , r):
    n = len(modifiedString)
    # Iterate through each parity bit position
    for i in range(r):
        binVal = 0
        # Iterate through each bit position
        for j in range(1, n + 1):
            if (j & (2**i) == ((2**i))):
                # XOR the bits in significant positions
                binVal = binVal ^ int(modifiedString[-1 * j])
        # Update the modified string with the correct parity bit at its specified position
        modifiedString = modifiedString[:n-(2**i)] + str(binVal) + modifiedString[n - (2**i) + 1:]
    return modifiedString

# Detecting errors in the received string
def DetectError(modifiedString , numberOfRedBit):
    n = len(modifiedString)
    res = 0
    # Iterate through each parity bit position
    for i in range(numberOfRedBit):
        val = 0
        # Iterate through each bit position
        for j in range(1, n + 1):
            if (j & (2**i) == (2**i)):
                # XOR the bits in significant positions
                val = val ^ int(modifiedString[-1 * j])
        res = res + val * (10**i)
    # Convert the binary result to decimal to get the position of the error bit
    return int(str(res),2)

# Function for adding single-bit errors
def AddRandomNoise(binaryNumber):
    # Select a random index and change its value randomly to introduce noise
    i = random.randint(0, len(binaryNumber) - 1)
    charList = list(binaryNumber)
    charList[i] = random.randint(0,1)
    binaryNumber = .join(str(e) for e in charList)
    return binaryNumber

##########################################################
# Main Code
##########################################################

data = 
while True: # Loop to check if there is a wrong binary input
    data = input("Enter binary number ")
    correctInput = True
    # Validate the input to ensure it contains only binary digits (0 or 1)
    for num in data:
        if (num == 0 or num == 1):
            # Continue if the current bit is valid
            continue
        else:
            # Prompt for input again if it is not binary
            correctInput = False
            break
    if (correctInput == False):
        print("Wrong Input! Try again")
    else:
        break

m = len(data)
r = RedundantBits(m)
# Get the modified string with parity bits
modifiedString = PositionRedundantBits(data, r)
modifiedString = CalculateParityBits(modifiedString , r)
print("Transmitted data is: " + modifiedString)

# Add random noise to the transmitted data
modifiedString = AddRandomNoise(modifiedString)
# Detect and correct errors in the received data
correct = DetectError(modifiedString , r)
if correct == 0:
    pass
else:
    listString = list(modifiedString)
    # Toggle the bit at the detected error position to correct the error
    if (listString[len(listString) - correct] == 0):
        listString[len(listString) - correct] = 1
    else:
        listString[len(listString) - correct] = 0
    modifiedString = "".join(listString)

print("Received data is: " + modifiedString)

#Aditya Mishra - 21013