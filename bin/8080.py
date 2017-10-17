#!/usr/bin/env python
# coding=utf-8
############## IMPORTS ##################
from __future__ import print_function
from os import path
from sys import argv, exit
from colorama import init, Fore, Style
from struct import pack
from binascii import unhexlify as UnHex
#########################################
"""
    Copyright (C) 2017, Zvonimir Rudinski
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
######### CROSS-PYTHON HACK #############
try:
    input = raw_input  # Python2
except NameError:
    pass  # Python3
# Init colorama module
init()
# Instruction table dictionary
INSTRUCTION_TABLE = {'nop': 0,
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
                     "rrc": 15,
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
                     'pop b': 193}
# Instruction table dictionary that expects a secondary parameter
VAR_INSTRUCTION_TABLE = {'lxi b,': 1,
                         'mvi b,': 6,
                         'mvi c,': 14,
                         'lxi d,': 17,
                         'mvi d,': 22,
                         'mvi e,': 30,
                         'lxi h,': 33,
                         'shld': 34,
                         'mvi h,': 38,
                         'lhld': 42,
                         'mvi l,': 46,
                         'lxi sp,': 49,
                         'sta': 50,
                         'mvi m,': 54,
                         'lda': 58,
                         'mvi a,': 62,
                         'jnz': 194,
                         'jmp': 195,
                         'cnz': 196,
                         'adi': 198,
                         'jz': 202,
                         'cz': 204,
                         'call': 205,
                         'aci': 206,
                         'jnc': 210,
                         'out': 211,
                         'cnc': 212,
                         'sui': 214,
                         'jc': 218,
                         'in': 219,
                         'cc': 220,
                         'sbi': 222,
                         'jpo': 226,
                         'cpo': 228,
                         'ani': 230,
                         'jpe': 234,
                         'cpe': 236,
                         'xri': 238,
                         'jp': 242,
                         'cp': 244,
                         'ori': 246,
                         'jm': 250,
                         'cm': 252,
                         'cpi': 254,
                         }

# Banner function
def banner():
    print(Style.DIM)
    print('     ___________________________')
    print('    /                           /\\')
    print('   /     sadboyzvone\'s        _/ /\\')
    print('  /        Intel 8080        / \/')
    print(' /         Assembler         /\\')
    print('/___________________________/ /')
    print('\___________________________\/')
    print(' \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\' + Style.RESET_ALL + Style.BRIGHT)
    print(Fore.WHITE + '\nPowered by ' + Fore.BLUE + 'Pyt' + Fore.YELLOW
          + 'hon' + Fore.WHITE + '\nCopyright (C) 2017, Zvonimir Rudinski')
# Help function
def print_help():
    print('\nThis ' + Fore.BLUE + 'Intel' + Fore.WHITE + ' 8080 assembler was made for ' + Fore.BLUE + 'Project ' + Fore.YELLOW + 'Week' + Fore.WHITE + ' in my school')
    print('It is written in ' + Fore.BLUE + 'Pyt' + Fore.YELLOW + 'hon' + Fore.WHITE)
    print('Modules: ' + Fore.RED + 'Co' + Fore.BLUE + 'lo' + Fore.YELLOW + 'ra' + Fore.GREEN + 'ma' + Fore.WHITE)
# Main
def start(arg=None):
    banner() # Print banner 
    # File name
    file_name = None
    # Variable dictionary
    variable_addr = {'null': UnHex('00')}
    try:
        if arg is None: # Check for arguments
            print('If you wish to know more please enter \'-p\' as an argument')
            file_name = input('File path: ') # None found, please input the path
        elif arg == '-p':
            print_help() # Print help then exit
            exit(0)
        else:
            file_name = arg # Argument is provided
        print('Trying to open ' + Fore.YELLOW + '\'' + file_name + '\'' + Fore.WHITE)
        if path.isfile(file_name) is False: # Check if the file exists
            print(Fore.RED + 'Fatal error: ' + Fore.WHITE + 'File not found: ' + Fore.YELLOW + '\'' + file_name + '\'')
            raise IOError
	# Read in the source code
        with open(file_name, 'r') as sourceFile:
            source_code = sourceFile.readlines()
	# Strip the newlines
        for i in range(0, len(source_code)):
            source_code[i] = source_code[i].split('\n')[0]
	# Start writing to a rom file
        with open(file_name + '.rom', 'wb+') as romFile:
	    # Check the line
            for i,sc_line in enumerate(source_code):
                sc_line = sc_line.lower() # Turn it to lower case for easier lookup
		# Check if it's in the instruction table
                if sc_line in INSTRUCTION_TABLE:
                    romFile.write(pack('B', INSTRUCTION_TABLE[sc_line])) # Write the opcode
		    continue
                elif sc_line.split(' ')[1] == 'equ': # Check if it's a variable declaration
                    try:
                        if(int(sc_line.split(' ')[2]) >= (2**8)):
                            print(Fore.RED + 'Variable too large: ' + sc_line + ' : Line ' + str(i+1))
                            raise SyntaxError
                        variable_addr[sc_line.split(' ')[0]] = UnHex(sc_line.split(' ')[2]) # It is, save it to a dictionary
                        print('Updating variables')
		  	continue

                    except TypeError:
                        print(Fore.RED + 'Digit count not divisible by 2: ' + sc_line + ' : Line ' + str(i+1))
                        raise SyntaxError
                else: # Check if it's in another instruction table
                    for k in VAR_INSTRUCTION_TABLE.keys():
                        if sc_line.startswith(k):
                            romFile.write(pack('B', VAR_INSTRUCTION_TABLE[k])) # Write the opcode
                            try:
				# Check if it's a variable
                                variable = sc_line.split(',')[1].strip() if "," in sc_line else sc_line.split()[1].strip()
                                if variable in variable_addr: # If it is get it's value from the dict
                                    romFile.write(variable_addr[variable])
                                else:
                                    romFile.write(UnHex(variable)) # Else write it down
				break
                            except (ValueError, TypeError):
                                print(Fore.RED + 'Type error: ' + sc_line + ' : Line ' + str(i+1)) # That's not even a number...or a variable name
                                raise SyntaxError
		    else:
		        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i+1))
		        raise SyntaxError
	# All was good
        print(Fore.WHITE + 'Closing down... ' + Fore.YELLOW + '\'' + file_name + Fore.WHITE + '\'\nEverything went ' + Fore.GREEN + 'fine')
    # Universal exception handler
    except (KeyboardInterrupt, EOFError, IOError,SyntaxError):
        print(Fore.RED + '\nExiting...')
        exit(-1)
# Call main
if __name__ == "__main__":
    if len(argv) is not 2:
        start()
    else:
        start(argv[1])
