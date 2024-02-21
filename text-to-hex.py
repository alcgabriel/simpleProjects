
import os
import time


def clearScreen():
    if os.name == 'nt':
        _ = os.system('cls')
     
    else: 
        _ = os.system('clear')






#used to get input from the user
convertHex = input("Digite o texto que deseja converter para hexadecimal:") 
clearScreen()

print("O texto convertido para hexadecimal é: ", convertHex)
time.sleep(3)
clearScreen()

print("O resultado é.")
time.sleep(1)
clearScreen()

print("O resultado é..")
time.sleep(1)
clearScreen()

print("O resultado é...")
time.sleep(1)
clearScreen()

print("O resultado é....")
time.sleep(1)
clearScreen()


#the output from the input is converted to bytes
bytes = convertHex.encode()

# now converts the byts to hexadecimal
hexadecimal = bytes.hex()

#print the output
print("Resultado da conversão: ", hexadecimal)






