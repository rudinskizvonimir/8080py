#!/usr/bin/env python
'''
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
'''
from os import path
from sys import argv, exit
from colorama import init, Fore, Back, Style
from struct import pack
from binascii import UnHexlify as UnHex

init()


def start(arg):
    print Style.DIM
    print '     ___________________________'
    print '    /                           /\\'
    print '   /       Zvonimirov         _/ /\\'
    print '  /        Intel 8080        / \/'
    print ' /         Assembler         /\\'
    print '/___________________________/ /'
    print '\___________________________\/'
    print ' \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\' + Style.RESET_ALL + Style.BRIGHT

    print Fore.WHITE + '\nPowered by ' + Fore.BLUE + 'Pyt' + Fore.YELLOW + 'hon' + Fore.WHITE + ' 2.7\nCopyright (C) 2017, Zvonimir Rudinski'
    fileName = None
    try:
        if arg is None:
            print 'If you wish to know more please enter \'-p\' as an arguement'
            fileName = raw_input('File path: ')
        elif arg == '-p':
            print '\nThis ' + Fore.BLUE + 'Intel' + Fore.WHITE + ' 8080 assembler was made for ' + Fore.BLUE + 'Project ' + Fore.YELLOW + 'Week' + Fore.WHITE + ' in my school'
            print 'It is written in ' + Fore.BLUE + 'Pyt' + Fore.YELLOW + 'hon' + Fore.WHITE + ' 2.7'
            print 'Modules: ' + Fore.RED + 'Co' + Fore.BLUE + 'lo' + Fore.YELLOW + 'ra' + Fore.GREEN + 'ma' + Fore.WHITE
            exit(0)
        else:
            fileName = arg
        print 'Trying to open \'' + Fore.YELLOW + fileName + '\'' + Fore.WHITE
        if path.isfile(fileName) is False:
            print Fore.RED + 'Fatal error: ' + Fore.WHITE + 'Can\'t open \'' + Fore.YELLOW + fileName + '\''
            raise IOError
        sourceCode = None
        with open(fileName, 'r') as sourceFile:
            sourceCode = sourceFile.readlines()
        for i in range(0, len(sourceCode)):
            sourceCode[i] = sourceCode[i].split('\n')[0]
        variableAddr = {'null': UnHex('00')}
        with open(fileName + '.rom', 'w+') as romFile:
            for i in range(0, len(sourceCode)):
                scLine = sourceCode[i].lower()
                if scLine == 'nop':
                    romFile.write(pack('B', 0))
                elif scLine.startswith('lxi b,'):
                    romFile.write(pack('B', 1))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:4])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'stax b':
                    romFile.write(pack('B', 2))
                elif scLine == 'inx b':
                    romFile.write(pack('B', 3))
                elif scLine == 'inr b':
                    romFile.write(pack('B', 4))
                elif scLine == 'dcr b':
                    romFile.write(pack('B', 5))
                elif scLine.startswith('mvi b,'):
                    romFile.write(pack('B', 6))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rlc':
                    romFile.write(pack('B', 7))
                elif scLine == 'dad b':
                    romFile.write(pack('B', 9))
                elif scLine == 'ldax b':
                    romFile.write(pack('B', 10))
                elif scLine == 'dcx b':
                    romFile.write(pack('B', 11))
                elif scLine == 'inr c':
                    romFile.write(pack('B', 12))
                elif scLine == 'dcr c':
                    romFile.write(pack('B', 13))
                elif scLine.startswith('mvi c,'):
                    romFile.write(pack('B', 14))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == "rrc":
                    romFile.write(pack('B', 15))
                elif scLine.startswith('lxi d,'):
                    romFile.write(pack('B', 17))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'stax d':
                    romFile.write(pack('B', 18))
                elif scLine == 'inx d':
                    romFile.write(pack('B', 19))
                elif scLine == 'inr d':
                    romFile.write(pack('B', 20))
                elif scLine == 'dcr d':
                    romFile.write(pack('B', 21))
                elif scLine.startswith('mvi d,'):
                    romFile.write(pack('B', 22))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'ral':
                    romFile.write(pack('B', 23))
                elif scLine == 'dad d':
                    romFile.write(pack('B', 25))
                elif scLine == 'ldax d':
                    romFile.write(pack('B', 26))
                elif scLine == 'dcx d':
                    romFile.write(pack('B', 27))
                elif scLine == 'inr e':
                    romFile.write(pack('B', 28))
                elif scLine == 'dcr e':
                    romFile.write(pack('B', 29))
                elif scLine.startswith('mvi e,'):
                    romFile.write(pack('B', 30))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rar':
                    romFile.write(pack('B', 31))
                elif scLine == 'rim':
                    romFile.write(pack('B', 32))
                elif scLine.startswith('lxi h,'):
                    romFile.write(pack('B', 33))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('shld'):
                    romFile.write(pack('B', 34))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'inx h':
                    romFile.write(pack('B', 35))
                elif scLine == 'inr h':
                    romFile.write(pack('B', 36))
                elif scLine == 'dcr h':
                    romFile.write(pack('B', 37))
                elif scLine.startswith('mvi h,'):
                    romFile.write(pack('B', 38))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'daa':
                    romFile.write(pack('B', 39))
                elif scLine == 'dad h':
                    romFile.write(pack('B', 41))
                elif scLine.startswith('lhld'):
                    romFile.write(pack('B', 42))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'dcx h':
                    romFile.write(pack('B', 43))
                elif scLine == 'inr l':
                    romFile.write(pack('B', 44))
                elif scLine == 'dcr l':
                    romFile.write(pack('B', 45))
                elif scLine.startswith('mvi l,'):
                    romFile.write(pack('B', 46))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'cma':
                    romFile.write(pack('B', 47))
                elif scLine == 'sim':
                    romFile.write(pack('B', 48))
                elif scLine.startswith('lxi sp,'):
                    romFile.write(pack('B', 49))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('sta'):
                    romFile.write(pack('B', 50))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'inx sp':
                    romFile.write(pack('B', 51))
                elif scLine == 'inr m':
                    romFile.write(pack('B', 52))
                elif scLine == 'dcr m':
                    romFile.write(pack('B', 53))
                elif scLine.startswith('mvi m,'):
                    romFile.write(pack('B', 54))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'stc':
                    romFile.write(pack('B', 55))
                elif scLine == 'dad sp':
                    romFile.write(pack('B', 57))
                elif scLine.startswith('lda'):
                    romFile.write(pack('B', 58))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'dcx sp':
                    romFile.write(pack('B', 59))
                elif scLine == 'inr a':
                    romFile.write(pack('B', 60))
                elif scLine == 'dcr a':
                    romFile.write(pack('B', 61))
                elif scLine.startswith('mvi a,'):
                    romFile.write(pack('B', 62))
                    try:
                        if scLine.split(',')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(',')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(',')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'cmc':
                    romFile.write(pack('B', 63))
                elif scLine == 'mov b,b':
                    romFile.write(pack('B', 64))
                elif scLine == 'mov b,c':
                    romFile.write(pack('B', 65))
                elif scLine == 'mov b,d':
                    romFile.write(pack('B', 66))
                elif scLine == 'mov b,e':
                    romFile.write(pack('B', 67))
                elif scLine == 'mov b,h':
                    romFile.write(pack('B', 68))
                elif scLine == 'mov b,l':
                    romFile.write(pack('B', 69))
                elif scLine == 'mov b,m':
                    romFile.write(pack('B', 70))
                elif scLine == 'mov b,a':
                    romFile.write(pack('B', 71))
                elif scLine == 'mov c,b':
                    romFile.write(pack('B', 72))
                elif scLine == 'mov c,c':
                    romFile.write(pack('B', 73))
                elif scLine == 'mov c,d':
                    romFile.write(pack('B', 74))
                elif scLine == 'mov c,e':
                    romFile.write(pack('B', 75))
                elif scLine == 'mov c,h':
                    romFile.write(pack('B', 76))
                elif scLine == 'mov c,l':
                    romFile.write(pack('B', 77))
                elif scLine == 'mov c,m':
                    romFile.write(pack('B', 78))
                elif scLine == 'mov c,a':
                    romFile.write(pack('B', 79))
                elif scLine == 'mov d,b':
                    romFile.write(pack('B', 80))
                elif scLine == 'mov d,c':
                    romFile.write(pack('B', 81))
                elif scLine == 'mov d,d':
                    romFile.write(pack('B', 82))
                elif scLine == 'mov d,e':
                    romFile.write(pack('B', 83))
                elif scLine == 'mov d,h':
                    romFile.write(pack('B', 84))
                elif scLine == 'mov d,l':
                    romFile.write(pack('B', 85))
                elif scLine == 'mov d,m':
                    romFile.write(pack('B', 86))
                elif scLine == 'mov d,a':
                    romFile.write(pack('B', 87))
                elif scLine == 'mov e,b':
                    romFile.write(pack('B', 88))
                elif scLine == 'mov e,c':
                    romFile.write(pack('B', 89))
                elif scLine == 'mov e,d':
                    romFile.write(pack('B', 90))
                elif scLine == 'mov e,e':
                    romFile.write(pack('B', 91))
                elif scLine == 'mov e,h':
                    romFile.write(pack('B', 92))
                elif scLine == 'mov e,l':
                    romFile.write(pack('B', 93))
                elif scLine == 'mov e,m':
                    romFile.write(pack('B', 94))
                elif scLine == 'mov e,a':
                    romFile.write(pack('B', 95))
                elif scLine == 'mov h,b':
                    romFile.write(pack('B', 96))
                elif scLine == 'mov h,c':
                    romFile.write(pack('B', 97))
                elif scLine == 'mov h,d':
                    romFile.write(pack('B', 98))
                elif scLine == 'mov h,e':
                    romFile.write(pack('B', 99))
                elif scLine == 'mov h,h':
                    romFile.write(pack('B', 100))
                elif scLine == 'mov h,l':
                    romFile.write(pack('B', 101))
                elif scLine == 'mov h,m':
                    romFile.write(pack('B', 102))
                elif scLine == 'mov h,a':
                    romFile.write(pack('B', 103))
                elif scLine == 'mov l,b':
                    romFile.write(pack('B', 104))
                elif scLine == 'mov l,c':
                    romFile.write(pack('B', 105))
                elif scLine == 'mov l,d':
                    romFile.write(pack('B', 106))
                elif scLine == 'mov l,e':
                    romFile.write(pack('B', 107))
                elif scLine == 'mov l,h':
                    romFile.write(pack('B', 108))
                elif scLine == 'mov l,l':
                    romFile.write(pack('B', 109))
                elif scLine == 'mov l,m':
                    romFile.write(pack('B', 110))
                elif scLine == 'mov l,a':
                    romFile.write(pack('B', 111))
                elif scLine == 'mov m,b':
                    romFile.write(pack('B', 112))
                elif scLine == 'mov m,c':
                    romFile.write(pack('B', 113))
                elif scLine == 'mov m,d':
                    romFile.write(pack('B', 114))
                elif scLine == 'mov m,e':
                    romFile.write(pack('B', 115))
                elif scLine == 'mov m,h':
                    romFile.write(pack('B', 116))
                elif scLine == 'mov m,l':
                    romFile.write(pack('B', 117))
                elif scLine == 'hlt':
                    romFile.write(pack('B', 118))
                elif scLine == 'mov m,a':
                    romFile.write(pack('B', 119))
                elif scLine == 'mov a,b':
                    romFile.write(pack('B', 120))
                elif scLine == 'mov a,c':
                    romFile.write(pack('B', 121))
                elif scLine == 'mov a,d':
                    romFile.write(pack('B', 122))
                elif scLine == 'mov a,e':
                    romFile.write(pack('B', 123))
                elif scLine == 'mov a,h':
                    romFile.write(pack('B', 124))
                elif scLine == 'mov a,l':
                    romFile.write(pack('B', 125))
                elif scLine == 'mov a,m':
                    romFile.write(pack('B', 126))
                elif scLine == 'mov a,a':
                    romFile.write(pack('B', 127))
                elif scLine == 'add b':
                    romFile.write(pack('B', 128))
                elif scLine == 'add c':
                    romFile.write(pack('B', 129))
                elif scLine == 'add d':
                    romFile.write(pack('B', 130))
                elif scLine == 'add e':
                    romFile.write(pack('B', 131))
                elif scLine == 'add h':
                    romFile.write(pack('B', 132))
                elif scLine == 'add l':
                    romFile.write(pack('B', 133))
                elif scLine == 'add m':
                    romFile.write(pack('B', 134))
                elif scLine == 'add a':
                    romFile.write(pack('B', 135))
                elif scLine == 'adc b':
                    romFile.write(pack('B', 136))
                elif scLine == 'adc c':
                    romFile.write(pack('B', 137))
                elif scLine == 'adc d':
                    romFile.write(pack('B', 138))
                elif scLine == 'adc e':
                    romFile.write(pack('B', 139))
                elif scLine == 'adc h':
                    romFile.write(pack('B', 140))
                elif scLine == 'adc l':
                    romFile.write(pack('B', 141))
                elif scLine == 'adc m':
                    romFile.write(pack('B', 142))
                elif scLine == 'adc a':
                    romFile.write(pack('B', 143))
                elif scLine == 'sub b':
                    romFile.write(pack('B', 144))
                elif scLine == 'sub c':
                    romFile.write(pack('B', 145))
                elif scLine == 'sub d':
                    romFile.write(pack('B', 146))
                elif scLine == 'sub e':
                    romFile.write(pack('B', 147))
                elif scLine == 'sub h':
                    romFile.write(pack('B', 148))
                elif scLine == 'sub l':
                    romFile.write(pack('B', 149))
                elif scLine == 'sub m':
                    romFile.write(pack('B', 150))
                elif scLine == 'sub a':
                    romFile.write(pack('B', 151))
                elif scLine == 'sbb b':
                    romFile.write(pack('B', 152))
                elif scLine == 'sbb c':
                    romFile.write(pack('B', 153))
                elif scLine == 'sbb d':
                    romFile.write(pack('B', 154))
                elif scLine == 'sbb e':
                    romFile.write(pack('B', 155))
                elif scLine == 'sbb h':
                    romFile.write(pack('B', 156))
                elif scLine == 'sbb l':
                    romFile.write(pack('B', 157))
                elif scLine == 'sbb m':
                    romFile.write(pack('B', 158))
                elif scLine == 'sbb a':
                    romFile.write(pack('B', 159))
                elif scLine == 'ana b':
                    romFile.write(pack('B', 160))
                elif scLine == 'ana c':
                    romFile.write(pack('B', 161))
                elif scLine == 'ana d':
                    romFile.write(pack('B', 162))
                elif scLine == 'ana e':
                    romFile.write(pack('B', 163))
                elif scLine == 'ana h':
                    romFile.write(pack('B', 164))
                elif scLine == 'ana l':
                    romFile.write(pack('B', 165))
                elif scLine == 'ana m':
                    romFile.write(pack('B', 166))
                elif scLine == 'ana a':
                    romFile.write(pack('B', 167))
                elif scLine == 'xra b':
                    romFile.write(pack('B', 168))
                elif scLine == 'xra c':
                    romFile.write(pack('B', 169))
                elif scLine == 'xra d':
                    romFile.write(pack('B', 170))
                elif scLine == 'xra e':
                    romFile.write(pack('B', 171))
                elif scLine == 'xra h':
                    romFile.write(pack('B', 172))
                elif scLine == 'xra l':
                    romFile.write(pack('B', 173))
                elif scLine == 'xra m':
                    romFile.write(pack('B', 174))
                elif scLine == 'xra a':
                    romFile.write(pack('B', 175))
                elif scLine == 'ora b':
                    romFile.write(pack('B', 176))
                elif scLine == 'ora c':
                    romFile.write(pack('B', 177))
                elif scLine == 'ora d':
                    romFile.write(pack('B', 178))
                elif scLine == 'ora e':
                    romFile.write(pack('B', 179))
                elif scLine == 'ora h':
                    romFile.write(pack('B', 180))
                elif scLine == 'ora l':
                    romFile.write(pack('B', 181))
                elif scLine == 'ora m':
                    romFile.write(pack('B', 182))
                elif scLine == 'ora a':
                    romFile.write(pack('B', 183))
                elif scLine == 'cmp b':
                    romFile.write(pack('B', 184))
                elif scLine == 'cmp c':
                    romFile.write(pack('B', 185))
                elif scLine == 'cmp d':
                    romFile.write(pack('B', 186))
                elif scLine == 'cmp e':
                    romFile.write(pack('B', 187))
                elif scLine == 'cmp h':
                    romFile.write(pack('B', 188))
                elif scLine == 'cmp l':
                    romFile.write(pack('B', 189))
                elif scLine == 'cmp m':
                    romFile.write(pack('B', 190))
                elif scLine == 'cmp a':
                    romFile.write(pack('B', 191))
                elif scLine == 'rnz':
                    romFile.write(pack('B', 192))
                elif scLine == 'pop b':
                    romFile.write(pack('B', 193))
                elif scLine.startswith('jnz'):
                    romFile.write(pack('B', 194))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('jmp'):
                    romFile.write(pack('B', 195))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('cnz'):
                    romFile.write(pack('B', 196))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'push b':
                    romFile.write(pack('B', 197))
                elif scLine.startswith('adi'):
                    romFile.write(pack('B', 198))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rst 0':
                    romFile.write(pack('B', 199))
                elif scLine == 'rz':
                    romFile.write(pack('B', 200))
                elif scLine == 'ret':
                    romFile.write(pack('B', 201))
                elif scLine.startswith('jz'):
                    romFile.write(pack('B', 202))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('cz'):
                    romFile.write(pack('B', 204))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('call'):
                    romFile.write(pack('B', 205))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('aci'):
                    romFile.write(pack('B', 206))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rst 1':
                    romFile.write(pack('B', 207))
                elif scLine == 'rnc':
                    romFile.write(pack('B', 208))
                elif scLine == 'pop d':
                    romFile.write(pack('B', 209))
                elif scLine.startswith('jnc'):
                    romFile.write(pack('B', 210))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('out'):
                    romFile.write(pack('B', 211))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('cnc'):
                    romFile.write(pack('B', 212))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'push d':
                    romFile.write(pack('B', 213))
                elif scLine.startswith('sui'):
                    romFile.write(pack('B', 214))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rst 2':
                    romFile.write(pack('B', 215))
                elif scLine == 'rc':
                    romFile.write(pack('B', 216))
                elif scLine.startswith('jc'):
                    romFile.write(pack('B', 218))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('in'):
                    romFile.write(pack('B', 219))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('cc'):
                    romFile.write(pack('B', 220))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('sbi'):
                    romFile.write(pack('B', 222))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rst 3':
                    romFile.write(pack('B', 223))
                elif scLine == 'rpo':
                    romFile.write(pack('B', 224))
                elif scLine == 'pop h':
                    romFile.write(pack('B', 225))
                elif scLine.startswith('jpo'):
                    romFile.write(pack('B', 226))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'xthl':
                    romFile.write(pack('B', 227))
                elif scLine.startswith('cpo'):
                    romFile.write(pack('B', 228))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'push h':
                    romFile.write(pack('B', 229))
                elif scLine.startswith('ani'):
                    romFile.write(pack('B', 230))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rst 4':
                    romFile.write(pack('B', 231))
                elif scLine == 'rpe':
                    romFile.write(pack('B', 232))
                elif scLine == 'pchl':
                    romFile.write(pack('B', 233))
                elif scLine.startswith('jpe'):
                    romFile.write(pack('B', 234))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'xchg':
                    romFile.write(pack('B', 235))
                elif scLine.startswith('cpe'):
                    romFile.write(pack('B', 236))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('xri'):
                    romFile.write(pack('B', 238))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rst 5':
                    romFile.write(pack('B', 239))
                elif scLine == 'rp':
                    romFile.write(pack('B', 240))
                elif scLine == 'pop psw':
                    romFile.write(pack('B', 241))
                elif scLine.startswith('jp'):
                    romFile.write(pack('B', 242))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'di':
                    romFile.write(pack('B', 243))
                elif scLine.startswith('cp'):
                    romFile.write(pack('B', 244))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'push psw':
                    romFile.write(pack('B', 245))
                elif scLine.startswith('ori'):
                    romFile.write(pack('B', 246))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:1])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:2]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rst 6':
                    romFile.write(pack('B', 247))
                elif scLine == 'rm':
                    romFile.write(pack('B', 248))
                elif scLine == 'sphl':
                    romFile.write(pack('B', 249))
                elif scLine.startswith('jm'):
                    romFile.write(pack('B', 250))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'ei':
                    romFile.write(pack('B', 251))
                elif scLine.startswith('cm'):
                    romFile.write(pack('B', 252))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine.startswith('cpi'):
                    romFile.write(pack('B', 254))
                    try:
                        if scLine.split(' ')[1] in variableAddr:
                            romFile.write(
                                variableAddr[scLine.split(' ')[1]][0:2])
                        else:
                            romFile.write(UnHex(scLine.split(' ')[1][0:4]))
                    except ValueError:
                        raise TypeError
                    except TypeError:
                        print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                        exit(-1)
                elif scLine == 'rst 7':
                    romFile.write(pack('B', 255))
                elif scLine.split(' ')[1] == 'equ':
                    try:
                        variableAddr[scLine.split(' ')[0]] = UnHex(
                            scLine.split(' ')[2])
                        print 'Updating variables'
                    except TypeError:
                        print Fore.RED + 'Digit count not divisable by 2: ' + scLine + ' : Linija ' + str(i)
                        exit(-1)
                else:
                    print Fore.RED + 'Syntax error: ' + scLine + ' : Line ' + str(i)
                    exit(-1)
        print Fore.WHITE + 'Closing down... \'' + Fore.YELLOW + fileName + Fore.WHITE + '\'\nEverything went ' + Fore.GREEN + 'fine'
    except KeyboardInterrupt:
        print Fore.RED + '\nExiting...'
        exit(-1)
    except EOFError:
        print Fore.RED + '\nExiting...'
        exit(-1)
    except IOError:
        print Fore.RED + 'Exiting...'
        exit(-1)


if __name__ == "__main__":
    if len(argv) is not 2:
        start(None)
    else:
        start(argv[1])
