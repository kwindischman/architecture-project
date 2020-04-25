import sys
import math

class Block:
    def __init__(self, block_size, tag_size):
        self.data = [0 for x in range(block_size)]
        self.valid = True
        self.tag = [tag_size]
        self.tag_size = tag_size

    def is_valid(self):
        return self.valid

    def set_valid(self, is_valid):
        self.valid = is_valid

    def set_tag(self, new_tag):
        for i in range(tag):
            tag[i] = 1 & (newtag >> tag_size-i)

def calculate_values():
    global total_blocks
    global tag_size
    global index_size
    global total_rows
    global overhead_size
    global implementation_mem_size
    global cost

    total_blocks = (cache_size * 1024) / block_size
    total_rows = (cache_size * 1024) / (block_size * associativity)
    index_size = math.log(total_rows, 2)
    tag_size = 32 - math.log(block_size, 2) - index_size
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
                instr_addr = line[10:18]
            elif i % 3 == 1:
                dest_addr = line[6:14]
                src_addr = line[33:41]
            #elif i % 3 == 2:
            #call function that processes data
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

def set_cache():
    global cache
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


if __name__ == '__main__':
    main()
