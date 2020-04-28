import sys
import math
import random

class Block:
    def __init__(self):
        self.valid = False
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

    global replacement_array 
    replacement_array = [0 for x in range(total_rows)]

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
                reg_instr(int(instr_length), instr_addr)
                global total_cycles
                total_cycles += 2
            elif i % 3 == 1:
                dest_addr = hex_to_binary(line[6:14])
                src_addr = hex_to_binary(line[33:41])
                rw_instr(dest_addr)
                rw_instr(src_addr)
            i+=1

def rnd_replacement(index, tag):
    global conf_misses
    conf_misses += 1

    block_num = random.randrange(associativity)
    block = cache[index][block_num]
    block.set_valid(True)
    block.set_tag(tag)

def rr_replacement(index, tag):
    global conf_misses
    global replacement_array
    conf_misses += 1

    block_num = replacement_array[index]
    block = cache[index][block_num]
    block.set_valid(True)
    block.set_tag(tag)
    replacement_array[index] = (block_num + 1) % associativity

def compulsory_miss(index, col, tag):
    global comp_misses
    comp_misses += 1

    block = cache[index][col]
    block.set_valid(True)
    block.set_tag(tag)

def reg_instr(len, addr):
    global total_accesses
    global total_cycles
    global total_instructions
    global total_hits

    total_instructions += 1

    offset = binary_to_dec(addr[int(tag_size) + int(index_size):])
    index = binary_to_dec(addr[int(tag_size):int(tag_size)+int(index_size)])
    tag = binary_to_dec(addr[:int(tag_size)])
    extra_blocks = 0

    if offset + len > block_size:
        extra_blocks += 1
        offset = offset + len - block_size

        while offset > 0:
            extra_blocks += 1
            offset -= block_size

    for i in range(0, extra_blocks + 1):
        total_accesses += 1
        new_index = 0

        if index != 0:
            new_index = (index + i) % index
        else:
            new_index = index + i

        block_found = check_row(new_index, tag)

        if block_found == -1:
            total_cycles += 1
            total_hits += 1
        else:
            total_cycles += (block_size / 4)
            if block_found == -2:
                replacement_method(new_index, tag)
            else:
                compulsory_miss(new_index, block_found, tag)


def check_row(index, tag):
    for i in range(associativity):
        current_block = cache[index][i]

        if not current_block.valid:
            return i
        elif current_block.tag == tag:
            return -1
    return -2

def rw_instr(addr):
    if int(binary_to_dec(addr)) == 0:
        return
    reg_instr(4, addr)
    global total_cycles
    total_cycles += 1

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

    global replacement_method

    if replacement.upper() == 'RR':
        print('%-30s %s' % ('Replacement Policy:', RR))
        replacement_method = rr_replacement
    elif replacement.upper() == 'RND':
        print('%-30s %s' % ('Replacement Policy:', RND))
        replacement_method = rnd_replacement
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
    print("%-30s %d" % ('Cache Hits:', total_hits))
    print("%-30s %d" % ('Cache Misses:', comp_misses + conf_misses))
    print("--- %-30s %d" % ("Compulsory Misses:", comp_misses))
    print("--- %-30s %d" % ("Conflict Misses:", conf_misses))

    print("\n***** ***** CACHE HIT & MISS RATE: ***** *****")
    print("\n%-30s %0.4f%%" % ('Hit Rate:', (total_hits*100/float(total_accesses))))
    print("%-30s %0.4f%%" % ('Miss Rate:', (100-(total_hits*100/float(total_accesses)))))
    print("%-30s %0.2f Cycles/Instruction" % ('CPI', total_cycles/float(total_accesses)))

    unused_cache = ((total_blocks - comp_misses) * (((block_size*8) + tag_size + 1) / 8.0 )) / 1024
    total_cache_size = (total_blocks * ((block_size * 8) + tag_size + 1) / 8.0 ) / 1024

    print("\n%-30s %0.2f KB / %0.2f KB = %0.2f%% Waste: $%0.2f" % ('Unused Cache Space:'
                                                                  , unused_cache
                                                                  , total_cache_size
                                                                  , (unused_cache/total_cache_size) * 100
                                                                  , 0.05 * unused_cache))
    print("%-30s %d / %d" % ('Unused Cache Blocks:', total_blocks - comp_misses, total_blocks))

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

    cache = [[Block() for x in range(associativity)] for y in range(total_rows)]

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
