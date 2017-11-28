#!/usr/bin/python
# -*- coding: utf-8 -*-

############## IMPORTS ##################

from __future__ import print_function
from os import path
from sys import argv, exit
from colorama import init as initColorama
from colorama import Fore, Style
from struct import pack
from binascii import unhexlify as unHex

#########################################

######### CROSS-PYTHON HACK #############
try:
    input = raw_input  # For Python 2
except NameError:
    pass  # For Python 3
#########################################

# Init colorama module
initColorama()

######### CONSTANTS #########

# Instruction table dictionary
instructionTable = {
    'nop': 0,
    'stax b': 2,
    'inx b': 3,
    'inr b': 4,
    'dcr b': 5,
    'rlc': 7,
    'dad b': 9,
    'ldax b': 10,
    'dcx b': 11,
    'inr c': 12,
    'dcr c': 13,
    'rrc': 15,
    'stax d': 18,
    'inx d': 19,
    'inr d': 20,
    'dcr d': 21,
    'ral': 23,
    'dad d': 25,
    'ldax d': 26,
    'dcx d': 27,
    'inr e': 28,
    'dcr e': 29,
    'rar': 31,
    'rim': 32,
    'inx h': 35,
    'inr h': 36,
    'dcr h': 37,
    'daa': 39,
    'dad h': 41,
    'dcx h': 43,
    'inr l': 44,
    'dcr l': 45,
    'cma': 47,
    'sim': 48,
    'inx sp': 51,
    'inr m': 52,
    'dcr m': 53,
    'stc': 55,
    'dad sp': 57,
    'dcx sp': 59,
    'inr a': 60,
    'dcr a': 61,
    'push b': 197,
    'rst 0': 199,
    'rz': 200,
    'ret': 201,
    'rst 1': 207,
    'rnc': 208,
    'pop d': 209,
    'push d': 213,
    'rst 2': 215,
    'rc': 216,
    'rst 3': 223,
    'rpo': 224,
    'pop h': 225,
    'xthl': 227,
    'push h': 229,
    'rst 4': 231,
    'rpe': 232,
    'pchl': 233,
    'xchg': 235,
    'rst 5': 239,
    'rp': 240,
    'pop psw': 241,
    'di': 243,
    'push psw': 245,
    'rst 6': 247,
    'rm': 248,
    'sphl': 249,
    'ei': 251,
    'rst 7': 255,
    'cmc': 63,
    'mov b,b': 64,
    'mov b,c': 65,
    'mov b,d': 66,
    'mov b,e': 67,
    'mov b,h': 68,
    'mov b,l': 69,
    'mov b,m': 70,
    'mov b,a': 71,
    'mov c,b': 72,
    'mov c,c': 73,
    'mov c,d': 74,
    'mov c,e': 75,
    'mov c,h': 76,
    'mov c,l': 77,
    'mov c,m': 78,
    'mov c,a': 79,
    'mov d,b': 80,
    'mov d,c': 81,
    'mov d,d': 82,
    'mov d,e': 83,
    'mov d,h': 84,
    'mov d,l': 85,
    'mov d,m': 86,
    'mov d,a': 87,
    'mov e,b': 88,
    'mov e,c': 89,
    'mov e,d': 90,
    'mov e,e': 91,
    'mov e,h': 92,
    'mov e,l': 93,
    'mov e,m': 94,
    'mov e,a': 95,
    'mov h,b': 96,
    'mov h,c': 97,
    'mov h,d': 98,
    'mov h,e': 99,
    'mov h,h': 100,
    'mov h,l': 101,
    'mov h,m': 102,
    'mov h,a': 103,
    'mov l,b': 104,
    'mov l,c': 105,
    'mov l,d': 106,
    'mov l,e': 107,
    'mov l,h': 108,
    'mov l,l': 109,
    'mov l,m': 110,
    'mov l,a': 111,
    'mov m,b': 112,
    'mov m,c': 113,
    'mov m,d': 114,
    'mov m,e': 115,
    'mov m,h': 116,
    'mov m,l': 117,
    'hlt': 118,
    'mov m,a': 119,
    'mov a,b': 120,
    'mov a,c': 121,
    'mov a,d': 122,
    'mov a,e': 123,
    'mov a,h': 124,
    'mov a,l': 125,
    'mov a,m': 126,
    'mov a,a': 127,
    'add b': 128,
    'add c': 129,
    'add d': 130,
    'add e': 131,
    'add h': 132,
    'add l': 133,
    'add m': 134,
    'add a': 135,
    'adc b': 136,
    'adc c': 137,
    'adc d': 138,
    'adc e': 139,
    'adc h': 140,
    'adc l': 141,
    'adc m': 142,
    'adc a': 143,
    'sub b': 144,
    'sub c': 145,
    'sub d': 146,
    'sub e': 147,
    'sub h': 148,
    'sub l': 149,
    'sub m': 150,
    'sub a': 151,
    'sbb b': 152,
    'sbb c': 153,
    'sbb d': 154,
    'sbb e': 155,
    'sbb h': 156,
    'sbb l': 157,
    'sbb m': 158,
    'sbb a': 159,
    'ana b': 160,
    'ana c': 161,
    'ana d': 162,
    'ana e': 163,
    'ana h': 164,
    'ana l': 165,
    'ana m': 166,
    'ana a': 167,
    'xra b': 168,
    'xra c': 169,
    'xra d': 170,
    'xra e': 171,
    'xra h': 172,
    'xra l': 173,
    'xra m': 174,
    'xra a': 175,
    'ora b': 176,
    'ora c': 177,
    'ora d': 178,
    'ora e': 179,
    'ora h': 180,
    'ora l': 181,
    'ora m': 182,
    'ora a': 183,
    'cmp b': 184,
    'cmp c': 185,
    'cmp d': 186,
    'cmp e': 187,
    'cmp h': 188,
    'cmp l': 189,
    'cmp m': 190,
    'cmp a': 191,
    'rnz': 192,
    'pop b': 193,
}

# Instruction table dictionary that expects a secondary parameter (8-bit)
varInstructionTable_EigthBit = {
    'mvi b,': 6,
    'mvi c,': 14,
    'mvi d,': 22,
    'mvi e,': 30,
    'mvi h,': 38,
    'mvi l,': 46,
    'sta': 50,
    'mvi m,': 54,
    'lda': 58,
    'mvi a,': 62,
    'adi': 198,
    'aci': 206,
    'out': 211,
    'sui': 214,
    'in': 219,
    'sbi': 222,
    'ani': 230,
    'xri': 238,
    'ori': 246,
    'cpi': 254
}
# Instruction table dictionary that expects a secondary parameter (16-bit)
varInstructionTable_SixteenBit = {
    'lxi b,': 1,
    'lxi d,': 17,
    'lxi h,': 33,
    'shld': 34,
    'lhld': 42,
    'lxi sp,': 49,
    'jnz': 194,
    'jmp': 195,
    'cnz': 196,
    'jz': 202,
    'cz': 204,
    'call': 205,
    'jnc': 210,
    'cnc': 212,
    'cc': 220,
    'jc': 218,
    'jpo': 226,
    'cpo': 228,
    'jpe': 234,
    'cpe': 236,
    'jp': 242,
    'cp': 244,
    'jm': 250,
    'cm': 252
}

helpArgVariants = ['-h', '--h', '-help', '--help']

######### FUNCTIONS #########
# Print a small ASCII art banner


def banner():
    print(Style.DIM)
    print('     ___________________________')
    print('    /                           /\\')
    print('   /     sadboyzvone\'s        _/ /\\')
    print('  /        Intel 8080        / \/')
    print(' /         Assembler         /\\')
    print('/___________________________/ /')
    print('\___________________________\/')
    print(' \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\'
          + Style.RESET_ALL + Style.BRIGHT)
    print(Fore.WHITE + '\nPowered by ' + Fore.BLUE + 'Pyt'
          + Fore.YELLOW + 'hon' + Fore.WHITE
          + '\nCopyright (C) 2017, Zvonimir Rudinski')

# Print usage information


def printHelp():
    print('\nThis ' + Fore.BLUE + 'Intel' + Fore.WHITE
          + ' 8080 assembler was made for ' + Fore.BLUE + 'Project '
          + Fore.YELLOW + 'Week' + Fore.WHITE + ' at my school.')
    print('It is written in ' + Fore.BLUE + 'Pyt' + Fore.YELLOW + 'hon'
          + Fore.WHITE)
    print('Modules: ' + Fore.RED + 'Co' + Fore.BLUE + 'lo'
          + Fore.YELLOW + 'ra' + Fore.GREEN + 'ma' + Fore.WHITE)
    print('\nPass a file path as an arguement.')


# Main function
def run(fileNameArg):
    banner()  # Print banner

    # File name
    fileName = None

    # Variable and label info
    labelMap = {}
    variableMap = {}

    # Program counter
    # TODO: If there is an ORG instruction change the PC to start from the specified address
    programCounter = 0

    try:
        if fileNameArg in helpArgVariants:
            printHelp()  # Print help then exit
            exit(0)
        else:
            fileName = fileNameArg  # Argument is provided
            print('Trying to open ' + Fore.YELLOW +
                  '\'' + fileName + '\'' + Fore.WHITE)
            if path.isfile(fileName) is False:  # Check if the file exists
                print(Fore.RED + 'Fatal error: ' + Fore.WHITE +
                      'File not found: ' + Fore.YELLOW + '\'' + fileName + '\'')
                raise IOError  # It doesn't raise an exception

        # Read in the source code from the file
        with open(fileName, 'r') as sourceFile:
            sourceCode = sourceFile.readlines()

        # Strip the newlines
        sourceCode = map(lambda sc: sc.strip(), sourceCode)

        # Start compiling the code
        with open(fileName + '.rom', 'wb+') as romFile:

            # Check the line
            for (i, scLine) in enumerate(sourceCode):
                scLine = scLine.lower()  # Turn it to lower case for easier lookup

                # Check if it's a label
                if len(scLine.split(':')) > 1:
                    print('Updating labels')
                    labelMap[scLine.split(':')[0]] = unHex(
                        str(programCounter).zfill(4))
                    continue

                # Check if it's in the instruction table
                if scLine in instructionTable:
                    # Write the opcode
                    romFile.write(pack('B', instructionTable[scLine]))
                    programCounter += 1  # 1 byte
                    continue

                elif scLine.split(' ')[1] == 'equ':
                    # Check if it's a variable declaration
                    if int(scLine.split(' ')[2]) >= 2 ** 8:
                        # Number is out of bounds for Intel 8080
                        print(Fore.RED + 'Variable too large: ' +
                              scLine + ' : Line ' + str(i + 1))
                        raise SyntaxError
                    variableMap[scLine.split(' ')[0]] = unHex(scLine.split(
                        ' ')[2].ljust(4, '0'))  # It is, save it to a dictionary
                    print('Updating variables')
                    continue

                else:
                    # Check if it's in a instruction table (8-bit)
                    for tableKey in varInstructionTable_EigthBit.keys():
                        if scLine.startswith(tableKey):
                            # Write the opcode
                            romFile.write(
                                pack('B', varInstructionTable_EigthBit[tableKey]))
                            try:
                                # Check if it's a variable
                                variable = (scLine.split(',')[1].strip(
                                ) if ',' in scLine else scLine.split()[1].strip())
                                if variable in variableMap.keys():  # If it is get it's value from the dict
                                    romFile.write(variableMap[variable][0])
                                elif variable in labelMap.keys():
                                    # It it is get it's value from the dict
                                    romFile.write(labelMap[variable])
                                else:
                                    # Else write it down
                                    romFile.write(unHex(variable))
                                programCounter += 2  # 2 bytes
                                break
                            except (ValueError, TypeError):
                                # That's not even a number...or a variable name
                                print(Fore.RED + 'Invalid variable use: ' +
                                      scLine + ' : Line ' + str(i + 1))
                                raise SyntaxError
                    else:
                        # Check if it's in a instruction table (16-bit)
                        for tableKey in varInstructionTable_SixteenBit.keys():
                            if scLine.startswith(tableKey):
                                # Write the opcode
                                romFile.write(
                                    pack('B', varInstructionTable_SixteenBit[tableKey]))
                                try:
                                    # Check if it's a variable
                                    variable = (scLine.split(',')[1].strip(
                                    ) if ',' in scLine else scLine.split()[1].strip())
                                    if variable in variableMap.keys():  # If it is get it's value from the dict
                                        romFile.write(variableMap[variable])
                                    elif variable in labelMap.keys():
                                        # It it is get it's value from the dict
                                        romFile.write(labelMap[variable])
                                    else:
                                        # Else write it down
                                        romFile.write(unHex(variable))
                                    programCounter += 3  # 3 bytes
                                    break
                                except (ValueError, TypeError):
                                    # That's not even a number...or a variable name
                                    print(Fore.RED + 'Invalid variable use: ' +
                                          scLine + ' : Line ' + str(i + 1))
                                    raise SyntaxError
                        else:
                            print(Fore.RED + 'Syntax error: ' +
                                  scLine + ' : Line ' + str(i + 1))
                            raise SyntaxError

        # All was good
        print(Fore.WHITE + 'Closing down... ' + Fore.YELLOW + '\'' +
              fileName + Fore.WHITE + '\'\nEverything went ' + Fore.GREEN + 'fine')
    except (KeyboardInterrupt, EOFError, IOError, SyntaxError):
        # Universal exception handler
        print(Fore.RED + '\nExiting...')
        exit(1)  # A peaceful exit to be honest ;)


# Call main
if __name__ == '__main__':
    if len(argv) is not 2:
        printHelp()
    else:
        run(argv[1])
