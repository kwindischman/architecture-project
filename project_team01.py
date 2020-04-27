import sys
import math

class Block:
    def __init__(self, block_size, tag_size):
        self.valid = True
        self.tag = 0

    def is_valid(self):
        return self.valid

    def set_valid(self, is_valid):
        self.valid = is_valid

    def get_tag(self):
        return self.tag

    def set_tag(self, new_tag):
        self.tag = new_tag

def calculate_values():
    global total_blocks
    global tag_size
    global index_size
    global block_offset
    global total_rows
    global overhead_size
    global implementation_mem_size
    global cost

    total_blocks = (cache_size * 1024) / block_size
    total_rows = (cache_size * 1024) / (block_size * associativity)
    index_size = math.log(total_rows, 2)
    block_offset = math.log(block_size, 2)
    tag_size = 32 - block_offset - index_size
    overhead_size = ((tag_size + 1) * total_blocks) // 8
    implementation_mem_size = (overhead_size + cache_size*1024)
    cost = (implementation_mem_size // 1024) * 0.05

def parse_trace_file():
    i = 0
    instr_length = ""
    instr_addr = ""
    dest_addr = ""
    src_addr = ""

    with open(file_name) as file:
        for line in file:
            if i % 3 == 0:
                instr_length = line[5:7]
                instr_addr = hex_to_binary(line[10:18])
                cache_fetch(instr_length, instr_addr)
            elif i % 3 == 1:
                dest_addr = hex_to_binary(line[6:14])
                src_addr = hex_to_binary(line[33:41])
                cache_write(dest_addr)
                cache_read(src_addr)
            i+=1

def print_args():
    RR = 'Round Robin'
    RND = 'Random'
    LRU = 'Least Recently Used'

    print('Cache Simulator - CS 3853 - Team 01')
    print('\nTrace File: %s' % file_name)
    print('\n***** Cache Input Parameters *****')
    print('\n%-30s %d KB' % ('Cache Size:', cache_size))
    print('%-30s %d bytes' % ('Block Size:', block_size))
    print('%-30s %d' % ('Associativity:', associativity))

    if replacement.upper() == 'RR':
        print('%-30s %s' % ('Replacement Policy:', RR))
    elif replacement.upper() == 'RND':
        print('%-30s %s' % ('Replacement Policy:', RND))
    elif replacement.upper() == 'LRU':
        print('%-30s %s' % ('Replacement Policy:', LRU))
    else:
        print('bad input for replacement policy')
        sys.exit(-1)

def print_calculated_values():
    print('\n***** Cache Calculated Values *****')
    print('\n%-30s %d' % ('Total # Blocks:', total_blocks))
    print('%-30s %d bits' % ('Tag Size:', tag_size))
    print('%-30s %d bits' % ('Index Size:', index_size))
    print('%-30s %d' % ('Total # Rows:', total_rows))
    print('%-30s %d bytes' % ('Overhead Size:', overhead_size))
    print('%-30s %0.2f KB (%d bytes)' % ('Implementation Memory Size:'
                                         , implementation_mem_size / 1024
                                         , implementation_mem_size))
    print('%-30s $%0.2f' % ('Cost:', cost))

def print_simulation_results():
    print("\n***** Cache Simulation Results *****")
    print("\n%-30s %d" % ('Total Cache Accesses:', total_accesses))
    print("\n%-30s %d" % ('Cache Hits:', total_hits))
    print("\n%-30s %d" % ('Cache Misses:', comp_misses + conf_misses))
    print("\n--- %-30s %d" % ("Compulsoty Misses:", comp_misses))
    print("\n--- %-30s %d" % ("Conflict Misses:", conf_misses))

    print("***** ***** CACHE HIT & MISS RATE: ***** *****")
    print("\n%-30s %0.4f%" % ('Hit Rate:', (total_hits/total_instructions)*100))
    print("\n%-30s %0.4f" % ('Miss Rate:', (1-(total_hits/total_instructions))*100))
    print("\n%-30s %0.2f" % ('CPI', total_cycles/total_instructions))

    unused_cache = ((total_blocks - comp_misses) * (block_size + overhead_size)) / 1024


    print("\n%-30s %0.2f KB / %0.2f KB = %0.2f% Waste: $%0.2f" % ('Unused Cache Space:'
                                                                  , unused_cache
                                                                  , cache_size
                                                                  , unused_cache/cache_size
                                                                  , 0.05 * unused_cache))
    print("\n%-30s %d / %d" % ('Unused Cache Blocks:', total_blocks - comp_misses, total_blocks))

def binary_to_dec(x):
    return int(x, 2)

def hex_to_binary(x):
    return bin(int(x, 16))[2:].zfill(32)

def set_cache():
    global cache
    global total_accesses
    global total_hits
    global total_cycles
    global total_instructions
    global conf_misses
    global comp_misses

    total_accesses = 0
    total_hits = 0
    total_cycles = 0
    total_instructions = 0
    conf_misses = 0
    comp_misses = 0

    cache = [[Block(block_size, tag_size) for x in range(total_rows)] for y in range(associativity)]

def set_vars():
    global file_name
    global cache_size
    global block_size
    global associativity
    global replacement

    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == '-f':
            file_name = sys.argv[i + 1]
        elif sys.argv[i] == '-s':
            cache_size = int(sys.argv[i + 1])
        elif sys.argv[i] == '-b':
            block_size = int(sys.argv[i + 1])
        elif sys.argv[i] == '-a':
            associativity = int(sys.argv[i + 1])
        elif sys.argv[i] == '-r':
            replacement = sys.argv[i + 1]
        else:
            print('invalid command ', sys.argv[i])
            sys.exit(-1)

def main():
    set_vars()
    print_args()
    calculate_values()
    print_calculated_values()
    set_cache()
    parse_trace_file()
    print_simulation_results()

if __name__ == '__main__':
    main()
