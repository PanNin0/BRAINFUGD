# ---------------------------

# Brainfugd v1.0

# ---------------------------

# Config

# Supported OS
# 'windows', 'linux' and 'mac'

system = 'windows'

# Code Types
# 'manual' - Will prompt the user to type in code on boot
# 'automatic' - Will automatically run code stored under the 'autocode' variable

codetype = 'manual'
autocode = ''

# ---------------------------

# Extensions

import random as rnd
import os
import time

# ---------------------------

# Var Setup

alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~', '\\', '|']

memory = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # The 16 allowed bits
bracketsaves = [] # Saves where in the code brackets have been placed
selected = 0 # The currently selected bit
output = 0 # The number most recently output
prog = 0 # Which letter of the code the program is reading
stroutput = '' # String output
userinput = '' # Used for the ? to store user inputs

# ---------------------------

# Logic

if (codetype == 'manual'): # Manual setting for codetype

    code = str(input('Type Code > '))

elif (codetype == 'automatic'): # Automatic setting for codetype

    code = autocode

while (prog < len(code)): # Repeats until the code either hits an end or reaches an 'e'
   
   # Basic Commands
   
   # ---------------------------
   
    if (code[prog] == '+'): # + command (Adds 1 to the selected bit)
        memory[selected] += 1
   
    elif (code[prog] == '-'): # - command (Subtracts 1 from the selected bit)
        memory[selected] += -1
   
    elif (code[prog] == '>'): # > command (Moves selected bit 1 to the right)
        selected += 1
   
    elif (code[prog] == '<'): # < command (Moves selected bit 1 to the left)
        selected += -1
   
    elif (code[prog] == '.'): # . command (Sets output number to selected bit)
        output = memory[selected]
        if (memory[selected] <= 68):
            stroutput = stroutput + alphabet[output]
   
    elif (code[prog] == ','): # , command (Generates a random number between 1 and 10)
        memory[selected] = rnd.randint(1,10)
        print('Random output - ' + str(memory[selected]))
    
    elif (code[prog] == '?'): # ? command (Gives user a prompt using the stroutput that will then be replaced by the users input)
        
        userinput = input(stroutput)
        stroutput = userinput.upper()
    
    elif (code[prog] == '/'): # ! command (Replaces memory with the first 16 didgets of the stroutput)
        
        strread = 0
        
        while (strread < 16 and strread != len(stroutput)):
            
            memory[strread] = int(alphabet.index(stroutput[strread])) # Essentially will replace a given index of the memory with the index of the nth letter of stroutput (if that makes sense, this comment will likely be updated to better explain this piece of code)
            
            strread += 1
    
    elif (code[prog] == '!'): # ! command (Clears memory)
        
        for n in range(16):
            
            memory[n] = 0
    
    elif (code[prog] == '@'): # @ command (Clears stroutput)
    
        stroutput = ''
        
    elif (code[prog] == '$'): # $ (Clears output)
        
        output = 0
    
    elif (code[prog] == '#'): # # command (Prints the stroutput)
        
        print(stroutput) # I thought it'd be funny to put a huge explanation here but that seems like a waste of time and space
    
    elif (code[prog] == 'o'): # o command (Prints the current output)

        print(output)
    
    elif (code[prog] == '`'): # ` (Prints the data being stored by the program)
        print('Memory : ', memory, '\nBrackets : ', bracketsaves, '\nSelected Byte : ', selected, '\nOutput : ', output, '\nCode Selected : ', prog, '\nString Output : ', stroutput, '\nUser Input : ', userinput)

    elif (code[prog] == '*'): # * command (Clears the screen)

        if (system == 'windows'): # Clear code when running Windows
            os.system('CLS')

        elif (system == 'linux' or os == 'mac'): # Clear code when running Mac or Linux
            os.system('clear')
    
    elif (code[prog] == 'p'): # p command (Pauses program for a 100th of a second)

        time.sleep(0.01)

    # ---------------------------
    
    # LOOPS KEEP QUARANTINED
    
    # ---------------------------
   
    elif (code[prog] == '['): #[ command (Begins a loop that ends once the currently selected bit hits 0)
        bracketsaves.append(prog)
   
    elif (code[prog] == ']'): #] command (If selected bit = 0 then end loop, if not go back to the start of the loop)
        if (memory[selected] != 0):
            prog = bracketsaves[len(bracketsaves) - 1] # If selected bit is 0 (end loop)
        else:
            bracketsaves.pop(len(bracketsaves) - 1) # Selected bit is not 0 (go back to start of loop)
    
    # ---------------------------
   
    elif (code[prog] == 'e'): #e command (ends code instantaniously)
        prog = len(code)
   
    # ---------------------------

    # ANTICRASH DO NOT REMOVE

    # ---------------------------
   
    if (selected == 16):
        selected = 0
    elif (selected == -1):
        selected = 15
   
    # ---------------------------
   
    prog += 1 # Move to next letter in the code

# ---------------------------

print('> End (Timing out in 5 minutes)') # End of program
time.sleep(300)
# ---------------------------
