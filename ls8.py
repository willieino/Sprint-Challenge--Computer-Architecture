"""Main."""

import sys
from cpu import *

cpu = CPU()

filename = sys.argv[1]
mem = cpu.load_memory(ram, filename)
cpu.run(mem)