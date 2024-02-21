import os
import time


def clearScreen():
    if os.name == 'nt':
        _ = os.system('cls')
     
    else: 
        _ = os.system('clear')






#used to get input from the user
convertHex = input("Type the text you want to convert to hexadecimal:") 

clearScreen()


#the output from the input is converted to bytes
bytes = convertHex.encode()

# now converts the byts to hexadecimal
hexadecimal = bytes.hex()




print("The text converted into hexadecimal is: ", convertHex)
time.sleep(3)
clearScreen()

print("The result is.")
time.sleep(1)
clearScreen()

print("The result is..")
time.sleep(1)
clearScreen()

print("The result is...")
time.sleep(1)
clearScreen()

print("The result is....")
time.sleep(1)
clearScreen()



#print the output
print("result of conversion:", hexadecimal)


time.sleep(5)
clearScreen()

hexNumber = input("Now if you want to convert a NUMBER to hex, type the number(WHITOUT SPACES), if not, press <CTRL+C> to exit:")


clearScreen()

#converts the str to int and then to hex
print("O número convertido para hexadecimal é: ", hex(int(hexNumber)))
