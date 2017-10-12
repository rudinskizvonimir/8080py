#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function

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
from os import path
from sys import argv, exit
from colorama import init, Fore, Style
from struct import pack
from binascii import unhexlify as UnHex

try:
    input = raw_input  # Python2
except NameError:
    pass  # Python3

init()


def start(arg=None):
    print(Style.DIM)
    print('     ___________________________')
    print('    /                           /\\')
    print('   /       Zvonimirov         _/ /\\')
    print('  /        Intel 8080        / \/')
    print(' /         Assembler         /\\')
    print('/___________________________/ /')
    print('\___________________________\/')
    print(' \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\' + Style.RESET_ALL + Style.BRIGHT)

    print(Fore.WHITE + '\nPowered by ' + Fore.BLUE + 'Pyt' + Fore.YELLOW
          + 'hon' + Fore.WHITE + ' 2.7\nCopyright (C) 2017, Zvonimir Rudinski')
    file_name = None
    try:
        if arg is None:
            print('If you wish to know more please enter \'-p\' as an arguement')
            file_name = input('File path: ')
        elif arg == '-p':
            print('\nThis ' + Fore.BLUE + 'Intel' + Fore.WHITE + ' 8080 assembler was made for '
                  + Fore.BLUE + 'Project ' + Fore.YELLOW + 'Week' + Fore.WHITE + ' in my school')
            print('It is written in ' + Fore.BLUE + 'Pyt' + Fore.YELLOW + 'hon' + Fore.WHITE + ' 2.7')
            print('Modules: ' + Fore.RED + 'Co' + Fore.BLUE + 'lo' +
                  Fore.YELLOW + 'ra' + Fore.GREEN + 'ma' + Fore.WHITE)
            exit(0)
        else:
            file_name = arg
        print('Trying to open \'' + Fore.YELLOW + file_name + '\'' + Fore.WHITE)
        if path.isfile(file_name) is False:
            print(Fore.RED + 'Fatal error: ' + Fore.WHITE + 'Can\'t open \'' + Fore.YELLOW + file_name + '\'')
            raise IOError

        with open(file_name, 'r') as sourceFile:
            source_code = sourceFile.readlines()
        for i in range(0, len(source_code)):
            source_code[i] = source_code[i].split('\n')[0]
        variable_addr = {'null': UnHex('00')}
        with open(file_name + '.rom', 'wb+') as romFile:
            for i in range(0, len(source_code)):
                sc_line = source_code[i].lower()
                if sc_line == 'nop':
                    romFile.write(pack('B', 0))
                elif sc_line.startswith('lxi b,'):
                    romFile.write(pack('B', 1))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:4])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:4]))
                    except (ValueError, TypeError):
                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'stax b':
                    romFile.write(pack('B', 2))
                elif sc_line == 'inx b':
                    romFile.write(pack('B', 3))
                elif sc_line == 'inr b':
                    romFile.write(pack('B', 4))
                elif sc_line == 'dcr b':
                    romFile.write(pack('B', 5))
                elif sc_line.startswith('mvi b,'):
                    romFile.write(pack('B', 6))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:2]))
                    except (ValueError, TypeError):
                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rlc':
                    romFile.write(pack('B', 7))
                elif sc_line == 'dad b':
                    romFile.write(pack('B', 9))
                elif sc_line == 'ldax b':
                    romFile.write(pack('B', 10))
                elif sc_line == 'dcx b':
                    romFile.write(pack('B', 11))
                elif sc_line == 'inr c':
                    romFile.write(pack('B', 12))
                elif sc_line == 'dcr c':
                    romFile.write(pack('B', 13))
                elif sc_line.startswith('mvi c,'):
                    romFile.write(pack('B', 14))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == "rrc":
                    romFile.write(pack('B', 15))
                elif sc_line.startswith('lxi d,'):
                    romFile.write(pack('B', 17))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:4]))
                    except (ValueError, TypeError):
                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'stax d':
                    romFile.write(pack('B', 18))
                elif sc_line == 'inx d':
                    romFile.write(pack('B', 19))
                elif sc_line == 'inr d':
                    romFile.write(pack('B', 20))
                elif sc_line == 'dcr d':
                    romFile.write(pack('B', 21))
                elif sc_line.startswith('mvi d,'):
                    romFile.write(pack('B', 22))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:2]))
                    except (ValueError, TypeError):
                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'ral':
                    romFile.write(pack('B', 23))
                elif sc_line == 'dad d':
                    romFile.write(pack('B', 25))
                elif sc_line == 'ldax d':
                    romFile.write(pack('B', 26))
                elif sc_line == 'dcx d':
                    romFile.write(pack('B', 27))
                elif sc_line == 'inr e':
                    romFile.write(pack('B', 28))
                elif sc_line == 'dcr e':
                    romFile.write(pack('B', 29))
                elif sc_line.startswith('mvi e,'):
                    romFile.write(pack('B', 30))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:2]))
                    except (ValueError, TypeError):
                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rar':
                    romFile.write(pack('B', 31))
                elif sc_line == 'rim':
                    romFile.write(pack('B', 32))
                elif sc_line.startswith('lxi h,'):
                    romFile.write(pack('B', 33))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:4]))
                    except (ValueError, TypeError):
                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('shld'):
                    romFile.write(pack('B', 34))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'inx h':
                    romFile.write(pack('B', 35))
                elif sc_line == 'inr h':
                    romFile.write(pack('B', 36))
                elif sc_line == 'dcr h':
                    romFile.write(pack('B', 37))
                elif sc_line.startswith('mvi h,'):
                    romFile.write(pack('B', 38))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'daa':
                    romFile.write(pack('B', 39))
                elif sc_line == 'dad h':
                    romFile.write(pack('B', 41))
                elif sc_line.startswith('lhld'):
                    romFile.write(pack('B', 42))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'dcx h':
                    romFile.write(pack('B', 43))
                elif sc_line == 'inr l':
                    romFile.write(pack('B', 44))
                elif sc_line == 'dcr l':
                    romFile.write(pack('B', 45))
                elif sc_line.startswith('mvi l,'):
                    romFile.write(pack('B', 46))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'cma':
                    romFile.write(pack('B', 47))
                elif sc_line == 'sim':
                    romFile.write(pack('B', 48))
                elif sc_line.startswith('lxi sp,'):
                    romFile.write(pack('B', 49))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('sta'):
                    romFile.write(pack('B', 50))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'inx sp':
                    romFile.write(pack('B', 51))
                elif sc_line == 'inr m':
                    romFile.write(pack('B', 52))
                elif sc_line == 'dcr m':
                    romFile.write(pack('B', 53))
                elif sc_line.startswith('mvi m,'):
                    romFile.write(pack('B', 54))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'stc':
                    romFile.write(pack('B', 55))
                elif sc_line == 'dad sp':
                    romFile.write(pack('B', 57))
                elif sc_line.startswith('lda'):
                    romFile.write(pack('B', 58))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'dcx sp':
                    romFile.write(pack('B', 59))
                elif sc_line == 'inr a':
                    romFile.write(pack('B', 60))
                elif sc_line == 'dcr a':
                    romFile.write(pack('B', 61))
                elif sc_line.startswith('mvi a,'):
                    romFile.write(pack('B', 62))
                    try:
                        if sc_line.split(',')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(',')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'cmc':
                    romFile.write(pack('B', 63))
                elif sc_line == 'mov b,b':
                    romFile.write(pack('B', 64))
                elif sc_line == 'mov b,c':
                    romFile.write(pack('B', 65))
                elif sc_line == 'mov b,d':
                    romFile.write(pack('B', 66))
                elif sc_line == 'mov b,e':
                    romFile.write(pack('B', 67))
                elif sc_line == 'mov b,h':
                    romFile.write(pack('B', 68))
                elif sc_line == 'mov b,l':
                    romFile.write(pack('B', 69))
                elif sc_line == 'mov b,m':
                    romFile.write(pack('B', 70))
                elif sc_line == 'mov b,a':
                    romFile.write(pack('B', 71))
                elif sc_line == 'mov c,b':
                    romFile.write(pack('B', 72))
                elif sc_line == 'mov c,c':
                    romFile.write(pack('B', 73))
                elif sc_line == 'mov c,d':
                    romFile.write(pack('B', 74))
                elif sc_line == 'mov c,e':
                    romFile.write(pack('B', 75))
                elif sc_line == 'mov c,h':
                    romFile.write(pack('B', 76))
                elif sc_line == 'mov c,l':
                    romFile.write(pack('B', 77))
                elif sc_line == 'mov c,m':
                    romFile.write(pack('B', 78))
                elif sc_line == 'mov c,a':
                    romFile.write(pack('B', 79))
                elif sc_line == 'mov d,b':
                    romFile.write(pack('B', 80))
                elif sc_line == 'mov d,c':
                    romFile.write(pack('B', 81))
                elif sc_line == 'mov d,d':
                    romFile.write(pack('B', 82))
                elif sc_line == 'mov d,e':
                    romFile.write(pack('B', 83))
                elif sc_line == 'mov d,h':
                    romFile.write(pack('B', 84))
                elif sc_line == 'mov d,l':
                    romFile.write(pack('B', 85))
                elif sc_line == 'mov d,m':
                    romFile.write(pack('B', 86))
                elif sc_line == 'mov d,a':
                    romFile.write(pack('B', 87))
                elif sc_line == 'mov e,b':
                    romFile.write(pack('B', 88))
                elif sc_line == 'mov e,c':
                    romFile.write(pack('B', 89))
                elif sc_line == 'mov e,d':
                    romFile.write(pack('B', 90))
                elif sc_line == 'mov e,e':
                    romFile.write(pack('B', 91))
                elif sc_line == 'mov e,h':
                    romFile.write(pack('B', 92))
                elif sc_line == 'mov e,l':
                    romFile.write(pack('B', 93))
                elif sc_line == 'mov e,m':
                    romFile.write(pack('B', 94))
                elif sc_line == 'mov e,a':
                    romFile.write(pack('B', 95))
                elif sc_line == 'mov h,b':
                    romFile.write(pack('B', 96))
                elif sc_line == 'mov h,c':
                    romFile.write(pack('B', 97))
                elif sc_line == 'mov h,d':
                    romFile.write(pack('B', 98))
                elif sc_line == 'mov h,e':
                    romFile.write(pack('B', 99))
                elif sc_line == 'mov h,h':
                    romFile.write(pack('B', 100))
                elif sc_line == 'mov h,l':
                    romFile.write(pack('B', 101))
                elif sc_line == 'mov h,m':
                    romFile.write(pack('B', 102))
                elif sc_line == 'mov h,a':
                    romFile.write(pack('B', 103))
                elif sc_line == 'mov l,b':
                    romFile.write(pack('B', 104))
                elif sc_line == 'mov l,c':
                    romFile.write(pack('B', 105))
                elif sc_line == 'mov l,d':
                    romFile.write(pack('B', 106))
                elif sc_line == 'mov l,e':
                    romFile.write(pack('B', 107))
                elif sc_line == 'mov l,h':
                    romFile.write(pack('B', 108))
                elif sc_line == 'mov l,l':
                    romFile.write(pack('B', 109))
                elif sc_line == 'mov l,m':
                    romFile.write(pack('B', 110))
                elif sc_line == 'mov l,a':
                    romFile.write(pack('B', 111))
                elif sc_line == 'mov m,b':
                    romFile.write(pack('B', 112))
                elif sc_line == 'mov m,c':
                    romFile.write(pack('B', 113))
                elif sc_line == 'mov m,d':
                    romFile.write(pack('B', 114))
                elif sc_line == 'mov m,e':
                    romFile.write(pack('B', 115))
                elif sc_line == 'mov m,h':
                    romFile.write(pack('B', 116))
                elif sc_line == 'mov m,l':
                    romFile.write(pack('B', 117))
                elif sc_line == 'hlt':
                    romFile.write(pack('B', 118))
                elif sc_line == 'mov m,a':
                    romFile.write(pack('B', 119))
                elif sc_line == 'mov a,b':
                    romFile.write(pack('B', 120))
                elif sc_line == 'mov a,c':
                    romFile.write(pack('B', 121))
                elif sc_line == 'mov a,d':
                    romFile.write(pack('B', 122))
                elif sc_line == 'mov a,e':
                    romFile.write(pack('B', 123))
                elif sc_line == 'mov a,h':
                    romFile.write(pack('B', 124))
                elif sc_line == 'mov a,l':
                    romFile.write(pack('B', 125))
                elif sc_line == 'mov a,m':
                    romFile.write(pack('B', 126))
                elif sc_line == 'mov a,a':
                    romFile.write(pack('B', 127))
                elif sc_line == 'add b':
                    romFile.write(pack('B', 128))
                elif sc_line == 'add c':
                    romFile.write(pack('B', 129))
                elif sc_line == 'add d':
                    romFile.write(pack('B', 130))
                elif sc_line == 'add e':
                    romFile.write(pack('B', 131))
                elif sc_line == 'add h':
                    romFile.write(pack('B', 132))
                elif sc_line == 'add l':
                    romFile.write(pack('B', 133))
                elif sc_line == 'add m':
                    romFile.write(pack('B', 134))
                elif sc_line == 'add a':
                    romFile.write(pack('B', 135))
                elif sc_line == 'adc b':
                    romFile.write(pack('B', 136))
                elif sc_line == 'adc c':
                    romFile.write(pack('B', 137))
                elif sc_line == 'adc d':
                    romFile.write(pack('B', 138))
                elif sc_line == 'adc e':
                    romFile.write(pack('B', 139))
                elif sc_line == 'adc h':
                    romFile.write(pack('B', 140))
                elif sc_line == 'adc l':
                    romFile.write(pack('B', 141))
                elif sc_line == 'adc m':
                    romFile.write(pack('B', 142))
                elif sc_line == 'adc a':
                    romFile.write(pack('B', 143))
                elif sc_line == 'sub b':
                    romFile.write(pack('B', 144))
                elif sc_line == 'sub c':
                    romFile.write(pack('B', 145))
                elif sc_line == 'sub d':
                    romFile.write(pack('B', 146))
                elif sc_line == 'sub e':
                    romFile.write(pack('B', 147))
                elif sc_line == 'sub h':
                    romFile.write(pack('B', 148))
                elif sc_line == 'sub l':
                    romFile.write(pack('B', 149))
                elif sc_line == 'sub m':
                    romFile.write(pack('B', 150))
                elif sc_line == 'sub a':
                    romFile.write(pack('B', 151))
                elif sc_line == 'sbb b':
                    romFile.write(pack('B', 152))
                elif sc_line == 'sbb c':
                    romFile.write(pack('B', 153))
                elif sc_line == 'sbb d':
                    romFile.write(pack('B', 154))
                elif sc_line == 'sbb e':
                    romFile.write(pack('B', 155))
                elif sc_line == 'sbb h':
                    romFile.write(pack('B', 156))
                elif sc_line == 'sbb l':
                    romFile.write(pack('B', 157))
                elif sc_line == 'sbb m':
                    romFile.write(pack('B', 158))
                elif sc_line == 'sbb a':
                    romFile.write(pack('B', 159))
                elif sc_line == 'ana b':
                    romFile.write(pack('B', 160))
                elif sc_line == 'ana c':
                    romFile.write(pack('B', 161))
                elif sc_line == 'ana d':
                    romFile.write(pack('B', 162))
                elif sc_line == 'ana e':
                    romFile.write(pack('B', 163))
                elif sc_line == 'ana h':
                    romFile.write(pack('B', 164))
                elif sc_line == 'ana l':
                    romFile.write(pack('B', 165))
                elif sc_line == 'ana m':
                    romFile.write(pack('B', 166))
                elif sc_line == 'ana a':
                    romFile.write(pack('B', 167))
                elif sc_line == 'xra b':
                    romFile.write(pack('B', 168))
                elif sc_line == 'xra c':
                    romFile.write(pack('B', 169))
                elif sc_line == 'xra d':
                    romFile.write(pack('B', 170))
                elif sc_line == 'xra e':
                    romFile.write(pack('B', 171))
                elif sc_line == 'xra h':
                    romFile.write(pack('B', 172))
                elif sc_line == 'xra l':
                    romFile.write(pack('B', 173))
                elif sc_line == 'xra m':
                    romFile.write(pack('B', 174))
                elif sc_line == 'xra a':
                    romFile.write(pack('B', 175))
                elif sc_line == 'ora b':
                    romFile.write(pack('B', 176))
                elif sc_line == 'ora c':
                    romFile.write(pack('B', 177))
                elif sc_line == 'ora d':
                    romFile.write(pack('B', 178))
                elif sc_line == 'ora e':
                    romFile.write(pack('B', 179))
                elif sc_line == 'ora h':
                    romFile.write(pack('B', 180))
                elif sc_line == 'ora l':
                    romFile.write(pack('B', 181))
                elif sc_line == 'ora m':
                    romFile.write(pack('B', 182))
                elif sc_line == 'ora a':
                    romFile.write(pack('B', 183))
                elif sc_line == 'cmp b':
                    romFile.write(pack('B', 184))
                elif sc_line == 'cmp c':
                    romFile.write(pack('B', 185))
                elif sc_line == 'cmp d':
                    romFile.write(pack('B', 186))
                elif sc_line == 'cmp e':
                    romFile.write(pack('B', 187))
                elif sc_line == 'cmp h':
                    romFile.write(pack('B', 188))
                elif sc_line == 'cmp l':
                    romFile.write(pack('B', 189))
                elif sc_line == 'cmp m':
                    romFile.write(pack('B', 190))
                elif sc_line == 'cmp a':
                    romFile.write(pack('B', 191))
                elif sc_line == 'rnz':
                    romFile.write(pack('B', 192))
                elif sc_line == 'pop b':
                    romFile.write(pack('B', 193))
                elif sc_line.startswith('jnz'):
                    romFile.write(pack('B', 194))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('jmp'):
                    romFile.write(pack('B', 195))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('cnz'):
                    romFile.write(pack('B', 196))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'push b':
                    romFile.write(pack('B', 197))
                elif sc_line.startswith('adi'):
                    romFile.write(pack('B', 198))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rst 0':
                    romFile.write(pack('B', 199))
                elif sc_line == 'rz':
                    romFile.write(pack('B', 200))
                elif sc_line == 'ret':
                    romFile.write(pack('B', 201))
                elif sc_line.startswith('jz'):
                    romFile.write(pack('B', 202))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('cz'):
                    romFile.write(pack('B', 204))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('call'):
                    romFile.write(pack('B', 205))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('aci'):
                    romFile.write(pack('B', 206))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rst 1':
                    romFile.write(pack('B', 207))
                elif sc_line == 'rnc':
                    romFile.write(pack('B', 208))
                elif sc_line == 'pop d':
                    romFile.write(pack('B', 209))
                elif sc_line.startswith('jnc'):
                    romFile.write(pack('B', 210))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('out'):
                    romFile.write(pack('B', 211))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('cnc'):
                    romFile.write(pack('B', 212))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'push d':
                    romFile.write(pack('B', 213))
                elif sc_line.startswith('sui'):
                    romFile.write(pack('B', 214))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rst 2':
                    romFile.write(pack('B', 215))
                elif sc_line == 'rc':
                    romFile.write(pack('B', 216))
                elif sc_line.startswith('jc'):
                    romFile.write(pack('B', 218))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('in'):
                    romFile.write(pack('B', 219))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('cc'):
                    romFile.write(pack('B', 220))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('sbi'):
                    romFile.write(pack('B', 222))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rst 3':
                    romFile.write(pack('B', 223))
                elif sc_line == 'rpo':
                    romFile.write(pack('B', 224))
                elif sc_line == 'pop h':
                    romFile.write(pack('B', 225))
                elif sc_line.startswith('jpo'):
                    romFile.write(pack('B', 226))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'xthl':
                    romFile.write(pack('B', 227))
                elif sc_line.startswith('cpo'):
                    romFile.write(pack('B', 228))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'push h':
                    romFile.write(pack('B', 229))
                elif sc_line.startswith('ani'):
                    romFile.write(pack('B', 230))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rst 4':
                    romFile.write(pack('B', 231))
                elif sc_line == 'rpe':
                    romFile.write(pack('B', 232))
                elif sc_line == 'pchl':
                    romFile.write(pack('B', 233))
                elif sc_line.startswith('jpe'):
                    romFile.write(pack('B', 234))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'xchg':
                    romFile.write(pack('B', 235))
                elif sc_line.startswith('cpe'):
                    romFile.write(pack('B', 236))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('xri'):
                    romFile.write(pack('B', 238))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rst 5':
                    romFile.write(pack('B', 239))
                elif sc_line == 'rp':
                    romFile.write(pack('B', 240))
                elif sc_line == 'pop psw':
                    romFile.write(pack('B', 241))
                elif sc_line.startswith('jp'):
                    romFile.write(pack('B', 242))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'di':
                    romFile.write(pack('B', 243))
                elif sc_line.startswith('cp'):
                    romFile.write(pack('B', 244))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'push psw':
                    romFile.write(pack('B', 245))
                elif sc_line.startswith('ori'):
                    romFile.write(pack('B', 246))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:2]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rst 6':
                    romFile.write(pack('B', 247))
                elif sc_line == 'rm':
                    romFile.write(pack('B', 248))
                elif sc_line == 'sphl':
                    romFile.write(pack('B', 249))
                elif sc_line.startswith('jm'):
                    romFile.write(pack('B', 250))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'ei':
                    romFile.write(pack('B', 251))
                elif sc_line.startswith('cm'):
                    romFile.write(pack('B', 252))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line.startswith('cpi'):
                    romFile.write(pack('B', 254))
                    try:
                        if sc_line.split(' ')[1] in variable_addr:
                            romFile.write(variable_addr[sc_line.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(sc_line.split(' ')[1][0:4]))
                    except (ValueError, TypeError):

                        print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                        exit(-1)
                elif sc_line == 'rst 7':
                    romFile.write(pack('B', 255))
                elif sc_line.split(' ')[1] == 'equ':
                    try:
                        variable_addr[sc_line.split(' ')[0]] = UnHex(sc_line.split(' ')[2])
                        print('Updating variables')
                    except TypeError:
                        print(Fore.RED + 'Digit count not divisable by 2: ' + sc_line + ' : Linija ' + str(i))
                        exit(-1)
                else:
                    print(Fore.RED + 'Syntax error: ' + sc_line + ' : Line ' + str(i))
                    exit(-1)
        print(Fore.WHITE + 'Closing down... \'' + Fore.YELLOW + file_name + Fore.WHITE
              + '\'\nEverything went ' + Fore.GREEN + 'fine')
    except (KeyboardInterrupt, EOFError, IOError):
        print(Fore.RED + '\nExiting...')
        exit(-1)


if __name__ == "__main__":
    if len(argv) is not 2:
        start()
    else:
        start(argv[1])
