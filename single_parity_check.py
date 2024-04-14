# Aditya Mishra - 21013

import random

binaryNumber = '' # Global variable for binary number

# Initially, the even parity of 1 is set to true, assuming that the initial count of 1s is even.
# Sender's end
while True: # Loop to check wrong binary input
    binaryNumber = input("Enter binary number ")
    correctInput = True
    for num in binaryNumber:
        if (num == '0'):
            # if current bit is 0 do nothing
            continue
        elif (num == '1'):
            # if current bit is 1, change parity from even to odd and odd to even
            evenParity = not evenParity
        else:
            # if input is not 0 or 1, ask for input again
            correctInput = False
            break
    if (correctInput == True):
        break
    print("Wrong Input! Try again")
parityBit = '' # global variable for the bit to be added to the binary string
# Keeping the parity of 1 even
if (evenParity):
    parityBit = '0'
else:
    parityBit = '1'

# Adding the parity bit to binary number
binaryNumber += parityBit
print("Transmitted binary string is: " + binaryNumber)

# Randomly adding noise to the string
i = random.randint(0, len(binaryNumber) - 1)
charList = list(binaryNumber)
charList[i] = str(random.randint(0,1)) 
binaryNumber = ''.join(charList)

# Receiver's end
checkParity = True
for bit in binaryNumber:
    if (num == '0'):
        continue
    else:
        checkParity = not checkParity
print("Received binary string is: " + binaryNumber)
if (checkParity):
    print("No errors in parity of 1")
else:
    print("Error found in parity of 1")

#Aditya Mishra - 21013