"""CPU functionality."""

import sys


ram = [0] * 256
registers = [0] * 8 # [0, 0, 0, 0, 0, 0, 0, 0]

registers[7] = 255  #hex(255)

IR = 0 # contains copy of currently executing command
HLT = 1

## ALU ops
 
ADD = 10100000 
SUB = 10100001 
MUL = 10100010 
DIV = 10100011 
MOD = 10100100 
INC = 1100101 
DEC = 1100110 
CMP = 10100111 
AND = 10101000 
NOT = 1101001 
OR  = 10101010 
XOR = 10101011 
SHL = 10101100 
SHR = 10101101  

## Other

NOP = 0
LDI = 10000010
LD = 10000011
ST =  10000100 
PUSH = 1000101
POP = 1000110
PRN = 1000111
PRA = 1001000

## PC mutators

CALL = 1010000
RET = 10001
INT = 1010010
IRET = 10011
JMP = 1010100 
JEQ = 1010101 
JNE = 1010110 
JGT = 1010111 
JLT = 1011000 
JLE = 1011001
JGE = 1011010  

class CPU:
    """Main CPU class."""

    def __init__(self):
        self.registers = [0] * 8 # [0, 0, 0, 0, 0, 0, 0, 0]
        self.PC = 0
        self.FL = 0
        self.SP = 0xF3
        self.SP = self.registers[7] # STACK POINTER (SP) R7
        self.IS = self.registers[6] # INTERRUPT STATUS (IS) R6
        self.IM = self.registers[5] # INTERRUPT MASK (IM) R5
        
    def ram_read(self, mar):
        mdr = ram[mar]
        return mdr
      
    def ram_write(self, mar, mdr): 
        ram[mar] = mdr

    # RETURNS A 8BIT BINARY
    def p8(self, v):
        return "{:08b}".format(v)

    # use this to print letters
    def get_ascii(self, binary_in):
 
        print("binary_in: ", binary_in)
        n = int(str(binary_in), 2)
        n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        return n

    def load_memory(self, ram, filename):
        address = 0
        try:
            with open(filename) as file:
                for line in file:
                    comment_split = line.split('#')
                    possible_number = comment_split[0]
                    if possible_number == '' or possible_number == '\n':
                        continue
                    instruction = int(possible_number)
                    ram[address] = instruction 
                    address += 1
            return ram
        except IOError:  #FileNotFoundError
            print('I cannot find that file, check the name')
            sys.exit(2)